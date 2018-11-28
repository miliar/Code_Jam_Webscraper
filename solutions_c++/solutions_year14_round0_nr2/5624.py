#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int TEST = 1,T;
	cin >> T;
	while(T--)
	{
		double C,F,X;
		double ans = 1e9, tot = 0;
		cin >> C >> F >> X;
		for(int i = 0 ; i <= 1000000; i++)
		{
			ans = min(ans,tot + (X / (2 + F*i)));
			tot += C / (2 + F*i);
		}
		printf("Case #%d: %.9lf\n",TEST++,ans);
	}
	return 0;
}
