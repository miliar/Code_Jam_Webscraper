#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

int A,B,K;

int main(void)
{
	freopen("C:\\Users\\ytimex\\Desktop\\gcj\\round1b\\B-small-attempt0.in","rb",stdin);
	freopen("C:\\Users\\ytimex\\Desktop\\gcj\\round1b\\B-small-attempt0.out","wb",stdout);
	int T,t=1;
	cin>>T;
	while(t<=T)
	{
		cin>>A>>B>>K;
		long long ans=0;
		int i,j;
		for(i=0;i<A;i++)
		{
			for(j=0;j<B;j++)
			{
				if((i&j)<K)
				{
					ans++;
					//cout<<i<<" "<<j<<endl;
				}
				//cout<<(i&j)<<endl;
			}
		}
		printf("Case #%d: %lld\n",t,ans);
		t++;
	}
	return 0;
}
