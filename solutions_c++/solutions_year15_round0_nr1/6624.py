#include <bits/stdc++.h>
using namespace std;
#define in(var) scanf("%d",&var);
#define out(var) printf("%d\n",var);

int main()
{
	int t,tc;
	in(t);
	tc=t;
	while(t--)
	{
		int n;
		long long int sum=0,ans=0;
		in(n);
		
		string a;
		cin>>a;
        for( int i=0; i<=n; i++)
        {
        	if( (sum<i) && ((a[i]-'0')>0))
        	{
        		ans+=i-sum;
        		sum+=ans;
        		
        	}
        	sum+=(a[i]-'0');
        }
        //cout<<ans<<endl;
		
		cout<<"Case #"<<tc-t<<": "<<ans<<endl;

	}
	return 0;	
	
}