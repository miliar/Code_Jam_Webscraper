/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
* Author : Prasad J Ghangal					*
* Title : Codejam-Omnious Omino					*
* Algorithm : AdHoc						*
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

#include <stdio.h>

int main()
{
	int t,x,r,c,tmp,tc=0;
	scanf("%d",&t);
	while(t--)
	{
		tc++;
		scanf("%d%d%d",&x,&c,&r);
		tmp=c*r;
		if(tmp%x==0)
		{
			if((c<=x/2 || r<=x/2))
			{
				if((x==2)&&(r==1 || c==1))
					printf("Case #%d: GABRIEL\n",tc);
				else
					printf("Case #%d: RICHARD\n",tc);
			}
			else
				printf("Case #%d: GABRIEL\n",tc);
		}
		else
		{
			printf("Case #%d: RICHARD\n",tc);
		}

	}
	return 0;
}
