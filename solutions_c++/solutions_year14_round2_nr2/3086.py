#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main ()
{
	int testcases , A ,B , K , check1 , count=0 , x=1;
	ifstream fin("B-small-attempt1.in");
	fin>>testcases;

	ofstream fout("out.txt");

	while(testcases!=0)
	{
		fin>>A;
		fin>>B;
		fin>>K;
			for(int i=0;i<A;i++)
			{
				for(int j=0;j<B;j++)
				{
					check1 = i & j;
					if(check1 < K)
					{	
									count++;
					}


				}
			}
			fout<<"Case #"<<x<<":"<<" "<<count<<endl;
			count = 0;
			x++;
			testcases--;
	}
}