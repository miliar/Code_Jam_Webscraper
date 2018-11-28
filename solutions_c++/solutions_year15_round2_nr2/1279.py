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
int check(int cur,int r,int c)
{
    int k=0,ans=0,a[r][c];
    rep(i,0,r-1)
    {
        rep(j,0,c-1)
        {
            if((1<<k)&(cur)) a[i][j]=1;
            else a[i][j]=0;
            k++;
 //           cout<<a[i][j]<<' ';
        }
   //     cout<<endl;
    }
    rep(i,0,r-2)
    {
        rep(j,0,c-1)
        {
            if(a[i][j]+a[i+1][j]==2) ans++;
        }
    }
   // cc1(ans);
    rep(i,0,r-1)
    {
        rep(j,0,c-2)
        {
            if(a[i][j]+a[i][j+1]==2) ans++;
        }
    }

   // cc1(ans);
    return ans;
}
int main()
{
	freopen("##inp.cpp","r",stdin);
    freopen("##out.cpp","w",stdout);
	//ios_base::sync_with_stdio(0);
    int t,r,c,x,n;
	cin>>t;
	rep(tes,1,t)
	{
	    int finale=MOD;
	    cin>>r>>c>>x;
        n=r*c;
        rep(i,0,(1<<n)-1)
        {
            if(__builtin_popcount(i)==x)
            {
                //if(i==9)cc2(i,check(i,r,c));
                finale=min(finale,check(i,r,c));
            }
        }
        cout<<"Case #"<<tes<<": ";
        cout<<finale<<endl;
    }
    //check(9,r,c);
}
