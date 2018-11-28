//Author: sagarkaniche
#include <bits/stdc++.h>
#define ll long long
using namespace std;
#define si(x) scanf("%d",&x)
#define sdb(x) scanf("%lf",&x)
#define sll(x) scanf("%lld",&x)
#define pb push_back
#define res 1000000007
typedef pair<int,int> pp;


int main()
{
	int t,cnt=1;
	si(t);
	while(t--)
	{
		int k,c,s;
		si(k);si(c);si(s);
		printf("Case #%d: ",cnt++);
		for(int i=0;i<k;i++) printf("%d ",i+1);
		printf("\n");
	}
	return 0;
}