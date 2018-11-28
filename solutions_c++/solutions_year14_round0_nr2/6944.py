#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <map>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <climits>
#include <set>
using namespace std;
double c,f,x;
double rate=2;
double curr,next,nextToreach;
int main()
{
	freopen ("out.out","w",stdout);
	freopen ("in.in","r",stdin);
	int t;
	scanf("%d",&t);
	for (int ca = 0; ca < t; ++ca)
	{
		cin>>c>>f>>x;
		rate=2;
		curr=x/rate;
		nextToreach=c/rate;
		next=c/rate;rate+=f;next+=x/rate;
		while(next<curr)
		{
			curr=next;
			nextToreach+=c/rate;
			next=nextToreach;rate+=f;next+=x/rate;
		}
		printf("Case #%d: %f\n",ca+1,curr);
	}
	return 0;
}
