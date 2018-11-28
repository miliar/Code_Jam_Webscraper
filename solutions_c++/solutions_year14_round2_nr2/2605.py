#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#include<iostream>
#include<fstream>
#include <string>

int main() 
{
	ifstream fpInput("C:\\Users\\ametpall\\Downloads\\B-small-attempt0.in", ios::in);
	ofstream fpOutput("C:\\Res.txt", ios::out);
	long tc; fpInput>>tc;
	
	for(int tci = 0; tci < tc; tci++) 
	{		
		long a,b,k;			
		fpInput>>a>>b>>k;				
		
		int count = 0;
		for(long i = 0;i<a;i++)
		{
			for(long j = 0;j<b;j++)
			{
				if(((i&j) < k))
					count++;
			}
		}
			
		fpOutput<<"Case #"<< tci+1<<": ";	
		fpOutput<<count;
		fpOutput<<"\n";
				
	}

	
	return 0;
}
