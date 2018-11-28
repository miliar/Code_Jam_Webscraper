#include <iostream>
#include <fstream>
using namespace std;

int main(int argc,char* argv[])
{
	ifstream fin(argv[1]);
	ofstream fout("pal.out");
	bool hashtable[1001];
	for(int i=1;i<1001;i++)
		hashtable[i]=false;
	hashtable[1]=true;
	hashtable[4]=true;
	hashtable[9]=true;
	hashtable[121]=true;
	hashtable[484]=true;
	int counter;
	int lowbound,upbound;
	fin>>counter;
	for(int i=0;i<counter;i++)
	{
		fin>>lowbound>>upbound;
		int sum=0;
		for(int j=lowbound;j<=upbound;j++)
		{
			if(hashtable[j])
				sum++;
		}
		fout<<"Case #"<<(i+1)<<": "<<sum<<endl;
	}
	return 0;
}