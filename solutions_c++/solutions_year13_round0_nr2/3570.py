

#include<iostream>
#include <string>
#include <bitset>
#include <limits>
#include<math.h>
#include<cmath>
#include<fstream>
#include<bitset>
#include<vector>
#include <sstream>
#include<algorithm>
#include<time.h>
#include<set>
#include<map>
#include <numeric>
//#include "Source.cpp"
using namespace std;
//Loop through coloum 
bool checkRow(int i,int j,vector< vector<int> > Case)
{
	bool bef=false;
	bool after=false;
	if(j==0)
		bef=true;
	if(j==Case[0].size()-1)
		after=true;
		for (int k = 0; k < Case[i].size(); k++)
		{
			if(Case[i][k]>Case[i][j]&&k<j)

			{ bef=true; break;}
		
		}
			for (int k = 0; k < Case[i].size(); k++)
		{
			if(Case[i][k]>Case[i][j]&&k>j)
			{after=true; break;}
		
		}
			if(bef==true&&after==true)
				return true;
	
	return false;
}
//loop throug row 
bool checkcol(int i,int j,vector< vector<int> > Case)
{
	bool bef=false;
	bool after=false;
	if(i==0)
		bef=true;
	if(i==Case.size()-1)
	after=true;
		for (int k = 0; k < Case.size(); k++)
		{
			if(Case[k][j]>Case[i][j]&&k<i)

			{ bef=true; break;}
		
		}
			for (int k = 0; k < Case.size(); k++)
		{
			if(Case[k][j]>Case[i][j]&&k>i)
			{after=true; break;}
		
		}
			if(bef==true&&after==true)
				return true;
	
	return false;
}
string check(int rows, int cols, vector< vector<int> > Case)
{

	
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			bool rcheck= checkRow(i,j,Case);
			bool cCheck=checkcol(i,j,Case);
			if(rcheck==true&&cCheck==true)
				return "NO";
		}
	}

	return "YES";
}
vector< vector<int> > init(vector< vector<int> > org)
{
	for (int i = 0; i < org.size(); i++)
	{
		for (int j = 0; j < org.size(); j++)
		{
			if(org[i][j]==1)
				org[i][j]==2;
		}
	}
	return org;
}




string check2(int rows, int cols, vector< vector<int> > Case)
{
	vector< vector<int> > Original(Case.begin(),Case.end());

		for (int i = 0; i < Original.size(); i++)
	{
		for (int j = 0; j < Original[i].size(); j++)
		{
			if(Original[i][j]<100)
				Original[i][j]=100;
		}
	}


	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			
			if(Case[i][j]==100)
					continue;
			else
			{
				bool row=true,col=true;
				int myval=Case[i][j];
				for (int k = 0; k < Case[i].size(); k++)
				{
					
					if(Case[i][k]>myval)
					{
						row=false; 
						break;
					}
				}
				
				for (int m = 0; m < Case.size(); m++)
				{
					//int colDiff=(100-Case[m][j]);
					if(Case[m][j]>myval)
					{
						col=false;
						break;}
				}
				if(row==false&&col==false)
					return "NO";

			}
			
		}
	}
	return "YES";
}
int convert(string s)
{
	int val;
	stringstream t(s);
	t>>val;
	return val;
}
int main()
{

	

	int Testcase;
	
	 string STRING;
	ifstream infile;
	infile.open ("B-large.in");
	ofstream Result;
Result.open("Result.txt");
string Test;

getline(infile,Test);
stringstream t(Test);
t>>Testcase;


for (int i = 0; i < Testcase; i++)
{
	int x=i;
	int row;
	int col;
		
	getline(infile,STRING);
	vector<int> size;
	int t;
	stringstream sizeline(STRING);
	while (sizeline>>t)
	{
		size.push_back(t);
	}
	row=size[0];
	col=size[1];
	size.clear();
	//cout<<row<<" "<<col<<endl;
	vector< vector<int> > Case(row);
	
	for (int j = 0; j < row; j++)
	{
		getline(infile,STRING);

		vector<int> size;
		int t;
		stringstream sizeline(STRING);
		while (sizeline>>t)
		{
			size.push_back(t);
		}
		Case[j]=size;
		size.clear();
	}
	if(row>1)
	Result<<"Case #"<<++x<<": "<<check2(row,col,Case)<<endl;
	else
		Result<<"Case #"<<++x<<": "<<"YES"<<endl;


	
	
}

	  infile.close();
	  Result.close();
	return 0;

}