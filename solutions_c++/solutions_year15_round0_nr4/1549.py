#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll a[1001];
ll dp[1001][1001];
int main()
{
	ll i,j,k,l,m,n,t,x,r,c;
	scanf("%lld",&t);
	j=1;
	while(t--)
	{
		scanf("%lld",&x);
		scanf("%lld",&r);
		scanf("%lld",&c);
		if(x==1)
		cout<<"Case #"<<j<<": GABRIEL"<<endl;
	    else if(x==2)
	    {
	    	if((r*c)%2!=0)
	    	cout<<"Case #"<<j<<": RICHARD"<<endl;
	    	else
	    	cout<<"Case #"<<j<<": GABRIEL"<<endl;
	    }
	    else if(x==3)
	    {
	    	if(c==1 ||r==1)
	    	cout<<"Case #"<<j<<": RICHARD"<<endl;
	        else if(c==3 || r==3)
	        cout<<"Case #"<<j<<": GABRIEL"<<endl;
	        else
            cout<<"Case #"<<j<<": RICHARD"<<endl;
	    }
	    else
	    {
            if(r==1 || c==1 || (r*c)%4!=0 || (r==2 && c==2))
            cout<<"Case #"<<j<<": RICHARD"<<endl;
            else if((r==4 && c==2) || (r==2 && c==4))
            cout<<"Case #"<<j<<": RICHARD"<<endl;
            else
            cout<<"Case #"<<j<<": GABRIEL"<<endl;
	    }
		j++;
	}
	return 0;
}
