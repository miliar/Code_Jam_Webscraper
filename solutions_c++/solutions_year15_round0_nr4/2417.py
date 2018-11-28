#include<bits/stdc++.h>
using namespace std;
int main()
{
	int tc,x,r,c,k;
	scanf("%d",&tc);
	for(k=1;k<=tc;k++)
	{
		scanf("%d%d%d",&x,&r,&c);
		switch(x)
		{
			case 1:
				printf("Case #%d: GABRIEL\n",k);
				break;
			case 2:
				if((r*c)%2==0)
					printf("Case #%d: GABRIEL\n",k);
				else
					printf("Case #%d: RICHARD\n",k);
				break;
			case 3:
					if(r==3||c==3)
					{
						if(r==1||c==1)
							printf("Case #%d: RICHARD\n",k);
						else
							printf("Case #%d: GABRIEL\n",k);
					}
					else
						printf("Case #%d: RICHARD\n",k);
				break;
			case 4:
				if(r==4&&c==4)
					printf("Case #%d: GABRIEL\n",k);
				else if((r==4&&c==3)||(r==3&&c==4))
					printf("Case #%d: GABRIEL\n",k);
				else
					printf("Case #%d: RICHARD\n",k);
			  	break;
		}

	}
	return 0;
}