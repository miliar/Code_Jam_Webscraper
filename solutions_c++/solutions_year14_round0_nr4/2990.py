#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <limits>
#include <cassert>
#include <sstream>
#include <cmath>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;

const int max_n=1010;
const double eps=1e-12;

int n;
double a[max_n],b[max_n];
int T;

bool lt(double a, double b)
{
	return a+eps<b;
}

int main()
{
	scanf("%d",&T);
	for(int z=0; z<T; z++)
	{
		scanf("%d",&n);
		for(int i=0; i<n; i++)
			cin>>a[i];
		for(int i=0; i<n; i++)
			cin>>b[i];

		sort(a,a+n);sort(b,b+n);

		int j=0,k=n-1;
		int r1=0;
		for(int i=0; i<n; i++)
		{
			if(lt(b[j],a[i]))
			{
				j++;
				r1++;
			}
			else
				k--;
		}

		set<double> S1,S2;
		for(int i=0; i<n; i++)
			S1.insert(a[i]),S2.insert(b[i]);

		int r2=0;
		for(int i=0; i<n; i++)
		{ 
			double x=*(S1.begin());
			set<double>::iterator it=S2.upper_bound(x);
			
			if(it==S2.end())
			{
				r2+=n-i;
				break;
			}
			else
			{
				//cerr<<i<<" "<<x<<" "<<*it<<endl;
				S1.erase(S1.begin());
				S2.erase(it);
			}
		}

		printf("Case #%d: ",z+1);
		printf("%d %d\n",r1,r2);
	}

	return 0;
}