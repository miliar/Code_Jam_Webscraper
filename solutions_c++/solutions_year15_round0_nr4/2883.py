#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<iostream>
using namespace std; 
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int t,i,X,R,C,win;
	scanf("%d",&t);
	for(i=0;i<20;i++)
	X=0;
	for(i=0;i<t;++i)
	{
	    scanf("%d%d%d",&X,&R,&C);
		int j=40;
	    switch(X)
	    {
	        case 1:
	                win=1;break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    win=2;
	                else
	                    win=1;break;
	        case 3:
	                if(R==1||C==1)
	                    win=2;
	                else if(R==3||C==3)
	                    win=1;
	                else
	                    win=2;break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    win=1;
	                else 
	                    win=2;
	    }
	    if(win==1)
	        printf("Case #%d: GABRIEL\n",i+1);
	    else
	        printf("Case #%d: RICHARD\n",i+1);
	
	}
	return 0;
}


