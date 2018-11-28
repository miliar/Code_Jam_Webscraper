#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>

typedef long long ll;

using namespace std;
#define K 1000
int main(){
    int T;
    scanf("%d",&T);
    for(int t=0;t++<T;){
        int N;
        scanf("%d",&N);
        vector<ll> V;
        for(int i = 0;i<N;i++){
            ll tmp;
            scanf("%lld",&tmp);
            V.push_back(tmp);
        }
        int ret = 0;
        for(int i = 0;i<N;i++){
            int min = K*K*K + 1;
            int index = 0;
            for(int j = 0; j<V.size();j++){
                if(V[j] < min){
                    min = V[j];
                    index=j;
                }
            }
            if(index < (V.size()-index-1))
                ret+=index;
            else
                ret += V.size()-index-1;
            V.erase(V.begin()+index);
        }
        printf("Case #%d: %d\n", t, ret);
    }
    return 0;
}
