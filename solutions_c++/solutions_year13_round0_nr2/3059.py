#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <string>

using namespace std;

int T,t;

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>T;
    while (t<T){
        t++;
        int map[200][200]={0};
        int n,m;        
        cin>>n>>m;
        for (int i = 1; i<=n; i++)
            for (int j = 1; j<=m; j++){
                cin>>map[i][j];
            }
        int flag = 1;
        for (int i = 1; i<=n; i++)
            for (int j = 1; j<=m; j++){
                int tmp1 = 1, tmp2 = 1;
                for (int k = 1; k<=n; k++){
                    if (map[k][j]>map[i][j]) tmp1 = 0;
                }
                
                for (int k = 1; k<=m; k++){
                    if (map[i][k]>map[i][j]) tmp2 = 0;
                }
                flag = flag&(tmp1|tmp2);
            }
        if (flag) cout<<"Case #"<<t<<": YES"<<endl;
        else cout<<"Case #"<<t<<": NO"<<endl;
    }
}
