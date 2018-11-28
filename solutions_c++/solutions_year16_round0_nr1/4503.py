#include <bits/stdc++.h>

using namespace std;

#define eb emplace_back
typedef unsigned long long int llu;

int main()
{
	llu n, t;
	cin >> t;
	llu dig[10], sum, val, c=1;
	for (llu i = 0; i < t; i++)
	{
		cin >> n;
		c=1;
		if(n==0){
			printf("Case #%llu: INSOMNIA\n", i+1);
		}else{
			memset(dig, 0, sizeof dig);
			sum=0;
			while(sum<10){
				val = n*c;
				c++;
				
				while(val>0){
					if(dig[val%10]==0){
						dig[val%10]=1;
						sum++;
					}
					val/=10;
					if(sum == 10) break;
				}
			}
			printf("Case #%llu: %llu\n", i+1, n*(c-1));
		}
	}
	
	
	return 0;
}
