#include<iostream>
#include<vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string>
#include <queue>
#include <sstream>
#include <iostream>
#include<string.h>
#include <iomanip>
#include <cstdio>
#include<math.h>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define ull unsigned long long 
#define pi 3.141592653589793
#define ARRAY_SIZE(A) sizeof(A)/sizeof(A[0])
#define PB push_back
#define INF 1<<30
using namespace std;
int main()
{
	int cases =0;
	cin>>cases;int tt =1;
	while(cases--)
	{
		double t =2;
		double c,f,x;
		double ans =0;
		cin>>c>>f>>x;
		if(c>=x)
		{
			ans =x/2;
		}
		else
		{
			while((x/(t+f))+(c/t)<(x/t))
			{
				ans += c/t;
				t =t+f;
			}
			ans+=(x/t);
		}
		cout<<"Case #"<<tt++<<": ";
		printf("%.7f\n",ans);
	}
	return 0;
}