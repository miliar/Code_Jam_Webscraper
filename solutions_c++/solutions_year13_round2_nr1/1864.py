#include <stdio.h>
#include <vector>
#include <algorithm>
using std::vector;

int main()
{
	unsigned int nCases = 0;scanf("%d",&nCases);					// 1 <= nCases <= 100
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int a = 0,n = 0;scanf("%d%d",&a,&n);
		vector<int> data(n,0);
		for(unsigned int i = 0;i < n;++i) scanf("%d",&data[i]);
		std::sort(data.begin(),data.end());
		unsigned int sum = 0,ans = n;
		for(unsigned int i = 0;i < n;++i)
		{
			if(a > data[i])
			{
				unsigned int x = sum + n - i - 1;
				if(x < ans) ans = x;
			}
			else
			{
				unsigned int x = sum + n - i;
				if(x < ans) ans = x;

				if(1 == a) break;
				//unsigned int delta = data[i] - a + 1;
				unsigned int u = 0;
				for(;a <= data[i];++u)
				{
					unsigned int t = a - 1;
					a += t;
				}
				//unsigned int u = (delta + a - 2)/(a - 1);

				//unsigned int v = (a - 1)*u;
				//a += v;

				sum += u;
				x = sum + n - i - 1;
				if(x < ans) ans = x;
			}
			a += data[i];
		}

		printf("Case #%u: %u\n",iCases,ans);
	}
	return 0;
}
