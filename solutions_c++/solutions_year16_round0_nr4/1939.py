#include<iostream>
#include<fstream>
using namespace std;


int main()
{
	ifstream fin("D-small-attempt0.in");
	ofstream fout("D-small-attempt0.out");
	int N;
	fin>>N;
	for(int n=1;n<=N;n++)
	{
		int K,C,S;
		fin>>K>>C>>S;
		if(S<K)
			fout<<"Case #"<<n<<": IMPOSSIBLE"<<endl;
		else
		{
			fout<<"Case #"<<n<<":";
		for(int i=1;i<=S;i++)
		{
			fout<<" "<<i;
		}
		fout<<endl;
		}
	}
	fout.close();
	fin.close();
	
	return 0;
}