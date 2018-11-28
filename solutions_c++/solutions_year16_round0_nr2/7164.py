#include<iostream>
#include<conio.h>
#include<stdio.h>
#include<fstream>

using namespace std;

void TopFlipPos(int);
void TopFlipNeg(int);
void Flip(int);
int County(char,int);
char S[100][102];

int main()
{
	int T,Step[100],NO_POS=0,NO_NEG=0;
	fstream fin,fout;
	fin.open("Large.in",ios::in);
	fout.open("OutLarge.txt",ios::out);
   
    fin>>T;
	for(int i=0;i<T;i++)
	{
		fin>>S[i];
	}
	
    for(int i=0;i<T;i++)
	{
        //int NO_POS=County('+',i);
	    //int NO_NEG=County('-',i);
        Step[i]=0;    
		for(int j=0;j<strlen(S[i]);j++)
		{	
			//if(j==0&&S[i][j]=='-')
			//	{
					//if(NO_POS<NO_NEG)
					//{
					//	Flip(i);
					//	Step[i]++;
					//}
			//	}
			again:
            int Con=County('-',i);
            if(S[i][j]=='-')
			{
					TopFlipNeg(i);
					Step[i]++;
					j=0;
					goto again;
			}
			else if(Con)
			{
					TopFlipPos(i);
					Step[i]++;
					j=0;
					goto again;
			}
			
		}
	}
	for(int i=0;i<T;i++)
	{
		fout<<"Case #"<<i+1<<": "<<Step[i]<<endl;
	}
	fin.close();
	fout.close();
    return 0;
}

void TopFlipPos(int k)
{
	int Prev=1;
	for(int i=0;i<strlen(S[k]);i++)
	{
		if(S[k][i]=='+'&&Prev==1)
		{
			Prev=1;
			S[k][i]='-';
		}
		else
		    Prev=0;
	}
}

void TopFlipNeg(int k)
{
	int Prev=1;
	for(int i=0;i<strlen(S[k]);i++)
	{
		if(S[k][i]=='-'&&Prev==1)
		{
			Prev=1;
			S[k][i]='+';
		}
		else
		    Prev=0;
	}
}

void Flip(int k)
{
	for(int i=0;i<strlen(S[k]);i++)
	{
		if(S[k][i]=='-')
			S[k][i]='+';
		else if(S[k][i]=='+')
			S[k][i]='-';	
		
	}
}

int County(char sign,int k)
{
   int no=0,len;
   for(len=0;S[k][len]!='\0';len++)
           continue;
   for(int j=0;j<len;j++)
     {
        if(S[k][j]==sign)
				no++;
		}
  return no;
}
