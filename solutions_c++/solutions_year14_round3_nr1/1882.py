// A_Part_Elf.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int main(int argc, char* argv[])
{
	FILE *IN1, *OUT1;
	double p,q,temp;
	int n;
	int count;
	bool flag,flag_1,flag_2;
	int ii,i;
	
	IN1 = fopen ("A-small-attempt0.in" , "rb");
	OUT1 = fopen ("A-small-attempt0.out" , "wb");
    
	fscanf(IN1,"%d",&n);
	for(ii=1;ii<=n;ii++)
	{
		flag = false;
		fscanf(IN1,"%lf/%lf",&p,&q);
		temp = p;
		for(count = 0;count > -1;)
		{
			count++;
			temp = temp * 2;
			if(temp>=q)
			{
				if(q/p == (int)(q/p))
					q = q/p;
				else{}

				for(i=0;i>-1;i++)
				{
					q=q/2;
					if(q==1)
						flag = true;
					else if(q < 1)
						break;
				}
			}
			if(flag == true)
				break;
			else if(count>100)
				break;
		}
		if(flag == false)
			fprintf(OUT1,"Case #%d: impossible\r\n",ii);
		else
			fprintf(OUT1,"Case #%d: %d\r\n",ii,count);
	}


	return 0;
}
/*
if(temp%2 == 0)
				temp = temp/2;
			else if(temp == 1)
				break;
			else
			{
				flag = true;
				break;
			}
			*/
/*			for(count=0;count>-1;count++)
			{
				if(temp%2 == 0)
					temp = temp/2;
				else if(temp == 1)
					break;
				else
				{
					flag = true;
					break;
				}
			}*/