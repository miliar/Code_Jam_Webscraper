#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(int argc, const char *argv[])
{
	string inputFileName = "A-small-attempt0.in";
	string outputFileName = "output.txt";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

	int test,i,j,k,m,temp,a;
	char array[5][5];
	char result;

	scanf("%d",&test);

	for(a=1;a<=test;a++)
	{
		for(k=0;k<4;k++)
		{
			scanf("%s",array[k]);
		}

		result='D';

		printf("Case #%d: ",a);

		for(k=0;k<4;k++)
			for(m=0;m<4;m++)
			{
				if(array[k][m]=='.')
				{
					result='C';
					break;
				}
			}

			temp=array[0][0];

			if((temp=='X')||(temp=='O')) {
				for(k=0;k<4;k++)
					if((array[k][k]!=temp)&&(array[k][k]!='T'))
					{
						temp='A';
						break;
					}

					if(temp==array[0][0])
						result=array[0][0];
			}


			temp=array[0][3];

			if((temp=='X')||(temp=='O')) {
				for(k=0;k<4;k++)
					if((array[k][3-k]!=temp)&&(array[k][3-k]!='T'))
					{
						temp='A';
						break;
					}

					if(temp==array[0][3])
						result=array[0][3];
			}

			for(k=0;k<4;k++)
			{
				for(m=0;m<4;m++)
				{
					if((array[k][m]=='X')||(array[k][m]=='T'))
					{
						temp=5;

					}
					else
					{
						temp=0;
						break;
					}
				}

				if(temp==5)
					result='X';
			}
			for(k=0;k<4;k++)
			{
				for(m=0;m<4;m++)
				{
					if((array[k][m]=='O')||(array[k][m]=='T'))
					{
						temp=6;
					}
					else
					{
						temp=0;
						break;
					}
				}


				if(temp==6)
					result='O';
			}

			for(k=0;k<4;k++)
			{
				for(m=0;m<4;m++)
				{
					if((array[m][k]=='X')||(array[m][k]=='T'))
					{
						temp=7;
					}
					else
					{
						temp=0;
						break;
					}
				}

				if(temp==7)
					result='X';
			}
			for(k=0;k<4;k++)
			{
				for(m=0;m<4;m++)
				{
					if((array[m][k]=='O')||(array[m][k]=='T'))
					{
						temp=8;

					}
					else
					{
						temp=0;
						break;
					}
				}


				if(temp==8)
					result='O';
			}
			if((result=='X')||(result=='O'))
			{
				printf("%c won\n",result);
			}

			else if(result=='C')
			{
				printf("Game has not completed\n");
			}

			else if(result=='D')
			{
				printf("Draw\n");
			}
			printf("\n");

	}
}
