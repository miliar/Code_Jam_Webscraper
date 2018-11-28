#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
	int t,x,r,c,ind=0,flag;
	scanf("%d",&t);
	while(t--)
	{
		ind++;
		scanf("%d%d%d",&x,&r,&c);
		if(r<c)
		{
			swap(r,c);
		}
		flag=0;
		switch(x)
		{
			case 1:	flag=1;
					break;
			case 2:	if((r*c)%2==0)	flag=1;
					break;
			case 3: if((r*c)%3==0)
                    if(r>=3)
					{
						if(c>=2)
						{
							flag=1;
						}
					}
					break;
			case 4: if((r*c)%4==0)
                    if(r>=4)
					{
						if(c>=3)	flag=1;
					}
					break;
            case 5: if((r*c)%5==0)
                    {
                        if(r>=5 && c>=5)    flag=1;
                    }
            case 6: if((r*c)%6==0)
                    {
                        if(r>=6 && c>=6)    flag=1;
                    }
		}
		printf("Case #%d: %s\n",ind,(flag==1)?"GABRIEL":"RICHARD");
	}
	return 0;
}

