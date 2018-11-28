/** Author :  Rounak Patni IIIT-H
_._._._._._._._._._._._._._._._._._._._._.*/
                                   
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <vector>
#include <cstring>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <queue>
using namespace std;
int MAX(long long int a, long long int b){if(a > b){return a;}else{return b;}}
int MIN(long long int a, long long int b){if(a < b){return a;}else{return b;}}
int gcd ( long long int a, long long int b ){long long int c;while ( a != 0 ) {c = a; a = b%a;  b = c;}return b;}
//long long int power(long long int  a, long long int  b) { long long int  x=1, y=a; while(b>0) { if(b%2==1) x=(x*y)%mod; y=(y*y)%mod; b=b/2;}     return x; }
int main()
{

	int t;
	cin >> t;
	for(int t1=1;t1<=t;t1++)
	{
		double c,f,x;
		cin >> c;
		cin >> f;
		cin >> x;
		double ans=9999999999.999999;

		double ini=2.0;	
		double time=0.0;
		while(1)
		{
			double f1=x/ini;
			if(f1+time < ans)
			{
				ans=f1+time;
			}
			if(ini > x+20000.0)
			{
				break;
			}
			time=(time)*1.0+(c*1.0)/(ini*1.0);
			ini=ini+f;
		}
		printf("Case #%d: %.7lf\n",t1,ans);
	}
	return 0;

}
