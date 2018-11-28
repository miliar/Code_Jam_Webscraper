#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<cstdlib>
#include<fstream>
#include<ctime>
#include<string>
using namespace std;
#define ll long long
#define mxn 100010
#define mxe 200010
#define inf 0x3f3f3f3f
#define mp make_pair
#define pii pair<int,int>

char s[1010];
int a[1010];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("google.out","w",stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int sm;
		scanf("%d %s",&sm,s);
		int sum=0,cnt=0;
		for(int i=0;i<=sm;i++)
		{
			if(sum<i)
			{
				cnt+=(i-sum);
				sum=i;
			}
			int k=s[i]-'0';
			sum+=k;
		}
		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}









		


				





						




