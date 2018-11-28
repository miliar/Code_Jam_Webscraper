#include <iostream>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <vector> 
#include <cstdio>
#include <stack>
#include <cassert>
#include <sstream>
using namespace std;  

int dp[1000+10][1000+10];
int data[1000+10];
int org[1000+10]; 
int table[1000+10][1000+10];
int main (){ 
    int T;
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout); 
    cin >> T ;
    for(int Cas = 1; Cas <= T; ++Cas){ 
        int N; 
        cin >> N ;
        for(int i=1; i <= N; ++i){
            cin >> data[i];
        } 
        int tmp[1000+10]; 
        for(int i=1; i <= N; ++i){
            int cnt = 0; 
            for(int j= 1; j <= N ; ++j){ 
                if(data[i] >= data[j])
                    ++cnt; 
            }
            tmp[i] = cnt ; 
        }

        for(int i=1; i <= N; ++i){
            table[i][i]=0;
            for(int j=i-1; j >=1; --j){ 
                table[i][j] = table[i][j+1]+ (data[i] < data[j]); 
            }
            for(int j=i+1; j <= N; ++j){
                table[i][j] = table[i][j-1]+ (data[i] < data[j]);
            }
        }

        memcpy(data, tmp, sizeof(tmp)); 
        int to[1000+10]; 
        for(int i=1; i <= N; ++i)
            to[data[i]] = i ; 
        memset(dp,0x3f,sizeof(dp));
        dp[0][0]=0; 
        for(int i=0; i < N ; ++i){
            for(int j=0; j <= i ; ++j){ 
                int left = j, right = i - j;
                int next = i + 1; 
                dp[i+1][j+1] = min(dp[i+1][j+1], 
                        dp[i][j] + table[to[next]][1]); 
                dp[next][j] = min(dp[next][j],
                        dp[i][j] + table[to[next]][N]);
            }
        }
        int ans = 0x3f3f3f3f; 
        for(int i=0; i <= N ; ++i)
            ans = min(ans, dp[N][i]);
        cout << "Case #"<<Cas<<": "<<ans<<endl; 
    }
    return 0;
}

                
                
        
