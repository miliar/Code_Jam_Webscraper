// B_Lawnmower_Large.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
#include "fstream"
using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int t,count=0;
	fin>>t;

	for(int n=0;n<t;n++)
	{
		//-----------------------------------Read Lawn Height
		int a,b,arr[101][101],arr2[101][101]={100};
		fin>>a>>b;

		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				fin>>arr[i][j];
			}
		}
		//-----------------------------------init arr2 = 100
		for(int i=0;i<101;i++)
			for(int j=0;j<101;j++)
				arr2[i][j]=100;

		for(int k=99;k>0;k--)
		{
			//-----------------------------------Left TO Right
			for(int i=0;i<a;i++)
			{
				count=0;

				for(int j=0;j<b;j++)
				{
					if(arr[i][j]<=k ) count++; 
				}
				if(count==b)
				{
					for(int j=0;j<b;j++) arr2[i][j]=k;
				}
			}
			//-----------------------------------Up TO Down
			for(int j=0;j<b;j++)
			{
				count=0;

				for(int i=0;i<a;i++)
				{
					if(arr[i][j]<=k ) count++; 
				}
				if(count==a)
				{
					for(int i=0;i<a;i++) arr2[i][j]=k;
				}
			}
			//-----------
		}
		//----------------------------------------------Search For Exist One ?
		bool error=false;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if(arr[i][j]!=arr2[i][j]) error=true; 
			}
		}
		if(error) 
			fout<<"Case #"<<n+1<<": NO"<<endl;
		else 
			fout<<"Case #"<<n+1<<": YES"<<endl;
	}
		//------------------------------------------------------END

	return 0;
}

