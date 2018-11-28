#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>

#define FOR(i,a,b) for(int i = (a); i <= (b);i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)

using namespace std;

multiset<int> se;
int n,C;
int main() 
{
    freopen("AA2.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> n >> C;
        se.clear();
        int X;
        FOR(i,1,n) {
            cin >> X;
            se.insert(X);
        }
        int res = 0;
        while (se.size()) {
            res++;
                
            multiset<int>::iterator tmp = se.end(); 
            
            tmp--;
            int cur = *tmp;
            se.erase(tmp);
            if (se.size()) {
                
                tmp = se.lower_bound(C-cur);
                
                if (tmp == se.end()) {
                    tmp--;
                }
                int now = *tmp;
                if (cur + now <= C) {
                    se.erase(tmp);
                    continue;
                }
                if (tmp != se.begin()) {
                    tmp--;
                    now = *tmp;
                    if (cur + now <= C) {
                        se.erase(tmp);
                        continue;
                    }
                }
            } 
        }
        cout << res << endl;
    }
    return 0;
}

