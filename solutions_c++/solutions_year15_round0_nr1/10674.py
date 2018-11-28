#include<iostream>
#include<stdlib.h>
#include<stdio.h>
//#include<math.h>
#include<cstdio>
#define gc getchar_unlocked

using namespace std;
template<class T>
void scanint(T &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
 
int main()
{
	int T,sk,count,i,j,sum,max;
	char s[1012];	
	scanint(T);
	for(i=0;i<T;i++)
	{
		count=0;
		scanint(sk);
		for(j=0;j<=sk;j++)
		{
			scanf("%c",&s[j]);
			//printf("%d",s[j]-48);
		}
		sum=0;
		for(j=1;j<=sk;j++)
		{
		//			scanint(s[j]);
			if(s[j-1]!='0')
			{
				
				count+=int(s[j-1])-48;
			}
			if(s[j]!='0')
			{
				if(count<j)
					{
						if(sum<j-count)
						sum=j-count;
						
			//			break;
					}
			}
		}
		printf("\nCase #%d: %d",i+1,sum);	
		
		
	}
	printf("\n");
return 0;
}
