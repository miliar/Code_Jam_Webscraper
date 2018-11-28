#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;
bool stat[10];
bool judge()
{
	for(int i=0;i<10;i++)
		if(!stat[i])	return false;
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,N;
	scanf("%d",&T);	
	for(int i=0;i<T;i++)
	{
		if(i>0)	printf("\n");
		memset(stat,0,sizeof(stat));
		scanf("%d",&N);
		if( N==0 )		printf("Case #%d: INSOMNIA",i+1);
		else
		{
			int current = 0;
			while(!judge())
			{
				current += N;
				int m = current,digit = current%10;
				while(m>0)
				{
					stat[digit] = true;
					m = m/10;
					digit = m%10;
				}
			}
			printf("Case #%d: %d",i+1,current);
		}
	}
} 
