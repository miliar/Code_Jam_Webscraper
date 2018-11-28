#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;
#define clear(a) memset((a),0,sizeof(a))
#define pb push_back
#define SIZE(v) v.size()
#define ull unsigned long long int
#define lli long long int
#define li long int
#define ii int
#define mod 1000000007
/* Created by : Rahul Johari
				Thapar University */
				
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small.txt","w",stdout);
	
	ii t,cse,x,r,c,flag;
	
	scanf("%d",&t);
	for ( cse=1;cse<=t;cse++ )
	{
		scanf("%d %d %d",&x,&r,&c);
		//if ( x==1 )
		//	printf("Case #%d: GABRIEL\n",cse);
		flag = 0;
		if ( x>8)
			flag = 1;		
		if ( r%x!=0 && c%x!=0 )
			flag = 1;
		if ( (r<x-1) || (c<x-1) )
			flag = 1;
		
		printf("Case #%d: ",cse);
		if ( flag==1 )
			printf("RICHARD\n");
		else 
			printf("GABRIEL\n");
	}	
	
    return 0;
}
