#include "stdafx.h"

#include <iostream>

using namespace std;

char stack[100+1];
int Answer=0;

int main(int argc, char * argv[])
{


	freopen("sample.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	
	cin>>T;
	for(int testcase =1;testcase<=T;testcase++)
	{
		int N;
		
		cin>>stack;
		Answer=0;
		
		while(1)
		{
			int limitPoint =0;
			for(int i=0;i<strlen(stack);i++)
			{
				if(stack[i]!=stack[0])
				{
					limitPoint=i;
					break;
				}
			}
			
			if((limitPoint==0 && stack[0] =='-'))
			{
				limitPoint =strlen(stack);
			}

			if((limitPoint==0 && stack[0] =='+') /*|| (limitPoint == strlen(stack) && stack[0]=='+' )*/)
			{
				break;
			}
			else
			{
				for(int i=0;i<limitPoint;i++)
				{
					if(stack[i]=='-')
					{
						stack[i] ='+';
					}
					else
					{
						stack[i] ='-';
					}
				}
				Answer++;
			}
			
		}

		cout<<"Case #"<<testcase<<": ";
		cout<<Answer<<endl;
	}

	return 1;
}