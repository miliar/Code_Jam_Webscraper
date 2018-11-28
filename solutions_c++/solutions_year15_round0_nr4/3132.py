#include <stdio.h>
#include <iostream>
using namespace std;
int main() {

    freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	int tc,t,X,R,C;
	bool winner=true;
	scanf("%d",&tc);
	for(t=1;t<=tc;t++)
	{
	    scanf("%d%d%d",&X,&R,&C);
	    switch(X)
	    {
	        case 1:
	                winner=true;
	                break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    winner=false;
	                else
	                    winner=true;
	                    break;
	        case 3:
	                if(R==1||C==1)
	                    winner=false;
	                else if(R==3||C==3)
	                    winner=true;
	                else
	                    winner=false;
	                    break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    winner=true;
	                else
	                    winner=false;
	    }
	    if(winner==true)
	        printf("Case #%d: GABRIEL\n",t);
	    else
	        printf("Case #%d: RICHARD\n",t);
	}
	return 0;
}
