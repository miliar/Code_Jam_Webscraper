/*Code Developed By : Siddharth Sharma (B-Tech (C.S.E., IIIT-Delhi))*/

#include<bits/stdc++.h>
using namespace std;
#include <stdio.h>

int main(void) {
    freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);

	int t_cases,i,First,Second,Third;
	int yz = Third-Second;
	char ans;
	scanf("%d",&t_cases);
	for(i=1;i<=t_cases;i++)
	{
	    scanf("%d%d%d",&First,&Second,&Third);
	    switch(First)
	    {
	        case 1:
	                ans='g';break;
	        case 2:
	                if((Second==1&&Third==1)||(Second==1&&Third==3)||(Second==3&&Third==1)||(Second==3&&Third==3))
	                    ans='r';
	                else
	                    ans='g';break;
	        case 3:
	                if(Second==1||Third==1)
	                    ans='r';
	                else if(Second==3||Third==3)
	                    ans='g';
	                else
	                    ans='r';break;
	        case 4:
	                if((Second==4&&Third==4)||(Second==4&&Third==3)||(Second==3&&Third==4))
	                    ans='g';
	                else
	                    ans='r';
	    }

	    if(ans=='g')
	        printf("Case #%d: GABRIEL\n",i);
	    else
	        printf("Case #%d: RICHARD\n",i);
	}
	return 0;
}
