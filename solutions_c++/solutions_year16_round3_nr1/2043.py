#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

bool myFunc(pair<char, int> a, pair<char, int> b) {
    return a.second > b.second;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        char tmChar = 'A';
        //case num
        int n, total = 0, tmp;
        scanf("%d", &n);
        vector<pair<char, int>> sen(n);
        for(int i = 0; i < n; i++) {
            scanf("%d", &tmp);
            total += tmp;
            sen.push_back(make_pair(tmChar++, tmp));
        }
        while(total) {
            sort(sen.begin(), sen.end(), myFunc);
            if(sen[0].second) {
                printf("%c", sen[0].first);
                sen[0].second--;
                total--;
            }
            if(total - 1 && (double)sen[1].second / (total - 1) <= .5 && sen[0].second) {
                printf("%c", sen[0].first);
                sen[0].second--; total--;
                if(total)
                    printf(" ");
                continue;
            }
            if(sen[1].second && (double)sen[0].second / (total - 1) <= .5 || total == 1) {
                if(total > 1 && n > 2 && (double)sen[2].second / (total - 1) > .5) {
                    if(total)
                        printf(" ");
                    continue;
                }
                printf("%c", sen[1].first);
                sen[1].second--; total--;
            }
            if(total)
                printf(" ");
        }
        puts("");
    }

    return 0;
}