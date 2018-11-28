#include <vector>
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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
#define tr(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define all(c) c.begin(),c.end()
#define mod 1000000007
#define itor(c) typeof(c.begin())
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define si set<int>
#define msi multiset<int>
#define sp set<pair<int,int> >
#define vp vector<pair<int,int> >
#define pb push_back
#define mp make_pair

using namespace std;
int main()
{
	vector<double> a1, b1; 
	int t, i, k, n, res1, res2, p, q, x, y,test;
	scanf("%d", &t);
	double temp;
	for(test=1; test<=t; test++)
	{
		res1=res2=0;
		scanf("%d", &n);
		for(i=0; i<n; i++)
		{
			scanf("%lf", &temp);
			a1.push_back(temp);
			
		}
		for(i=0; i<n; i++)
		{
			scanf("%lf", &temp);
			
			b1.push_back(temp);
		}
		sort(a1.begin(), a1.end());
		sort(b1.begin(), b1.end());
		
		          p=q=n-1;
		for(i=0; i<n; i++)
		{
			if(a1[p] > b1[q])
			{
				p--;	
				q--;
				res1++;
			}
			else
				q--;
		}
 
		p=q=n-1;
		for(i=0; i<n; i++)
		{
			if(a1[p] > b1[q])
			{
				p--;
				res2++;
			}
			else
			{
				p--;
				q--;
			}
		}
 
		printf("Case #%d: %d %d\n", test, res1, res2);
		a1.clear();
		b1.clear();
	}
	return 0;
}