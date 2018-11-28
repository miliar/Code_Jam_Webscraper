#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cstring>
#include <functional>
#include <cmath>
#define CLR(a) memset(a,0,sizeof(a))
typedef long long ll;
int a[5][5],b[5][5];
int x,y;
bool h[17],g[17];
using namespace std;
int main(){
    //freopen("A-small-attempt2.in","r",stdin);
    //freopen("out.txt","w",stdout);
    ios::sync_with_stdio(0);
    int t;
    cin>>t;
    int cs = 1;
    while(cs<=t){
        cin>>x;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>a[i][j];
        cin>>y;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>b[i][j];

        vector<int> va,vb,ans;
        for(int i=1;i<=4;i++){
            va.push_back(a[x][i]);
            vb.push_back(b[y][i]);
        }
        // memset(h,0,sizeof(h));
        // memset(g,0,sizeof(g));
        // for(int i=0)

        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(va[i] == vb[j])
                    ans.push_back(va[i]);
            }
        }
        cout<<"Case #"<<cs<<": ";
        if(ans.size() == 0)
            cout<<"Volunteer cheated!\n";
        else if(ans.size() == 1)
            cout<<ans[0]<<endl;
        else
            cout<<"Bad magician!\n";
        cs++;
    }

}