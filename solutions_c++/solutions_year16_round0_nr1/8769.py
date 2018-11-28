#include <bits/stdc++.h>
#define ll long long int
#define rep(a,c)   for ( ll (a)=0; (a)<(c); (a)++)
#define nl cout<<endl
using namespace std;

int main(){
	ll T,n,n1,r,ans;
	cin>>T;
	ll d[10];
	
	for (int t = 0; t < T; ++t)
	{
		/* code */
		for (int i = 0; i < 10; ++i)
		{
			/* code */
			d[i]=0;
		}
		cin>>n;
		ans=0;
		cout<<"Case #"<<t+1<<": ";
		if (n==0)
		{
			/* code */
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		for (int i = 1;; ++i)
		{
			/* code */
			n1=n;
			n1*=i;
			while(n1!=0){
				r=n1%10;
				n1/=10;
				if (r<0)
				{
					/* code */
					r+=10;
				}
				if (d[r]==0)
				{
					/* code */
					d[r]=1;
					ans++;
				}
			
			}
			if(ans==10){
					cout<<n*i<<endl;
					break;
			}
		}
		// cout<<ans<<endl;

	}

	return 0;
}