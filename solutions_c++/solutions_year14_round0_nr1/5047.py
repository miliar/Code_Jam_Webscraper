#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
#include<iomanip>
#include<vector>
#include<ctime>
#include<cstdlib>
#include<sstream>
#include<set>
#include<cstdio>
using namespace std;

typedef long long ll;
ll n,mod=1000000007;
int vis[20],x;

int main(){
    int t;
    //freopen("A-small-attempt3.in","r",stdin);
    cin>>t;
    //freopen("A-small-attempt0.out","w",stdout);
    for(int ca=1;ca<=t;ca++){
        cin>>n;
        memset(vis,0,sizeof(vis));
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {
            cin>>x;if(i==n)vis[x]=1;
        }
        cin>>n;
        for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
        {
            cin>>x;if(i==n)vis[x]++;
        }
        int ans=-1;
        for(int i=1;i<=16;i++)
        if(vis[i]==2){
            if(ans==-1)ans=i;
            else ans=-2;
        }
        printf("Case #%d: ",ca);
        if(ans==-1)cout<<"Volunteer cheated!\n";
        else if(ans==-2)cout<<"Bad magician!\n";
        else cout<<ans<<endl;
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
