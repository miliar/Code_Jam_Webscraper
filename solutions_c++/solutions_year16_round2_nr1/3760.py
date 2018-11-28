#include <stdio.h>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <limits.h>
#include <string.h>
#include <limits.h>

using namespace std;


int comp(const void *a, const void *b)
{
        return ( *(int*)a - *(int*)b );	// ascending order sort
    // return ( *(int*)b - *(int*)a );		// descending order sort
    
}

int main()
{
	int t=0;
	char * code[10]=
					{
						"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
					};
	scanf("%d",&t);
	for(int a=1;a<=t;a++)
	{
		int hash[100] = {0};
		bool found[10]= {false};
		char str[20001] ={0};
		int number[2000] ={0};
		int numCtr=0;
		bool complete = false;
		int x=0;
		scanf("%s",str);
		//cout<<str<<"\n";
		
		int len = strlen(str);
		
		for(int i=0;i<len;i++)
		{
			hash[str[i]]++;
		}
		
		for(int i=0;i<10;i++)
			found[i]=true;
			
		printf("Case #%d: ",a);
		for(int i=0;i<len && !complete ;i++)
		//while(!complete)
		{
		
			char * tmp;//=NULL;
			//printf("Loop: %d\n",i);
			
			int min = INT_MAX;
				for( int q='A'; q<='Z'; q++)
					if( hash[q] != 0 && min > hash[q] )
						min = hash[q];
			//cout << min<<"\n";
						
			for( int p='A';p<='Z';p++)
			{
						
				if ( hash[p] == min)
				{
					//printf("character: %c\n",p);
					for ( int a=0; a<=9 ; a++)
					{
					//	printf("Match: %s\n",code[a]);
						
						if( found[a])
						if (strchr(code[a],p) != NULL)
						{
							tmp = code[a];
							x=a;
							break;
						}
					}					
				}
			}
			
			//for(int x=9;x>=0  && !complete ;x--)
			{
			//char *tmp = code[x];
			char thash[100] = {0};
			bool flag = true;
			int digit=0;
			int j=0;
		
			for( int p='A';p<='Z';p++)
				thash[p]=hash[p];
			
	
		//	cout<<"tmp: "<<tmp<<"\n";
			while( tmp[j] != '\0')
			{
				
				if( thash[ tmp[j] ] <= 0)
				{
					flag = false;
					found[x]=false;
					break;
				}
				else
				{
					thash [tmp[j]]--;
				}
				j++;
			}
		
			if (flag == true)
			{
				//printf("found: %d",x);
				number[numCtr++]=x;
				
				//char *tmp = code[x];
				int j=0;
				while( tmp[j] != '\0')
					hash[tmp[j++]]--;
					
				
			}
			
			complete = true;
			for( int p='A';p<='Z';p++)
				if ( hash[p] != 0)
					complete = false;
					
					//complete = true;// for testing
			
			}//end of x
		}
			qsort(number,numCtr,sizeof(int),comp);
			for(int b=0;b<numCtr;b++)
				printf("%d",number[b]);
			printf("\n");		
	
	}
	return 0;
}
