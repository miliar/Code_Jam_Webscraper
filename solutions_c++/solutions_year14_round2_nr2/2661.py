#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int t, case_num=0;
	scanf("%d", &t);
	while (t--) {
		unsigned long long a, b, k, res;
		res = 0;
		case_num++;
		scanf("%lld %lld %lld", &a, &b, &k);

		for (int i=0; i<a; i++)
		{
			for (int j=0; j<b; j++)
			{
				if ((i&j) < (k) )
				{
					res++;
				}
			}
		}

		

		printf("Case #%d: %lld\n", case_num, res);
	}
	return 0;
}
