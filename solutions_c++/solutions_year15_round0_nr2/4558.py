#include <stdio.h>
#include <set>
using namespace std;
multiset<int, greater<int> > myset;
multiset<int, greater<int> > :: iterator it;

int calc(multiset<int, greater<int> > p, int h) {
    int ans = *p.begin(), help = 0;
    for(it = p.begin(); (*it) != 1 && it != p.end(); ) {
        ans = ans < (help + (*it)) ? ans : (help + (*it));
        int a = (*it);
   //     printf("Ok\n");

        if(a % 2 == 0) p.insert(a/2);
        else p.insert(a/2 + 1);
        p.insert(a/2);

        p.erase(it);
        it = p.begin();
        help += 1;
    }
    if(it != p.end()) ans = ans < (help + 1) ? ans : (help + 1);
    return ans;
}

int main() {
    int t, d, p, ans, a, help;
    freopen("B-small-attempt2 (1).in", "r", stdin);
    freopen("Ans", "w", stdout);

    scanf("%d", &t);
    for(int j = 1; j <= t; j++) {
        help = 0;
        scanf("%d", &d);

        for(int i = 0; i < d; i++) {
            scanf("%d", &p);
            myset.insert(p);
        }

        ans = *(myset.begin());
        if(ans == 9) {
            multiset<int, greater<int> > myset2;
            myset2.insert(myset.begin(), myset.end());
            it = myset2.begin();
            int help2 = 0;
            while((*it) == 9) {
                myset2.insert(6);
                myset2.insert(3);
                myset2.erase(it);
                it = myset2.begin();
                help2 += 1;
            }
            help = calc(myset2, help2);
            help = help + help2;
            ans = (ans <= help) ? ans : help;

            myset2.clear();
            help2 = 0;
            myset2.insert(myset.begin(), myset.end());
            it = myset2.begin();
            while((*it) == 9) {
                myset2.insert(5);
                myset2.insert(4);
                myset2.erase(it);
                it = myset2.begin();
                help2 += 1;
            }
            help = calc(myset2, help2);
            help = help + help2;
            ans = (ans <= help) ? ans : help;
            myset2.clear();
        }
        else {
            help = calc(myset, 0);
            ans = (ans <= help) ? ans : help;
        }

        myset.clear();
        printf("Case #%d: %d\n", j, ans);
    }

    fclose(stdout);
    return 0;
}

