// g.cpp : Defines the entry point for the console application.
//

#include "StdAfx.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <stdlib.h>
using namespace std;
int ncase;
int main()
{
		freopen("file.in", "r", stdin);
		freopen("file.out", "w", stdout);
		cin>>ncase;
		int x,r,c;
		
		for(int i=1;i<=ncase;i++)
	{		
		bool richard=false;
		scanf("%d %d %d",&x,&r,&c);
		if(x==1){
			richard=false;
		}
		else if(x==2){
			if((r*c)%2==0)
				richard=false;
			else
				richard=true;
		}
		else if(x==3){
			if((r==1 && c==3)||(r==3 && c==1))
				richard=true;
			else if((r*c)%3==0)
				richard=false;
			else
				richard=true;
		}
		else{
			if((r==1 && c==4)||(r==4 && c==1))
				richard=true;
			else if(r==2 && c==2)
				richard=true;
			else if((r==2 && c==4)||(r==4 && c==2))
				richard=true;
			else if((r*c)%4==0)
				richard=false;
			else
				richard=true;
		}

	if(richard)
			printf("Case #%d: RICHARD\n",i);
		else
			printf("Case #%d: GABRIEL\n",i);


	}
}

