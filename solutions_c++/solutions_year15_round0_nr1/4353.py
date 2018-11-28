/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
* Author : Prasad J Ghangal					*
* Title : Codejam- Standing Ovation				*
* Algorithm : 							*
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

#include <stdio.h>
#include <iostream>
#define gc getchar_unlocked
using namespace std;
int fin()
{
	char c=gc();
	int res=0;
	while(c<'0' || c>'9')
		c=gc();
	while(c>='0' && c<='9')
	{
		res=res*10+(c-48);
		c=gc();
	}
	return res;
}

int main()
{
	int t,n,cnt,l,i,tot,tc=0;
	char a[1005];
	t=fin();
	while(t--)
	{
		tc++;
		cnt=tot=0;
		n=fin();
		n+=1;
		scanf("%s",a);
		for(i=0;i<n+1;i++)
		{
			if(i<=tot)
			{
				tot=tot+(a[i]-48);	
			}
			else
			{
				cnt+=(i-tot);
				tot+=((a[i]-48)+(i-tot));
			}

		}
		printf("Case #%d: %d\n",tc,cnt);
	}
	return 0;
}
