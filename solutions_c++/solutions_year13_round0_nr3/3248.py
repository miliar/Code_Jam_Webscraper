#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int r[1001] = {0};
	r[1] = 1;
	r[4] = 1;
	r[9] = 1;
	r[121] = 1;
	r[484] = 1;
	int t;
	cin >> t;
	for(int x=0;x<t;x++)
	{
		int a,b;
		cin >> a >> b;
		int cnt = 0;
		for(int i=a;i<=b;i++)
			cnt+=r[i];
		printf("Case #%d: %d\n",x+1,cnt);
	}
	return 0;	
}
