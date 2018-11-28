/*	ashish1610	*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tcase=1;tcase<=t;++tcase)
	{
		int A,B,K;
		cin>>A>>B>>K;
		long long int ans=0,temp;
		for(int i=0;i<A;++i)
		{
			for(int j=0;j<B;++j)
			{
				temp=i&j;
				if(temp<K)
					ans++;
			}
		}
		cout<<"Case #"<<tcase<<": "<<ans<<endl;
	}
	return 0;
}
