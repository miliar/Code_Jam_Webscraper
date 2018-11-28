#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>
#define xx first
#define yy second
#define mp(a,b) make_pair(a,b)
using namespace std;
typedef pair<int,int>p1;
string ans;
int n,r,p,s;
p1 get(char c){
    if(c=='R'){
        return mp('S','R');
    }
    else if(c=='P') return mp('P','R');
    else return mp('P','S');
}
char c[100005],d[100005];
int flag;
void dfs(int q,int x,int y,int z){
    if(q==n+1){
        if(x==r&&y==p&&z==s){
            string ss="";
            int pp=1<<n;
            for(int i=0;i<pp;i++){
                ss+=c[i];
            }
            if(flag==0){
                ans=ss;
            }
            else{
                if(ans>ss){
                    ans=ss;
                }
            }
            flag=1;
        }
        return;
    }
    if(q==0){
        c[0]='P';
        dfs(1,0,1,0);
        c[0]='S';
        dfs(1,0,0,1);
        c[0]='R';
        dfs(1,1,0,0);
    }
    else{
        int pp=1<<(q-1);
        int tot=0;
        x=0;
        y=0;
        z=0;
        for(int i=0;i<pp;i++){
            p1 p2=get(c[i]);
            if(q==n&&c[i]=='R'){
                p2=mp('R','S');
            }
            if(q<n-1&&c[i]=='S'){
                p2=mp('S','P');
            }
            d[tot++]=p2.xx;
            d[tot++]=p2.yy;
        }
        for(int i=0;i<tot;i++){
            c[i]=d[i];
            if(c[i]=='R') x++;
            else if(c[i]=='P') y++;
            else z++;
        }
        dfs(q+1,x,y,z);
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,N=0;
    cin>>t;
    while(t--){
        cin>>n>>r>>p>>s;
         flag=0;
        dfs(0,0,0,0);
        printf("Case #%d: ",++N);
        if(flag) cout<<ans<<endl;
        else printf("IMPOSSIBLE\n");
    }
}