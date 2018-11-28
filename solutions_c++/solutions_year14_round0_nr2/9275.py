// test1.cpp : Defines the entry point for the console application.
//

#include <stdio.h>  
#include <stdlib.h>  
#include <iostream>  
#include <fstream>
#include <cmath>
#include <iomanip> 
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

//string fileinPath = "F:\\Projects\\test1\\test1\\in.txt";
string fileinPath = "F:\\Projects\\test1\\test1\\B-large.in";
string fileoutPath = "F:\\Projects\\test1\\test1\\out.txt";

fstream fin(fileinPath );
ofstream fout(fileoutPath);
//
//bool   cmp( vector<vector<int>>&   s1,  vector<vector<int>>&   s2)  
//{  
//	if( s1[0][0] == s2[0][0])
//		return   s1[0][1] < s2[0][1];  
//	else 
//		return s1[0][0] < s2[0][0];
//}
//
//int getdis(int x1, int y1, int x2, int y2)
//{
//	return abs(x1-x2)+abs(y1-y2);
//}
//double getdis2(double x1, double y1, int x2, int y2)
//{
//	return abs(x1-x2)+abs(y1-y2);
//}


void getPos(vector<vector<int>>& rec,int& x,int& y,int& sum,int n)
{

}

int main()
{
	int caseNum;
	fin>>caseNum;
	double C, F, X;
	double H;
	double t,v;

	for (int k=1; k <=caseNum;k++)
	{
		fin>>C>>F>>X;
		H = 0; t = 0; v =2.0;
		while ( true )
		{
			if (C+C*v/F >=X)//not buy
			{
				t+=(X-H)/v;
				break;
			}
			else {	//buy
			//	t+=C/v+C/F;
				t+=C/v;
				H= 0;
				v+=F;
			}
		}
		fout << fixed<< setprecision (7) ;
		fout<<"Case #"<<k<<": "<< t <<endl;
		//	fout<<"Case #"<<k<<": "<<"No"<<endl;
	}
	return 0;
}
