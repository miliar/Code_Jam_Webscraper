#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
#define FOR(i,N) for(int i=0;i<N;i++)
#define FORV(i,V,N) for(int i=V;i<N;i++)
int main()
{
	int T;
	cin>>T;
	FORV(t,1,T+1)
	{
		int K=0;
		int ans=0;
		int Smax;
		string shy;
		cin>>Smax>>shy;
		FOR(i,Smax+1)
		{
			if(K<i)
			{
				ans+=(i-K);
				K+=(i-K);
			}
			K+=shy[i]-'0';
			//cout<<"i: "<<i<<" K: "<<K<<endl;
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	
	
}

