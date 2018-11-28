#include<cstdio>
#include<fstream>
#include<iostream>

using namespace std;

int main()
{
	std::ifstream fi("input.txt");
	int t;
	fi>>t;
	std::ofstream fo("op.txt");
	for(int i=1;i<=t;i++)
	{
		int a,b,k,cnt=0;
		fi>>a>>b>>k;
		for(int p=0;p<a;p++)
			for(int q=0;q<b;q++)
				if((p&q)<k)
					cnt++;
		fo<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}
