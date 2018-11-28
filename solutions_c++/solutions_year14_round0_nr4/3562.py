// Deceitful_War.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int main(int argc, char* argv[])
{
	int t,n;
	FILE *IN1, *OUT1;
	int i,j,k;
	int temp_addr;
	double a[1010],b[1010],temp;
	double c[2][1010];
	int count;
	bool end;
	int y,z;
	
	IN1 = fopen ("D-large.in" , "rb");
    OUT1 = fopen ("D-large.out" , "wb");
    fscanf(IN1,"%d",&t);
	for(i=0;i<t;i++)
	{
	    fscanf(IN1,"%d",&n);
		for(j=0;j<n;j++)
			fscanf(IN1,"%lf",&a[j]);
		for(j=0;j<n;j++)
			fscanf(IN1,"%lf",&b[j]);
		for(j=0;j<n;j++)
		{
			temp = a[j];
			temp_addr = 0;
			for(k=j+1;k<n;k++)
			{
				if(temp > a[k])
				{
					temp = a[k];
					temp_addr = k;
				}
			}
			if(temp_addr != 0)
			{
				a[temp_addr] = a[j];
				a[j] = temp;
			}
		}
		
		for(j=0;j<n;j++)
		{
			temp = b[j];
			temp_addr = 0;
			for(k=j+1;k<n;k++)
			{
				if(temp > b[k])
				{
					temp = b[k];
					temp_addr = k;
				}
			}
			if(temp_addr != 0)
			{
				b[temp_addr] = b[j];
				b[j] = temp;
			}
		}

		for(j=0;j<n;j++)
		{
			c[0][j] = a[j] ;
			c[1][j] = b[j] ;
		}
	

		count = 0;
		for(j=0;j<n;j++)
		{
			end = false;
			for(k=0;k<n;k++)
			{
				if(c[1][k] == -1)
					continue;
				else
					if(c[0][j] <c[1][k])
						break;
					else
					{
						count++;
						c[0][j] = -1;
						c[1][k] = -1;
						end = true;
					}
			}
			if(end == false)
				for(k=n-1;k>=0;k--)
					if(c[1][k] != -1)
					{
						c[0][j] = -1;
						c[1][k] = -1;
						break;
					}
		}
		y = count;

		for(j=0;j<n;j++)
		{
			c[0][j] = a[j] ;
			c[1][j] = b[j] ;
		}
		count = 0;
		for(j=n-1;j>=0;j--)
		{
			end = false;
			for(k=0;k<n;k++)
			{
				if( c[0][j] < c[1][k])
				{
					end = true;
					c[0][j] = -1;
					c[1][k] = -1;
					break;
				}
			}
			
			if(end == false)
			{
				for(k=0;k<n;k++)
					if(c[1][k] != -1)
					{
						count++;
						c[1][k] = -1;
						c[0][j] = -1;
						break;
					}
			}
		}
		z = count;
		fprintf(OUT1,"Case #%d: %d %d\r\n",i+1,y,z);
	}
	return 0;
}

