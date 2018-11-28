#include <iostream>
#include <fstream>
using namespace std;


int main()
{
	int size,A,B,K,temp,wins=0;
	unsigned int a;
	unsigned int b;
	ifstream fin("B-small-attempt0 (1).in");
	ofstream fout("output.txt");
	fin>>size;
	for(int i=0;i<size;i++)
	{	
		fin>>A;
		fin>>B;
		fin>>K;
		wins=0;
		for (int j=0;j<A;j++)
		{
			for(int k=0;k<B;k++)
			{
				a=j;
				b=k;
				temp=a&b;
				if(temp<K)
					wins++;

			}
		}
		fout<<"Case #"<<i+1<<": "<<wins<<endl;
		
	}
	fin.close();
	fout.close();
	return 0;
	
}