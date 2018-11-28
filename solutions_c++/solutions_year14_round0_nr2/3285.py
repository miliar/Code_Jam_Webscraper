#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>

#define SQR(_x) ((_x)*(_x))
//#define REP(_i,_n) for(int _i = 0; _i < (int)(_n); _i++)
//#define FOR(_i,_a,_b) for(int _i = (int)(_a); _i <= (int)(_b); _i++)
//#define BCK(_i,_a,_b) for(int _i = (int)(_a); _i >= (int)(_b); _i--)
#define NL printf("\n")
#define LL long long
#define INF 1000000000

using namespace std;


double frm[100100]={};
double minn=INF;

int main()
{
	int t;
	double c,f,x,di;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> c >> f >> x;
		minn = x/2;
		di=2;
		for(int j = 1;; j++)
		{
			frm[j]=frm[j-1]+(c/di);
			di+=f;
			if(minn>frm[j]+(x/di))
			{
				minn = frm[j]+(x/di);
			}
			else
			{
				printf("Case #%d: %.7lf\n",i,minn);
				break;
			}
		}
	}
	return 0;
}