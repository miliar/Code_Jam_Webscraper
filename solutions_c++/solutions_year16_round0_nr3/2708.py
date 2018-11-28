/* ***********************************************
Author        :yzkAccepted
Created Time  :2016/4/9 23:50:51
TASK		  :。.cpp
LANG          :C++
************************************************ */

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stack>
using namespace std;
typedef __int64 ll;
ll ans[55]={32769,32773,32775,32777,32781,32787,32793,32795,32799,32805,32811,32815,32817,32821,32823,32827,32829,32835,32841,32847,32853,32855,32857,32859,32861,32863,32865,32867,32871,32875,32877,32883,32885,32889,32891,32893,32895,32899,32901,32905,32913,32919,32921,32923,32925,32931,32935,32937,32947,32949};
ll check(ll k)
{
	ll i;
	for(i=2;i<sqrt(k);i++)
	{
		if(k%i==0)
			return i;
	}
	return 1;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j;
	ll res,st,w;
	int aa,bb,cc;
	scanf("%d%d%d",&aa,&bb,&cc);
	printf("Case #1:\n");
	for(i=0;i<50;i++)
	{
		res=0;
		st=1;
		for(j=0;j<16;j++)
		{
			if(((1<<j)&ans[i])==(1<<j))
			{	
				res+=st;
			}
			st=st*10;
		}
		printf("%I64d ",res);

		
		ll ks;
		for(w=2;w<=10;w++)
		{
			res=0;
			st=1;
			for(j=0;j<16;j++)
			{
				if(((1<<j)&ans[i])==(1<<j))
				{	
					res+=st;
				}
				st=st*w;
			}
			ks=check(res);
			printf("%I64d ",ks);
		}
		printf("\n");
	}
    return 0;
}
