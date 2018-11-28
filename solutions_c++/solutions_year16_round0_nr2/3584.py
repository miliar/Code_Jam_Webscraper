//#include<iostream>
#include<algorithm>
#include<math.h>
#include<cstdio>
#include<cstring>
#include<set>

using namespace std;

int solve()
{
	char txt[205];
	int ans=0;
	scanf("%s", txt);
	int dl = strlen(txt);
	char last = '$';
	for( int i=0; i<dl; ++i)
	{
		if(txt[i]=='-' and last == '+')
			ans+=2;
		if(txt[i] == '-' and last == '$')
			ans+=1;
		last= txt[i];
	}
	return ans;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int test =1; test <= t; ++test)
	{
		printf("Case #%d: %d\n", test, solve());
	}
	return 0;
}
