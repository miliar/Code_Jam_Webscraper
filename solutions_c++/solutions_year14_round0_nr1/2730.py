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

int r1[20], r2[20], ans1, ans2;
void solve(int test)
{
	cin>>ans1;
	for (int i=1; i<=4; i++)
		for (int j=1; j<=4; j++)
		{
			int x; 
			cin>>x;
			r1[x]=i;
		}
	cin>>ans2;
	for (int i=1; i<=4; i++)
		for (int j=1; j<=4; j++)
		{
			int x; 
			cin>>x;
			r2[x]=i;
		}	
	int ans=-1, u=0;
	for (int i=1; i<=16; i++)
		if ( r1[i]==ans1 && r2[i]==ans2 )
			ans=i, u++;
	printf("Case #%d: ", test);
	if ( u==1 )
		printf("%d", ans);
	else
		if (u>1)
			printf("Bad magician!");
		else
			printf("Volunteer cheated!");
	printf("\n");
}
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int test;
	cin>>test;
	for (int i=1; i<=test; i++)
		solve(i);
	return 0;
}
