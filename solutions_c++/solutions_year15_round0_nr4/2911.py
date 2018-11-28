#include <stdio.h>
int main(void) {
	//freopen("D-small-attempt4.in","r",stdin);
	//freopen("D-small-attempt4.out","w",stdout);
	int tc,t,X,R,C;
	char win;
	scanf("%d",&tc);
	for(t=1;t<=tc;t++)
	{
	    scanf("%d%d%d",&X,&R,&C);
	    switch(X)
	    {
	        case 1:
	                win='g';break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    win='r';
	                else
	                    win='g';break;
	        case 3:
	                if(R==1||C==1)
	                    win='r';
	                else if(R==3||C==3)
	                    win='g';
	                else
	                    win='r';break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    win='g';
	                else 
	                    win='r';
	    }
	    if(win=='g')
	        printf("Case #%d:GABRIEL\n",t);
	    else
	        printf("Case #%d:RICHARD\n",t);
	}
	return 0;
}


