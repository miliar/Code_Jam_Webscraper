// The_Repeater.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "string.h"
#include "stdlib.h"


int main(int argc, char* argv[])
{
	FILE *IN1, *OUT1;
	char data[105][105];
	int t,n;
	int ii,i,j,k;
	int count;
	int temp_ans,ans,len,len1;
	bool flag;
	char temp_ch,temp_str[100],temp_str1[100];



	IN1 = fopen ("A-small-attempt0.in" , "rb");
	OUT1 = fopen ("A-small-attempt0.out" , "wb");

	fscanf(IN1,"%d",&t);
	for(ii=0;ii<t;ii++)
	{
		for(i=0;i<100;i++)
			for(j=0;j<100;j++)
				data[i][j] = 0;
		for(i=0;i<100;i++)
			temp_str[i] = 0;
		for(i=0;i<100;i++)
			temp_str1[i] = 0;
		
		ans = 0;
		flag = false;

		fscanf(IN1,"%d",&n);
		for(i=0;i<n;i++)
			fscanf(IN1,"%s",data[i]);
		
		for(i=0;i<n;i++)
		{
			temp_ch = data[i][0];
			count = 1;
			
			if(i==0)
				temp_str[0] = data[i][0];
			else
				temp_str1[0] = data[i][0];

			for(j=1;j<100;j++)
				if(temp_ch == data[i][j])
					continue;
				else if(data[i][j] == 0)
					break;
				else
				{
					if(i == 0)
						temp_str[count] = data[i][j];
					else
						temp_str1[count] = data[i][j];
					temp_ch = data[i][j];
					count++;
				}
			if(i==0)
				continue;
			else
			{
				if(strcmp(temp_str,temp_str1) == 0)
					continue;
				else
				{
					flag = true;
					break;
				}	
			}	
		}
//-----------------------------------------------------------------------------------
		len = strlen(temp_str);
		for(i=0;i<n;i++)
			ans = ans + abs(strlen(data[i]) - len);
		
		for(i=0;i<n;i++)
		{
			temp_ans = 0;
			for(j=0;j<n;j++)
			{
				len = strlen(data[i]);
				len1 = strlen(data[j]);
				count = 0;
				if(i==j)
					continue;
				else
					for(k=0,count=0; (k<len) || (count<len1); k++,count++)
					{
						if(data[i][k] == data[j][count])
							temp_ch = data[i][k];
						else if((data[i][k] != data[j][count]) && (data[i][k] == temp_ch))
						{
							count--;
							temp_ans++;
						}
						else if((data[i][k] != data[j][count]) && (data[j][count] == temp_ch))
						{
							k--;
							temp_ans++;
						}
//						else 
//							fprintf(OUT1,"error\r\n");
					}
			}
			if (ans > temp_ans)
				ans = temp_ans;

		}

//-----------------------------------------------------------------------------------

		if(flag == false)
			fprintf(OUT1,"Case #%d: %d\r\n",ii+1,ans);
		else 
			fprintf(OUT1,"Case #%d: Fegla Won\r\n",ii+1);

		
	}

	return 0;
}

