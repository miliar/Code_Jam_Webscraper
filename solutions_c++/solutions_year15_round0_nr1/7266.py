#include <iostream>
#include <cstdio>
#include <string.h>
#define max 10001
#define true 1
#define false 0

using namespace std;

int main(){

	
	int t, tc;
	FILE *input, *output;
	input = fopen("input.txt","r");
	output = fopen("output.txt","w");
	
	int shy_index;
	char shyness[max];
	int standing,needed;
	int shy_level;
	int i;
	
	fscanf(input, "%d", &t);
	
	for(tc=1; tc<=t; tc++)
	{
		int no;
		int temp_needed;
		
		fscanf(input,"%d",&shy_index);
		fscanf(input,"%s",shyness);
		
		standing =0 ;
		needed=0;
		
		for(i=0;i<=shy_index;i++)
		{
			shy_level=i;
			no=shyness[i]-'0';
			if(shy_level==0)
			{
				standing+=no;
			}
			else
			{
				if(shy_level > standing)
				{
					 temp_needed =  shy_level-standing;
					 needed+=temp_needed;
					 standing+=temp_needed;
					 standing+=no;
				}
				else
				{
					standing+=no;
				}
			}
		}
		
		fprintf(output,"Case #%d: %d\n",tc,needed);
	}
}
