// magic.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;
ifstream in;
ofstream out;

int tests;
int row;
int row2;
int table[4][4];
int r1[4];
int r2[4];
int result=0;
int card;
int _case=1;

void displayTable()
    {
        for(int i=0; i<4; i++)
        {
            for(int j=0;j<4; j++)
            {
                cout<<table[i][j];
				cout<<" ";
            }
            cout<<endl;;
        }
    }

void final()
{
        result=0;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(r1[i]==r2[j])
                {
					cout<<r1[i]<< " == "<<r2[j]<<endl;
                    card=r1[i];
                    result++;
                }
            }
        }
        if(result==0)
        {
            cout<<"Volunteer cheated!";
			out<<"case #"<<_case<<": "<<"Volunteer cheated!"<<endl;
        }
        else if(result==1)
        {
            cout<<card;
			out<<"case #"<<_case<<": "<<card<<endl;
        }
        else if(result>1)
        {
            cout<<"Bad magician!";
			out<<"case #"<<_case<<": "<<"Bad magician!"<<endl;
        }
		_case++;
}
void fileread()
{
	int count=0;
	int s,a,b,c,d;
	in.open("input.txt");
	while(in>>s)
	{
		
		if(count==0)
		{
			tests=s;
			cout<<tests<<endl;
			count++;
		}
		else if(count==1)
		{
			row=s;
			cout<<row<<endl;
			count++;
		}
		else if(count==2)
		{
			in>>b>>c>>d;
				table[0][0]=s;
				table[0][1]=b;
				table[0][2]=c;
				table[0][3]=d;
				count++;
		}
		else if(count==3)
		{
			in>>b>>c>>d;
				table[1][0]=s;
				table[1][1]=b;
				table[1][2]=c;
				table[1][3]=d;
				count++;
			
		}
		else if(count==4)
		{
			in>>b>>c>>d;
				table[2][0]=s;
				table[2][1]=b;
				table[2][2]=c;
				table[2][3]=d;
				count++;
			
		}
		else if(count==5)
		{
			in>>b>>c>>d;
				table[3][0]=s;
				table[3][1]=b;
				table[3][2]=c;
				table[3][3]=d;
				count++;
			
		}
		else if(count==6)
		{
			displayTable();
			row2=s;
			for(int i=0; i<4; i++)
            {
                r1[i]=table[row-1][i];
            }
			count++;
		}
		else if(count==7)
		{
			in>>b>>c>>d;
				table[0][0]=s;
				table[0][1]=b;
				table[0][2]=c;
				table[0][3]=d;
				count++;
		}
		else if(count==8)
		{
			in>>b>>c>>d;
				table[1][0]=s;
				table[1][1]=b;
				table[1][2]=c;
				table[1][3]=d;
				count++;
		}
		else if(count==9)
		{
			in>>b>>c>>d;
				table[2][0]=s;
				table[2][1]=b;
				table[2][2]=c;
				table[2][3]=d;
				count++;
		}
		else if(count==10)
		{
			in>>b>>c>>d;
				table[3][0]=s;
				table[3][1]=b;
				table[3][2]=c;
				table[3][3]=d;
				count=1;
				for(int i=0; i<4; i++)
				{
        			r2[i]=table[row2-1][i];
				}
				displayTable();
				final();
			}
		}
	
}
int _tmain(int argc, _TCHAR* argv[])
{
	out.open("output.txt");
	fileread();
	return 0;
}

