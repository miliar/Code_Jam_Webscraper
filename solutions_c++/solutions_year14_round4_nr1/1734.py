#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

#define N 10012

#define pb push_back
#define ii pair<int, int>

vector<int> v;

bool cmp(int a, int b){
    return a > b;
}


int main(){
    int t, nt, n, x, s;

    scanf("%d", &nt);
    for(int t = 0; t < nt; ++t){
        v.clear();
        scanf("%d %d", &n, &x);
        for(int i = 0; i < n; ++i){
            scanf("%d", &s);
            v.pb(s);
        }
        sort(v.begin(), v.end());
        reverse(v.begin(), v.end());
        
        int res = 0;
        vector<int>::iterator it;
        vector<int>::iterator it2;
        for(it = v.begin(); it != v.end();){
            int achou = 0;
            it2 = lower_bound(v.begin(), v.end(), x-(*it), cmp);
            if(it2 == it) it2++;
            if(it2 != v.end() && *it2+(*it)<=x && (int)(it2-it) != 0){
                res++;
                v.erase(it2);
                achou = 1;                  
            }
            if(!achou && it2 != v.end() && (int)(it2-it) != 0){
                it2++;
                if(it2 != v.end() && *it2+*it <= x && (int)(it2-it) != 0){
                    res++;
                    v.erase(it2);
                    achou = 1;
                }
            }
            if(!achou){
                res++;
            }
            v.erase(it);
            it = v.begin();
            
        }
        printf("Case #%d: %d\n", t+1, res);
    }

    return 0;
}
