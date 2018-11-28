#include <bits/stdc++.h>
using namespace std;
int main()
{
	cout.tie(0);
    std::ios::sync_with_stdio(false);
    ifstream fin;
    fin.open("input.in",ios::in);
    ofstream fout;
    fout.open("output.txt",ios::out);
	int t,T;
	fin>>T;
	for(t=1;t<=T;t++)
	{
		int k,c,s,i;
		fin>>k>>c>>s;
		fout<<"Case #"<<t<<": ";
		for(i=1;i<=s;i++)
		{
			fout<<i<<" ";
		}
		fout<<"\n";
	}
	return 0;
}