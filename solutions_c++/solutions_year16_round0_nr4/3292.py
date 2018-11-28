#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fstream>
using namespace std;
int main()
{
int t,test,k,c,s;
ifstream fin;
ofstream fout;
fin.open("D-small-attempt0.in",ios::in);
fout.open("output.txt",ios::out);
fin>>t;
test=t;
while(t--)
{
	fin>>k>>c>>s;
	fout<<"Case #"<<test-t<<": ";
	for(int i=1;i<=s;i++)
	{
		fout<<i<<" ";
	}
	fout<<"\n";
}
return 0;
}
