#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int mp[105][105];
int main()
{
    //freopen("Input.txt","r",stdin);
   // freopen("Output.txt","w",stdout);
    int T,k = 1;
    cin>>T;
    while(T--){
        int n,m;
        cin>>n>>m;
        cout<<"Case #"<<k++<<": ";
        for(int i = 0;i < n;++i){
            for(int j = 0;j < m;++j)
                cin>>mp[i][j];
        }
        bool flag = false,flag1;
        for(int i = 0;i < n;++i){
            for(int j = 0;j < m;++j){
                flag1 = false;
                for(int k = j;k >= 0;--k){
                    if(mp[i][k] > mp[i][j]){
                        flag1 = true;
                        break;
                    }
                }
                if(!flag1){
                    for(int k = j;k < m;++k){
                        if(mp[i][k] > mp[i][j]){
                            flag1 = true;
                            break;
                        }
                    }
                }
                if(!flag1) continue;
                flag1 = false;
                for(int k = i;k >= 0;--k){
                    if(mp[k][j] > mp[i][j]){
                        flag1 = true;
                        break;
                    }
                }
                if(!flag1){
                    for(int k = i;k < n;++k){
                        if(mp[k][j] > mp[i][j]){
                            flag1 = true;
                            break;
                        }
                    }
                }
                if(!flag1) continue;
                flag = true;
                break;
            }
            if(flag) break;
        }
        if(!flag) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
