#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <set>
#include <algorithm>
#include <map>
#include <vector>
#include <deque>

using namespace std;

int N, M, K, T;
int X, C;
char input[65535];
long long ss[20][20];
int ss_num[20];

set<long long> lang[3];
set<long long> new_lang[3];

int run_res = 10000000;

long long get_ll(char *p)
{
    long long res = 0;
    for(; *p != '\0'; ++p) {
        res *= 32;
        res += (*p - 'a' + 1);
    }
    return res;
}

int get_sure(int k)
{
    //printf("==========\n");
    //printf("%s", input);
    //printf("==========\n");
    char *p = input;

    for(; *p != '\0'; ++p) {
        char *head = p;
        for(; *p != ' ' && *p != '\0' && *p != '\n' && *p != '\r'; ) {
            ++p;
        }
        if(*p == '\0' || *p == '\n' || *p == '\r') {
            *(p + 1) = '\0';
        }
        *p = '\0';
        long long s = get_ll(head);
        //cout << "get_new_word " << s << endl;
        if(lang[2].count(s) > 0) {
            continue;
        }
        set<long long>::iterator it = lang[1 - k].find(s);
        if(it == lang[1 - k].end()) {
            lang[k].insert(s);
        } else {
            lang[2].insert(s);
            lang[1 - k].erase(it);
        }
    }
    //cout << "--------------" << endl;
    return 0;
}

int fenci(int k)
{
    char *p = input;
    int word_num = 0;
    for(; *p != '\0'; ++p) {
        char *head = p;
        for(; *p != ' ' && *p != '\0' && *p != '\n' && *p != '\r'; ) {
            ++p;
        }
        if(*p == '\0' || *p == '\n' || *p == '\r') {
            *(p + 1) = '\0';
        }
        *p = '\0';
        long long s = get_ll(head);
        if(lang[2].count(s) > 0) {
            continue;
        }
        ss[k][word_num++] = s;
    }
    ss_num[k] = word_num;
    return word_num;
}

int try_put(int idx, int k)
{
    for(int i = 0; i < ss_num[idx]; ++i) {
        if(new_lang[2].count(ss[idx][i]) > 0) {
            continue;
        }
        set<long long>::iterator it = lang[1 - k].find(ss[idx][i]);
        if(it == lang[1 - k].end()) {
            it = new_lang[1 - k].find(ss[idx][i]);
            if(it == new_lang[1 - k].end()) {
                new_lang[k].insert(ss[idx][i]);
            } else {
                new_lang[1 - k].erase(it);
                new_lang[2].insert(ss[idx][i]);
            }
        } else {
            new_lang[2].insert(ss[idx][i]);
        }
    }
    return 0;
}

int gaoyigao(int key)
{
    new_lang[0].clear();
    new_lang[1].clear();
    new_lang[2].clear();
    int bit_flag = 1;
    for(int i = 0; i < N; ++i, bit_flag *= 2) {
        if(key & bit_flag) {
            try_put(i, 0);
        } else {
            try_put(i, 1);
        }
        if(new_lang[2].size() + lang[2].size() > run_res) {
            break;
        }
    }

    //printf("gaoyigao %d res %d\n", key, int(new_lang[2].size()));
    return new_lang[2].size() + lang[2].size();
}

int run()
{
    lang[0].clear();
    lang[1].clear();
    lang[2].clear();
    scanf("%d", &N);
    fgets(input, sizeof(input), stdin);
    fgets(input, sizeof(input), stdin);
    get_sure(0);
    fgets(input, sizeof(input), stdin);
    get_sure(1);
    N -= 2;
    for(int i = 0; i < N; ++i) {
        fgets(input, sizeof(input), stdin);
        int ret = fenci(i);
        if(ret == 0) {
            --i;
            --N;
        }
    }
    if(N == 0) {
        cout << lang[2].size() << endl;
        return 0;
    }

    // for(int i = 0; i < N; ++i) {
    //     printf("[%d]", ss_num[i]);

    //     for(int j = 0; j < ss_num[i]; ++j) {
    //         printf("[%s] ", ss[i][j].c_str());
    //     }

    //     printf("\n");
    // }
    run_res = 10000000;
    int max_try = (1 << N);
    for(int i = 0; i < max_try; ++i) {
        run_res = min(run_res, gaoyigao(i));
    }
    printf("%d\n", run_res);

    return 0;
}

int main()
{
    scanf("%d", &T);
    for(int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        run();
    }
    return 0;
}


