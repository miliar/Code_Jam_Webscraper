#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int main(){
    //ios::sync_with_stdio(0);
    
    int TC,N;
    long long p,q,r,s;
    long long sum[1000001];
    
    cin >> TC;
    
    for(int tc = 1;tc <= TC;++tc){
        cin >> N >> p >> q >> r >> s;
        sum[0] = 0;
        
        for(int i = 0;i < N;++i){
            sum[i + 1] = sum[i] + ((i * p + q) % r + s);
        }
        
        long long best = sum[N];
        
        for(int i = 0;i < N;++i){
            /*for(int j = i;j < N;++j){
                best = min(best,max(sum[i],max(sum[j + 1] - sum[i],sum[N] - sum[j + 1])));
            }*/
            
            int lo = i,hi = N - 1,mi;
            
            while(lo < hi){
                mi = (lo + hi + 1) >> 1;
                
                if(sum[N] - sum[mi + 1] < sum[mi + 1] - sum[i]) hi = mi - 1;
                else lo = mi;
            }
            
            best = min(best,max(sum[i],max(sum[lo + 1] - sum[i],sum[N] - sum[lo + 1])));
            
            if(lo + 1 < N){
                ++lo;
                best = min(best,max(sum[i],max(sum[lo + 1] - sum[i],sum[N] - sum[lo + 1])));
            }
        }
        
        best = sum[N] - best;
        
        cout << "Case #" << tc << ": ";
        printf("%.10f\n",(double)best / sum[N]);
    }
    
    return 0;
}
