// jam_matrix.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int check_row(char a[4][4],int m,int n,char l);
int check_col(char a[4][4],int m,int n,char l);
int check_dia(char a[4][4],int m,int n,char l);
int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	char a[4][4];
	string s;
    ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("output.txt");
	in>>t;
	int tt=1;
h:while(tt<=t)
	{
		//cout<<"t="<<tt<<endl;
		int i,j;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
               in>>a[i][j];
			}
			//in>>s;
		}
		getline(in,s);
	/*	for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
               out<<a[i][j]; //cout
			}
			out<<endl;
		}*/
		out<<"Case #"<<tt<<": ";
		 //in>>s;  //this works fine actually
		 //in>>s;
		int xr=0,xc=0,xd=0,or=0,oc=0,od=0;
		if(check_row(a,4,4,'X')||check_col(a,4,4,'X')||check_dia(a,4,4,'X')){
             out<<"X won"<<endl;
			 tt++;
			 goto h;
		}
		else if(check_row(a,4,4,'O')||check_col(a,4,4,'O')||check_dia(a,4,4,'O')){
			out<<"O won"<<endl;
			tt++;
			goto h;
		}
		/*check if game is incomplete*/

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[i][j]=='.'){
					out<<"Game has not completed"<<endl;
					tt++;
					goto h;
				}
			}
		}
       out<<"Draw"<<endl;
	   tt++;
   }
	return 0;
}
int check_row(char a[4][4],int m,int n,char l)
{
	int i,j,count;
	for(i=0;i<m;i++)
	{
		count=0;
		for(j=0;j<n;j++)
		{
			if((a[i][j]==l) || (a[i][j]=='T'))
				count++;
			//else 
				//return 0;
			if(count==4)
				return 1;
		}
	}
	return 0;
}
int check_col(char a[4][4],int m,int n,char l)
{
	int i,j,count;
	for(i=0;i<m;i++)
	{
		count=0;
		for(j=0;j<n;j++)
		{
			if((a[j][i]==l) || (a[j][i]=='T'))
				count++;
			//else 
				//return 0;
			if(count==4)
				return 1;
		}
	}
	return 0;
}
int check_dia(char a[4][4],int m,int n,char l)
{
	int i,count=0;
	for(i=0;i<4;i++)
	{
		if((a[i][i]==l) || (a[i][i]=='T'))
			count++;
		if(count==4)
			return 1;
	}
	count=0;
	int j=0;
	for(i=3;i>=0;i--)
	{
		
		if((a[j][i]==l) || (a[j][i]=='T')){
			count++;
			//cout<<endl<<a[j][i]<<" "<<"count="<<count<<endl;
		}
		else
			return 0;
		if(count==4)
			return 1;
		j++;
	}

}




