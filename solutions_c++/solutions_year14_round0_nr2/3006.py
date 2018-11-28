#include<iostream>
#include<map>
#include<string>
#include<string.h>
#include<vector>
#include<stdio.h>
#include <cstdio>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <cmath>
#include <bitset>
#include <limits.h>
#include <limits>
#include <utility>
#include <set>
#include <numeric>
#include <functional>
#define R(i) freopen(i,"r",stdin)
#define W(i) freopen(i,"w",stdout)
#define R_W R("i.txt"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define inf numeric_limits<int>::max()
#define minf numeric_limits<int>::min()
#define DFS_WHITE -1
#define DFS_BLACK 1
using namespace std;
double c, x ,f;
double timeToFinish(double cf){
	return max(double(0), (x) / cf);
}
int main(){
	R_W;
	int T;
	int cases = 1;
	cin >> T;
	while (T--)
	{

		scanf("%lf %lf %lf",&c,&f,&x);
		double t = 0, cf, cx = 0;
		cf = 2;
		while (true)
		{
			double t1 = (x / cf);
			double t2 = (c / cf) + (x / (cf + f));
			if (t1 < t2)
			{
				t += t1;
				break;
			}
			t += (c / cf);
			cf += f;
		}
		printf("Case #%d: %.7lf\n", cases++, t);
	}
	return 0;
}