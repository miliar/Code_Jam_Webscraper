#include <cstdio>
#include <algorithm>

using namespace std;
int A,B,K;

int main()
{
	int ss;
	scanf("%d",&ss);
	for(int s=1;s<=ss;++s)
	{
		printf("Case #%d: ",s);
		scanf("%d %d %d",&A,&B,&K);
		unsigned long long res=0;
		int a=min(K,A);
		int b=min(K,B);
		res=a*b;
		res+=(A-a)*b;
		res+=(B-b)*a;
		for(int i=a;i<A;++i)
			for (int j=b;j<B;++j)
				if ((i&j)<K)
					res++;
		printf("%llu\n",res);
	}
}
