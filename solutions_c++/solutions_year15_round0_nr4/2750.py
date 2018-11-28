#include <stdio.h>

int main(void) {
	int round,win;
	scanf("%d",&round);
	for(int t=1;t<=round;t++)
	{
		int X,R,C;
		scanf("%d%d%d",&X,&R,&C);
		switch(X){
			case 1:
				win=0;
				break;
			case 2:
				if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
					win=1;
				else
					win=0;
				break;
			case 3:
				if(R==1||C==1)
					win=1;
				else if(R==3||C==3)
					win=0;
				else
					win=1;
				break;
			case 4:
				if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
					win=0;
				else
					win=1;
		}
		if(win==0)
			printf("Case #%d: GABRIEL\n",t);
		else
			printf("Case #%d: RICHARD\n",t);
	}
	return 0;
}
