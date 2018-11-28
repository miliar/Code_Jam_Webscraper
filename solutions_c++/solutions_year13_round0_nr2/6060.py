#include<iostream>
#include<fstream>

using namespace std;

bool lookForRow (int **arr , int row , int len)
{
	for(int i = 1 ; i<len ; i++)
	{
		if(arr[row][i-1] != arr[row][i])
					return false;
	}
	return true;
}

bool lookForCol (int **arr , int col , int len)
{
	for(int i = 1 ; i<len ; i++)
	{
		if(arr[i][col] != arr[i-1][col])
					return false;
	}
	return true;
}

int main()
{
	int n,m,iterate;
	bool imp ;
	ifstream in("a.txt");
	ofstream out;
	out.open ("out.txt");

	in>> iterate;
	in.get();
	for(int it = 0 ;it<iterate ; it++)
	{
		in>>n>>m;
		imp = true;

		int **lownArr	= new int* [n];
		
		for(int i = 0; i<n ; i++)
			lownArr[i]	= new int [m];

		for(int i = 0 ; i<n ; i++)
			for(int j = 0 ; j<m ; j++)
			{
				in>>lownArr[i][j];
			}

		for(int i = 0 ; i<n ; i++)
		{
			if(lownArr[i][0] == 1)
				if(lookForRow(lownArr,i,m))
					continue;
			for(int j = 0 ; j<m ; j++)	
			{
				if(lownArr[i][j] == 1)
					if(lookForCol(lownArr,j,n) == false)
					{
							imp=false;
							break;
					}
			}
			if(imp == false)
				break;
		}


		if(imp == true)
			out <<"Case #"<<it+1<< ": YES"<<endl;
		else
			out <<"Case #"<<it+1<< ": NO"<<endl;

	}
	
	system("pause");
	return 0;
}