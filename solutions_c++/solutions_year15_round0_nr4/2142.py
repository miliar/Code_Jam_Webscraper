#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <math.h>

using namespace std;

int main()
{
    int T,X,R,C;
    int i,j,x;

    cin >> T;
    
    for (x=0;x<T;x++)
    {

	cin >> X;
	cin >> R;
	cin >> C;

	if (X>R && X>C)
       		printf("Case #%d: RICHARD\n",x+1);
	else if (((R*C)%X)!=0)
       		printf("Case #%d: RICHARD\n",x+1);
	else if (X==1 || X==2 || X==3)
	{
		if (X==3 && (C==1 || R==1))	
       			printf("Case #%d: RICHARD\n",x+1);
		else
       			printf("Case #%d: GABRIEL\n",x+1);
	}
	else if (X==4)
	{
		if (R==1 || C==1 || R==2 || C==2)
       			printf("Case #%d: RICHARD\n",x+1);
		else
       			printf("Case #%d: GABRIEL\n",x+1);
			
	}
		
    }
}
