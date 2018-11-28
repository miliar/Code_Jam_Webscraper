#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cstring>
using namespace std;
typedef long long ll;

int T;
ll A,B;
char s[10];
vector<int> d;

bool C(char c[10])
{
	int n = strlen(c);
	for (int i = 0; i <= n-i-1; i++)if (c[i]!=c[n-i-1]) return false;
	return true;
}

int main()
{
	for (int i = 1; i <= 40000; i++)
	{
		sprintf(s,"%d",i);
		if (!C(s)) continue;
		sprintf(s,"%d",i*i);
		if (!C(s)) continue;
		d.push_back(i*i);
	}
	scanf("%d",&T);
	for (int t = 1; t <= T; t++)
	{
		cin>>A>>B;
		printf("Case #%d: %d\n",t,upper_bound(d.begin(),d.end(),B)-lower_bound(d.begin(),d.end(),A));
	}
}