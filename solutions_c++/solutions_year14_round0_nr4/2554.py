#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string.h>
#include <string>
#include <string>
#include <set>
#include <map>


using namespace std;

vector<double>a, b;
int n;
bool was[1010];
void solve(int test)
{
	a.clear();
	b.clear();
	memset(was, 0, sizeof(was));
	cin>>n;
	for (int i=1; i<=n; i++)
	{
		double x;
		cin>>x;
		a.push_back(x);
	}
	for (int i=1; i<=n; i++)
	{
		double x;
		cin>>x;
		b.push_back(x);
	}
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());	
	int ans1=0, ans2=0;
	for (int i=0; i<n; i++)
	{
		int f=(1<<20);
		bool ok=0;
		for (int j=0; j<n; j++)
			if ( was[j]==0  )
			{
				f=min(f, j);
				if ( b[j]>a[i] )
				{
					ok=1; was[j]=1; 
					break;
				}
			}
		if ( ok==0 ) ans1++, was[f]=1;
	}
	int l=0, r=n-1;
	for (int i=0; i<a.size(); i++)
	{
		if ( a[i]>b[l] ) ans2++, l++;
		else
			r--;
	}
	printf("Case #%d: %d %d\n", test, ans2, ans1);
}
int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int test;
	cin>>test;
	for (int i=1; i<=test; i++)
		solve(i);
	return 0;
}
