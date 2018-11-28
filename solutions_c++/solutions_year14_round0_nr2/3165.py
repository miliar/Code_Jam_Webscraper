#include<cstring>
#include<cstdio>
#include<iostream>

using namespace std;

const int mn = 20;
const int mm = 1000000007;
const int MAX = 10000000;

int Test;
int n;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin >> Test;
	for ( int Testi = 0; Testi < Test; ++Testi )
	{
		double C, F, X;
		cin >> C >> F >> X;
		double ans = 0 , pre = 0 , product = 2.0;
		pre = X / product;
		int farm = 1;
		for ( farm = 1; farm < MAX; ++farm ) 
		{
			ans += C / product;
			product += F;
			if ( ans + X / product > pre ) 
			{
				ans = pre;
				break;
			}
			pre = ans + X / product;
		}
		printf("Case #%d: %.7lf\n",Testi+1,ans);
	}
}