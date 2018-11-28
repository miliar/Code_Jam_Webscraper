#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

int n, t, a, b;
#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)

int main() {
	ifstream myfile;
	myfile.open("input.txt");
	ofstream myfile2;
	myfile2.open("output.txt");
	
	myfile >> n;

	for (int u = 0; u < n; u++) {
		myfile >>a >>b;
		int** arr = new int*[a];
		for(int i = 0; i < a; ++i)
			 arr[i] = new int[b];
		int** arr2 = new int*[a];
		for(int i = 0; i < a; ++i)
			 arr2[i] = new int[b];
		int max=0;
		For(i,0,a-1)
		{
			For(j,0,b-1)
			{
				myfile >> arr[i][j];
				if(max<arr[i][j])
					max=arr[i][j];
				arr2[i][j]=101;
			}
		}
		bool mark=true;
		for(int m=max;m>0;m--)
		{
			
		
			For(i,0,a-1)
			{
				bool mark=true;
				
				
				For(j,0,b-1)
				{
					if(arr2[i][j]==0)
					{
						mark=false;
						break;
					}	
				}
				if(mark)
				{
					For(j,0,b-1)
					{
						if(arr2[i][j]>m)
							arr2[i][j]=m;
					}
				}
			}	
			For(j,0,b-1)
			{
				bool mark=true;
					
				For(i,0,a-1)
				{
					if(arr2[i][j]==0)
					{
						mark=false;
						break;
					}	
				}
				if(mark)
				{
				For(i,0,a-1)
					{
						if(arr2[i][j]>m)
							arr2[i][j]=m;
					}
				}
			}
			for (int i=a-1;i>0;i--)
			{
				bool mark=true;
				For(j,0,b-1)
				{
					if(arr2[i][j]==0)
					{
						mark=false;
						break;
					}	
				}
				if(mark)
				{
				for (int j=b-1;j>0;j--)
				{
					if(arr2[i][j]>m)
						arr2[i][j]=m;
				}
				}
			}
			for (int j=b-1;j>0;j--)
			{
				bool mark=true;
					
				For(i,0,a-1)
				{
					if(arr2[i][j]==0)
					{
						mark=false;
						break;
					}	
				}
				if(mark)
				{
					for (int i=a-1;i>0;i--)
					{
						if(arr2[i][j]>m)
							arr2[i][j]=m;
				}
				}
			}
			
			For(i,0,a-1)
			{
				For(j,0,b-1)
				{
					if(arr2[i][j]==arr[i][j])
							arr2[i][j]=0;
				}
			}
		
		}
		int tot=0;
		For(i,0,a-1)
			{
				For(j,0,b-1)
				{
					tot += arr2[i][j];
				}
			}
		
			if(tot==0)
			{
				myfile2<<"Case #"<<u+1<<": "<< "YES"<<endl;
			}
			else
			{
				myfile2<<"Case #"<<u+1<<": "<< "NO"<<endl;
			}
		
	}
	system("pause");
}
