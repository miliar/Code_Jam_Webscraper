#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("Bin.in","r",stdin);
	freopen("Bout.txt","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		int A,B,K,ans=0;
		cin>>A>>B>>K;
		for(int i=0;i<A;i++)
			for(int j=0;j<B;j++)
				if((i&j)<K)
					ans++;
		cout<<ans<<endl;
	}
	return 0;
}
