//sums in a triangle
#include<iostream>
#include<cstdio>
#include<algorithm>
#include <fstream>
using namespace std;


int main()
{
	FILE *in_file  = fopen("A-small-attempt2.in", "r"); // read only 
    FILE *out_file = fopen("magic_ouput.txt", "w"); // write only 
    int t = 0,counter = 1;
    fscanf(in_file,"%d",&t);
    while(t--)
    {
    	int a[4][4]={0}, b[4][4]={0}, flag = 0, output = 0, first_match = 0,second_match=0;
        fscanf(in_file,"%d",&first_match);
        for(int i=0;i<4;i++)
        	for(int j=0;j<4;j++)
				fscanf(in_file,"%d",&a[i][j]);
		fscanf(in_file,"%d",&second_match);
        for(int i=0;i<4;i++)
        	for(int j=0;j<4;j++)
				fscanf(in_file,"%d",&b[i][j]);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[first_match-1][i] == b[second_match-1][j])
				{
					flag = flag + 1;
					output = a[first_match-1][i];
				}
			}
		}
		if(flag == 1)
		{
			fprintf(out_file,"Case #%d: %d\n",counter,output);
		}
		else
		{
			if(flag == 0)
			{
				fprintf(out_file,"Case #%d: Volunteer cheated!\n",counter);		
			}
			else
				fprintf(out_file,"Case #%d: Bad magician!\n",counter);
		}
		counter++;
	}    	
 		return 0;   
}
