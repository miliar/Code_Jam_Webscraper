#include<iostream>
#include<fstream>
using namespace std;
int main()
{

	long long n;
	long long r,t,i,nc,rc;
	ifstream fin("c:/a.txt");
	ofstream fout("C:/o.txt");
	fin>>n;

	for(i=0;i<n;i++)
	{
		fin>>r>>t;
		nc=0;

		while(1)
		{
			rc=r+r+1;
			t=t-rc;
			if(t>=0)
				nc++;
			else
				break;
			r=r+2;
		}

		fout<<"Case #"<<(i+1)<<": "<<nc<<endl;

	}

	return 0;
}