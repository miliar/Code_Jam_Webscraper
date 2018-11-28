#include <bits/stdc++.h>
using namespace std;
int main() 
{
	int t,i,X,R,C;
	char sp;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
	    scanf("%d%d%d",&X,&R,&C);
	    switch(X)
	    {
	        case 1:
	                sp='g';break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    sp='r';
	                else
	                    sp='g';break;
	        case 3:
	                if(R==1||C==1)
	                    sp='r';
	                else if(R==3||C==3)
	                    sp='g';
	                else
	                    sp='r';break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    sp='g';
	                else 
	                    sp='r';
	    }
	    if(sp=='g')
	        printf("Case #%d: GABRIEL\n",i);
	    else
	        printf("Case #%d: RICHARD\n",i);
	}
}

