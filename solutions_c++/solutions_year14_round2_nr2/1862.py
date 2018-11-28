#include <iostream>
using namespace std;

int main()
{
	long long t, a, b, k, i, j, l, ans;
	cin>>t;
	for(i=1; i<=t; i++)
	{
		cin>>a>>b>>k;
		ans=0;
		for(j=0; j<a; j++)
		{
			for(l=0; l<b; l++) 
			{
				if((j&l)<k) ans++;
			}
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}

	return 0;
}
