#include <cstdio>
#include<iostream>
using namespace std; 
int main() {
		freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int test,i,X,R,C,w;
	scanf("%d",&test);
	for(i=0;i<test;i++)
	{
	    scanf("%d%d%d",&X,&R,&C);
	    switch(X)
	    {
	        case 1:
	                w=1;break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    w=2;
	                else
	                    w=1;break;
	        case 3:
	                if(R==1||C==1)
	                    w=2;
	                else if(R==3||C==3)
	                    w=1;
	                else
	                    w=2;break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    w=1;
	                else 
	                    w=2;
	    }
	    if(w==1)
	        printf("Case #%d: GABRIEL\n",i+1);
	    else
	        printf("Case #%d: RICHARD\n",i+1);
	}
	return 0;
}


