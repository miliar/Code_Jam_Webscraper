#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string.h>
#include<map>
#include<cmath>
#include<iomanip>
#include<vector>
#include<queue>
using namespace std;
typedef long long LL;



int main(){
	freopen("1b2s.txt","r",stdin);
	freopen("outp.txt","w",stdout);
	int t,z;
	scanf("%d",&t);
	z=t;
	while(t--)
	{
		int a,b,k,cnt=0;
		scanf("%d %d %d",&a,&b,&k);
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n",z-t,cnt);
	}
    return 0;
}
