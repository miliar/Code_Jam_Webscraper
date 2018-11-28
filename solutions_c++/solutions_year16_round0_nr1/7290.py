#include <cstdio>
#include <cstring>
#include <map>
#include <queue>
#include <deque>
#include <algorithm>
#include <iostream>
#include <string>
#include <stack>
using namespace std;
typedef long long LL;
#define MAXN 100


int main()
{
    int T;
    
    freopen("/Users/thedream/Desktop/cpp/cpp/input","r",stdin);
    freopen("/Users/thedream/Desktop/cpp/cpp/output","w",stdout);
    
    scanf("%d",&T);
    
    int N;
    for (int t=1;t<=T;t++) {
        scanf("%d",&N);
        int ans=N;
        if(N==0) {
            printf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        
        int ck[10] = {0,},cnt=0;
        for(int k=N;;k+=N){
            int tmp = k;
            
            while(tmp){
                if ( !ck[tmp%10] ) {
                    ck[tmp%10] = 1;
                    cnt++;
                }
                tmp /=10;
            }
            if(cnt == 10){
                ans = k;
                break;
            }
        }
        
        
        printf("Case #%d: %d\n",t,ans);
    }
    
    return 0;
}