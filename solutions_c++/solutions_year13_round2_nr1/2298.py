#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;

int n;
vector <int> v;
#define oo 2147483647

int fun (long long A, int i)
{
	if (i == n)
		return 0;
	int l = oo,r = oo;
	if (v[i] < A)
	{
		l = fun (A+v[i],i+1);
	}
	else
	{
		int x = A-1;
		if (v[i] < A+x)
			r= fun (A+x+v[i],i+1)+1;
		
		else
		{
			int r1= oo, r2 = oo;
			if (x)
				r1 = fun (A+x,i)+1;
			r2 = fun(A,i+1)+1;
			r = min (r1,r2);
		}
	}
	/*else if (v[i] == A)
	{
		r = fun(A,i+1)+1;
	}*/
	return min (r,l);
}


int main ()
{
	freopen("A-small.in","r",stdin);
	freopen("out.out","w",stdout);

	int T;
	long long A;


	scanf("%d",&T);
	for (int t=1; t<=T; t++)
	{
		scanf("%lld %d",&A,&n); 
		for (int i=0; i<n; i++)
		{
			int x;
			scanf("%d",&x);
			v.push_back(x);
		}
		sort(v.begin(),v.end());
		int res = fun (A,0);
		printf ("Case #%d: %d\n",t,res);
		v.clear();
	}

	return 0;
}