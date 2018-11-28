#include <iostream>
#include<stdio.h>

using namespace std;
char input[20],data[1000][20];
bool G=false;

bool is_Row(int n)
{
	if(n%4 <=1)
	{
		if(input[n+1]==input[n])
		{
			if(input[n+2]==input[n]&&(n+3)%4>2)
			{
				if(input[n+3] == input[n] || input[n+3]=='T' && (n+3)%4>1) 
				{
					//printf("%d row true",n);
					return true;
				}
			}
		}
	}
	return false;
}

bool is_Column(int n)
{
	if(n <= 7)
		if(input[n+4] == input[n])
		{
			if(input[n+8] == input[n])
			{
				if(input[n+12] == input[n] ||input[n+12] =='T')
				{
				//printf("%d column true",n);
					return true;
				}
			}
		}
		return false;
}
bool is_Diagonal()
{

	if(data[0][0]==data[1][1]==data[2][2]==data[3][3] || data[0][3]==data[1][2]==data[2][1]==data[3][0])
		return true;
}
bool is_Diagonal(int n)
{
	
	if(n%4 >2)
	{
		if(input[n+3] == input[n])
		{
			if(input[n+6] == input[n])
			{
				if(input[n+9]==input[n] ||input[n+9] =='T')
				{
						//printf("%d diagonal true",n);
					return true;
				}
			}
		}
	}
	else if(n%4 <2)
	{
		if(input[n+5] == input[n])
		{
			if(input[n+10] == input[n])
			{				
				if(input[n+15]==input[n] ||input[n+15]=='T')
				{
					{
						//printf("%d diagonal true1",n);
					return true;
					}
				}
			}
		}
		
	}
	return false;
}


void main()
{
	int i=0;
	int case_no= 0;
	int index=0;
	char winner;
	freopen ("d:/A-small-attempt1.in","r",stdin);
    freopen ("d:/A-small-attempt1.out","w",stdout);
	cin>>case_no;

	for( int x=1; x<=case_no ;x++)
	{
	for( i=0;i<=3;i++)
		for(int j=0;j<=3;j++)
		{
			cin>>data[i][j];
			input[index++]=data[i][j];
		}
		winner='.';
		index=0;
		G=false;
		//is_Tavailable();
		//for(int k=0;k<strlen(input);k++) printf("input[%d]= %c\n",k,input[k]);
		//printf("%s\n",input);
		printf("Case #%d: ",x);
		//if()
		//is_Diagonal();
	for( i=0; i<strlen(input);i++)
		//for(int j=0; j<=3 ;j++)
		{
			if(input[i]=='X' || input[i]=='O')
			{
				if( is_Diagonal(i)|| is_Row(i)|| is_Column(i))
				{
				printf("%c won\n",input[i]);
				winner=input[i];
				break;
				}
			}
			else if (input[i] == '.')
				G=true;
		}
	
	//if(for(int y=0;input[y];y++)if (input[strlen(input)-1]=='.'||input[strlen(input)-1]=='T') && winner=='.') printf("Game has not completed\n");
		if (G == true && winner=='.') printf("Game has not completed\n");	
		else if(G==false && i== strlen(input) && winner=='.') printf("Draw\n");
	}//case ended
}