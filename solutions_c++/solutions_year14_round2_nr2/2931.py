#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <Windows.h>

using namespace std;

int main()
{
		 long long int a=100000007,b=1110000,k=2;
	 ifstream fin("B-large.in");
	 ofstream fout("B-large.out");
	 int t=0;
	 fin>>t;
	 for (int l = 0; l < t; l++)
	 {
		 fin>>a>>b>>k;
		 int count=0;
		 for (int i = 0; i < k; i++)
		 {
			 for (int q = 0; q < a; q++)
			 {
				 for (int w = 0; w < b; w++)
				 {
					 int z=q&w;
					 if( z==i )
					 {
						 count++;
					 }
				 }

			 }
		 }
		 fout<<"Case #"<<l+1<<": "<<count<<endl;
	 }


	return 0;
}