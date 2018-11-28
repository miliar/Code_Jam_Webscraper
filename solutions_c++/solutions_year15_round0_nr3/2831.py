#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <string>
#include <math.h>


using namespace std;
int M[5][5]={{0,0,0,0,0},
	     {0,1,2,3,4},
	     {0,2,-1,4,-3},
	     {0,3,-4,-1,2},
	     {0,4,3,-2,-1}};

int main()
{

        int T;
        int t;
        freopen( "input.txt", "r", stdin );
        freopen( "output.txt", "w", stdout );
	cin >> T;

	for(int t=1;t<=T;t++)
	{
		int L,X;		
		cin >> L >> X;
		char *str = (char *)malloc(sizeof(X));
		for(int x=0;x<L;x++)
		{
			cin >> str[x];
		} 
		if(L*X <=2)
		{
			printf("Case #%d: NO\n",t);
			continue;
	
		}
//		char *str = (char *)malloc(sizeof(str));
//		for(int x=0;x<L*X;x=x+L)
//		{
//			strncpy(str+x,a,L);
//		}
		int temp=0;
		temp = str[0]-'i' + 2;
			
		int index=1;
		while(temp!=2 && index < L*X )	
		{
				
			if(temp < 0)
			{
			temp = -M[abs(temp)][str[index%L]-'i'+2];
			}
			else
			{
			temp = M[temp][str[index%L]-'i'+2];
			}
			index++;	
			
		}

		if(index >= L*X || temp!=2)
		{

			printf("Case #%d: NO\n",t);
			continue;

		}
		temp = str[index%L]-'i' + 2;
		index++;
		while(temp!=3 && index < L*X )	
		{
			
			if(temp < 0)
			{
			temp = -M[abs(temp)][str[index%L]-'i'+2];
			}
			else
			{
			temp = M[temp][str[index%L]-'i'+2];
			}
			index++;	
			
		}

		if(index >= L*X || temp!=3)
		{

			printf("Case #%d: NO\n",t);
			continue;

		}
	

		temp = str[index%L]-'i' + 2;
		index++;

		while(temp!=4 || index < L*X )	
		{
			
			if(temp < 0)
			{
			temp = -M[abs(temp)][str[index%L]-'i'+2];
			}
			else
			{
			temp = M[temp][str[index%L]-'i'+2];
			}
			index++;	
			
		}
		
		if(index == L*X && temp==4)
		{

			printf("Case #%d: YES\n",t);
		//	continue;

		}
		else
		{
			printf("Case #%d: NO\n",t);
//			continue;


		}
		

		
		
	}	
	return 0;
}

