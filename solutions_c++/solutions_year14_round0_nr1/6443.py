#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<set>
using namespace std;

#define ll long long
#define inf 1<<30
#define Mod 10000007
#define dbg printf("%c",a);
#define sz(a) (a).size()
int n,m;int ans;

int main()
{
    int i,j,k,T,cs=0;int x,y,a[5][5],cnt,b[5][5];
    freopen("A-small-attempt0.in","r",stdin);
    freopen("magicout.txt","w",stdout);
    cin>>T;
    //while(scanf("%d",&n)==1)
    while(T--)
    {
        scanf("%d",&x);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>a[i][j];

        scanf("%d",&y);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>b[i][j];

        cnt=0;x--;y--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(a[x][i]==b[y][j])cnt++,ans=a[x][i];
        //cnt/=2;
        //cout<<cnt;
        printf("Case #%d: ",++cs);
        if(cnt==1)cout<<ans<<endl;
        else if(cnt>1)cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }

    return 0;
}

