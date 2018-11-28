#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <sstream>
#include <set>

using namespace std;


int minn;
void insert(set<string> &words, string &sentence)
{
    string w;
    stringstream ss(sentence);
    while (ss >> w) {
        words.insert(w);
    }
}

int calc(set<string> &english, set<string> &french)
{
    set<string> intersect;
    set_intersection(english.begin(), english.end(),
                     french.begin(), french.end(),
                     inserter(intersect, intersect.begin()));
    return intersect.size();
}

int dfs(int d, vector<string> &sentences, set<string> &english, set<string> &french)
{
    int ret = calc(english, french);
    if (minn <= ret) {
        return minn;
    }
    if (d >= sentences.size()) {
        minn = ret;
        return minn;
    }
    set<string> ieng(english), ifr(french);
    insert(ieng, sentences[d]);
    insert(ifr, sentences[d]);
    return min(dfs(d + 1, sentences, ieng, french), dfs(d + 1, sentences, english, ifr));
}



void work()
{
    minn = 100000000;
    vector<string> sentences;
    int n;
    scanf("%d\n", &n);
    string s;
    for (int i = 0; i < n; i++) {
        getline(cin, s);
        sentences.push_back(s);
    }
    set<string> english, french;
    insert(english, sentences[0]);
    insert(french, sentences[1]);
    printf("%d\n", dfs(2, sentences, english, french));
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        work();
    }
    return 0;
}
