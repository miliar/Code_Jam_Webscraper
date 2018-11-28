//Author : Jatin Goyal
//codecracker4

#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007  //NA
#define N 111
#define ll long long int
#define dt int
#define all(c) c.begin(), c.end()
#define dcl(a) memset(a,0,sizeof(a))
#define rep(i,a,b) for(dt i=a;i<=(dt)(b);i++)
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
int fg,r,c,ans,a[N][N],visited[N][N];
int dfs(int i,int j,int ct,char cv)
{
    if((i==0)&&(cv=='^'))
    {
        //cc1("fhd");
        ans++;
        return 0;
    }
    if((i==r+1)&&(cv=='v'))
    {
        ans++;
        return 0;
    }
    if((j==c+1)&&(cv=='>'))
    {
        ans++;
        return 0;
    }
    if((j==0)&&(cv=='<'))
    {
        ans++;
        return 0;
    }
    if(a[i][j]!='.') visited[i][j]=1;
    if(a[i][j]=='.') {a[i][j]=cv; ct--;}
    if((a[i][j]=='>')&&(visited[i][j+1]==0)) dfs(i,j+1,ct+1,a[i][j]);
    if((a[i][j]=='<')&&(visited[i][j-1]==0)) dfs(i,j-1,ct+1,a[i][j]);
    if((a[i][j]=='^')&&(visited[i-1][j]==0)) dfs(i-1,j,ct+1,a[i][j]);
    if((a[i][j]=='v')&&(visited[i+1][j]==0)) dfs(i+1,j,ct+1,a[i][j]);
}
int main()
{
    freopen("##inp.cpp","r",stdin);
    freopen("##out.cpp","w",stdout);
	//ios_base::sync_with_stdio(0);
	int t;
	string str;
	cin>>t;
	rep(tes,1,t)
	{
	    dcl(visited);
	    ans=0;
	    fg=0;
	    cin>>r>>c;
	    rep(i,1,r)
	    {
	        cin>>str;
	        rep(j,1,c){a[i][j]=str[j-1]; a[i][j]=str[j-1];}
	    }
	    rep(i,1,r)
	    {
	        rep(j,1,c)
	        {
	            if(a[i][j]!='.')
                {
                    int x=0,y=0;
                    rep(k,1,c) if(a[i][k]!='.') x++;
                    rep(k,1,r) if(a[k][j]!='.') y++;
                    if((x==1)&&(y==1)) fg=1;
                }
	        }
	    }

	    rep(i,1,r)
        {
            rep(j,1,c)
            {
                if(a[i][j]!='.') dfs(i,j,1,'.');
            }
        }
        cout<<"Case #"<<tes<<": ";
        if(fg==1) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<endl;
	}
}
