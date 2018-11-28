//Author : Jatin Goyal
//codecracker4

#include<bits/stdc++.h>
using namespace std;
#define MOD 1e18  //NA
#define N 11111
#define ll long long int
#define dt ll
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
ll t,maxe,ans1,ans2,n,cur,dum,a[N],las,fg;
int main()
{
	freopen("##inp.cpp","r",stdin);
    freopen("##out.cpp","w",stdout);
	//ios_base::sync_with_stdio(0);
	cin>>t;
	rep(tes,1,t)
	{
	    maxe=0;
	    cin>>n;
	    rep(i,0,n-1) {cin>>a[i]; maxe=max(maxe,a[i]);}
	    las=a[0];
	    ans1=0;
	    rep(i,1,n-1)
	    {
	        if(a[i]>las);
	        else ans1+=las-a[i];
	        las=a[i];
	    }
	    ans2=MOD;
	    rep(i,0,maxe*10)
	    {
	        cur=a[0];
	        dum=0;
	        fg=0;
	        rep(j,1,n-1)
	        {
	            dum+=min(cur,i);
	            cur=max(0ll,cur-i);
	            //cc2(dum,cur);
	            if(cur>a[j]) {fg=1; break;}
	            else cur=a[j];
	        }
	        //cc3(i,dum,cur);
	        if(fg==0) ans2=min(ans2,dum);
	    }
	    cout<<"Case #"<<tes<<": "<<ans1<<' '<<ans2<<endl;
	}
}
