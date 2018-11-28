//Author : Jatin Goyal
//codecracker4

#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007  //NA
#define N 111111
#define ll long long int
#define dt int
#define all(c) c.begin(), c.end()
#define dcl(a) memset(a,0,sizeof(a))
#define rep(i,a,b) for(dt i=a;i<=(dt)b;i++)
#define tr(container, it) for(vector<dt> ::iterator it= container.begin(); it!=container.end(); it++)
#define trp(container, it) for(vector<pair<dt,dt> >::iterator it = container.begin(); it!=container.end(); it++)
#define tra(container, it) for(typeof(container.begin()) it = container.begin(); it!=container.end(); it++)
#define cc1(a)cout<<#a<<": "<<a<<endl;
#define cc2(a,b)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<< endl;
#define cc3(a,b,c)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<endl;
#define cc4(a,b,c,d)cout<<#a<<": "<<a<<" , "<<#b<<": "<<b<<" , "<<#c<<": "<<c<<" , "<<#d<<": "<<d<<endl;
#define pr pair<dt,dt>  //NA
#define mp(a,b) make_pair(a,b)
#define pb push_back  //NA
#define gc getchar  //NA
#define F first
#define S second
int dp[11][11];
int vis[11111];
int fun(char c)
{
    if(c=='i') return 2;
    if(c=='j') return 3;
    if(c=='k') return 4;
}
int main()
{
    dp[1][1]=1;dp[1][2]=2;dp[1][3]=3;dp[1][4]=4;
    dp[2][1]=2;dp[2][2]=-1;dp[2][3]=4;dp[2][4]=-3;
    dp[3][1]=3;dp[3][2]=-4;dp[3][3]=-1;dp[3][4]=2;
    dp[4][1]=4;dp[4][2]=3;dp[4][3]=-2;dp[4][4]=-1;
	freopen("##inp.cpp","r",stdin);
    freopen("##out.cpp","w",stdout);
	//ios_base::sync_with_stdio(0);
	int t,x,y,sgn,ans,tes,fg;
	string dum;
	cin>>t;
	rep(tes,1,t)
    {
        fg=0;
        cin>>x>>y>>dum;
        string str;

        dcl(vis);
        while(y--) str=str+dum;
        ans=1;
        sgn=1;

        for(int i=str.size()-1;i>=0;i--)
        {
            if(str[i]=='i') vis[i]=1;
            else break;
        }
        vis[str.size()]=1;

        rep(i,0,str.size()-1)
        {

            if(dp[abs(ans)][fun(str[i])]>0) ans=dp[abs(ans)][fun(str[i])];
            else {ans=-dp[abs(ans)][fun(str[i])]; sgn=-sgn;}
           // cc3(str[i],ans,sgn);
        }

        if(ans*sgn==-1)
        {
            ans=1;
            sgn=1;
            rep(i,0,str.size()-1)
            {

                if(dp[abs(ans)][fun(str[i])]>0) ans=dp[abs(ans)][fun(str[i])];
                else {ans=-dp[abs(ans)][fun(str[i])]; sgn=-sgn;}
                if((ans*sgn==2)&&(vis[i+1]==0))fg=1;
            }
        }
        printf("Case #%d: ",tes);
        if(fg==1) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }

}
