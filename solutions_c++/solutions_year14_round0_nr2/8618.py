#include<iostream>
#include<vector>
#include<climits>
#include<cstdio>
using namespace std;
#define LL long long
int T;

double C, F, X;

int main(void)
{
cin >> T;
	for(int t=0;t<T;t++)
	{
		cin >> C >> F >> X;
		double mini=X/2;
		for(int n=0;;n++)
		{
			double diff=(C-X)/(2+n*F)+X/(2+(n+1)*F);
			if(diff<0)
				mini=mini+diff;
			else break;
		}
		cout << "Case #"<<(t+1)<<": ";
		printf("%.7f\n",mini);
	}
}
