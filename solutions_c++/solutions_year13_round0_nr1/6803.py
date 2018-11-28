#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
	FILE* input;
	FILE* output;
	
	input = fopen("A-large.in","r");
	output = fopen("A-large.out","w");
	int t;
	fscanf(input,"%d",&t);
	char data[4][5]; 
	for(int i = 1;i <= t;i++)
	{
		for(int j = 0;j != 4;j++)
			fscanf(input,"%s",data[j]);
		int data1,data2;
		bool draw = true;
		bool flag = false;
		for(int j = 0;j != 4;j++)
		{
			data1 = 0;
			data2 = 0;
			for(int k = 0;k != 4;k++)
			{
				if(data[j][k] == 'X')
					data1 ++;
				else if(data[j][k] == 'O')
					data2 ++;
				else if(data[j][k] == 'T')
				{
					data1 ++;
					data2 ++;
				}
				else
				draw = false;
			}
			if(data1 == 4)
			{
				fprintf(output,"Case #%d: X won\n",i);
				flag = true;
				break;
			}
			if(data2 == 4)
			{
				fprintf(output,"Case #%d: O won\n",i);
				flag = true;
				break;
			}
		}
		if(flag)
		continue;
		for(int j = 0;j != 4;j++)
		{
			data1 = 0;
			data2 = 0;
			for(int k = 0;k != 4;k++)
			{
				if(data[k][j] == 'X')
					data1 ++;
				else if(data[k][j] == 'O')
					data2 ++;
				else if(data[k][j] == 'T')
				{
					data1 ++;
					data2 ++;
				}
				else
				draw = false;
			}
			if(data1 == 4)
			{
				fprintf(output,"Case #%d: X won\n",i);
				flag = true;
				break;
			}
			if(data2 == 4)
			{
				fprintf(output,"Case #%d: O won\n",i);
				flag = true;
				break;
			}
		}
		if(flag)
		continue;
		data1 = 0;
		data2 = 0;
		for(int j = 0;j != 4;j++)
		{
			if(data[j][j] == 'X')
				data1 ++;
			else if(data[j][j] == 'O')
				data2 ++;
			else if(data[j][j] == 'T')
			{
				data1 ++;
				data2 ++;
			}
			else
				draw = false;
		}
		if(data1 == 4)
		{
			fprintf(output,"Case #%d: X won\n",i);
			flag = true;
			continue;
		}
		if(data2 == 4)
		{
			fprintf(output,"Case #%d: O won\n",i);
			flag = true;
			continue;
		}
		data1 = 0;
		data2 = 0;
		for(int j = 0;j != 4;j++)
		{	
			if(data[3-j][j] == 'X')
				data1 ++;
			else if(data[3-j][j] == 'O')
				data2 ++;
			else if(data[3-j][j] == 'T')
			{
				data1 ++;
				data2 ++;
			}
			else
				draw = false;
		}
		if(data1 == 4)
		{
			fprintf(output,"Case #%d: X won\n",i);
			flag = true;
			continue;
		}
		if(data2 == 4)
		{
			fprintf(output,"Case #%d: O won\n",i);
			flag = true;
			continue;
		}
		if(draw)
			fprintf(output,"Case #%d: Draw\n",i);
		else
			fprintf(output,"Case #%d: Game has not completed\n",i);
	}
	return 0;
}
