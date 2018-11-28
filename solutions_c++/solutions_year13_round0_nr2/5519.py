#include<iostream>
#include<conio.h>
#include<math.h>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<array>
#include<fstream>
#include<sstream>

using namespace std;

ifstream myfilein;
ofstream myfileout;
string line;	
bool myfunction (long long i,long long j) { return (i>j); }


void open2()
  {
    freopen("test2.in", "rt", stdin);
    freopen("test2.out", "wt", stdout);
  }  
 



int T,N,M;
string check;

void main()
	{ 
	open2();
	cin>>T;
	for (int i = 1; i <=T; i++)
	{
		cin>>N;
		cin>>M;

	//	if (N==1 || M==1)
	//	{
	//	check="YES";
	//	goto end;
	//	}
		int array1[100][100]={};
		int array2[100][100]={};
	


		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				cin>>array1[j][k];
				array2[j][k]=100;

			}
		}
	/// check horizontally	
		int cnt=0;
		int h=1;
		for (int j = 0; j < N; j++)
		{
			cnt=0;
			for (int k = 0; k < M; k++)
			{
				if((array1[j][k])==1)
				{
				cnt=cnt+1;
				}
			}

			if (cnt==M)
			{
			for (int l = 0; l < M; l++)
			{
				array2[j][l]=1;
			}			
			}


		}


		for (int k = 0; k < M; k++)
		{
			cnt=0;
			for (int j = 0; j < N; j++)
			{
				if((array1[j][k])==1)
				{
				cnt=cnt+1;
				}
			}

			if (cnt==N)
			{
			for (int l = 0; l < N; l++)
			{
				array2[l][k]=1;
			}			
			}

		}



		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				if(array2[j][k]==100)
				{
				array2[j][k]=2;
				}
			}
		}

		check = "YES";

		for (int j = 0; j < N; j++)
		{
			for (int k = 0; k < M; k++)
			{
				if(array2[j][k]!=array1[j][k])
				{
				check = "NO";
				goto end;
				}
			}
		}






end:
		cout<<"Case #"<<i<<": "<<check<<endl;
		
	}






	}