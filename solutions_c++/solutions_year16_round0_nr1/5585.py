#include<bits/stdc++.h>
using namespace std;
set<long long int>s;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int k=1;
	scanf("%d",&t);
	while(t--)
	{
		long long int n,i=1;
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",k++);
			continue;
		}
		s.clear();	
		while(s.size()!=10)
		{
			long long int num=n*i;
			while(num!=0)
			{
				s.insert(num%10);
				num=num/10;
			}
			i++;
		}
		printf("Case #%d: ",k++);
		cout<<n*(i-1)<<endl;
	}
	return 0;
}
