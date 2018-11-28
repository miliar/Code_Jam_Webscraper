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
string fileinPath = "F:\\Projects\\test1\\test1\\A-small-attempt0.in";
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
	int a[4];
	int ans1, ans2;
	int t,result,num;

	for (int k=1; k <=caseNum;k++)
	{
		result = -1; num = 0;
		fin >> ans1;
		for (int i = 1; i< ans1;i++ )
		{
			for (int j =0; j<4;j++)
				fin >> t;
		}
		for (int j =0; j<4; j++)
			fin >> a[j];
		for (int i = ans1; i< 4;i++ )
		{
			for (int j =0; j<4;j++)
				fin >> t;
		}
		fin >> ans2;
		for (int i = 1; i< ans2;i++ )
		{
			for (int j =0; j<4;j++)
				fin >> t;
		}
		for (int j =0; j<4; j++)
		{
			fin >> t;
			for (int i=0;i<4;i++)
			{
				if (t == a[i]) {
					num ++; result = t; break;
				}
			}
		}
		for (int i = ans2; i< 4;i++ )
		{
			for (int j =0; j<4;j++)
				fin >> t;
		}
	//	fout << fixed<< setprecision (7) ;
		switch (num){
		case 0:fout<<"Case #"<<k<<": Volunteer cheated!"<<endl;break;
		case 1:fout<<"Case #"<<k<<": "<< result <<endl;break;
		default:fout<<"Case #"<<k<<": Bad magician!"<<endl;break;
		}
		//fout<<"Case #"<<k<<": "<< t <<endl;
		//	fout<<"Case #"<<k<<": "<<"No"<<endl;
	}
	return 0;
}
