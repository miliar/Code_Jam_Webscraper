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
    ios::sync_with_stdio(0);
    
    int TC;
    
    cin >> TC;
    
    int N,X,S[10000];
    bool used[10000];
    
    for(int tc = 1;tc <= TC;++tc){
        cin >> N >> X;
        
        for(int i = 0;i < N;++i)
            cin >> S[i];
        
        sort(S,S + N);
        
        int ans = 0;
        memset(used,false,sizeof used);
        
        for(int i = 0;i < N;++i){
            if(!used[i]){
                used[i] = true; ++ans;
                
                for(int j = N - 1;j > i;--j)
                    if(!used[j] && S[i] + S[j] <= X){
                        used[j] = true;
                        break;
                    }
            }
        }
        
        cout << "Case #" << tc << ": " << ans << endl;
    }
    
    return 0;
}
