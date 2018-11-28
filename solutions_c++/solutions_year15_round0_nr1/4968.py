#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;
	ifile.open("input.in");
	ofile.open("output.txt");
	int t,sm,pe,ad,mo;
	string s;
	ifile>>t;
	for(int i=1;i<=t;i++)
	{
		pe=ad=mo=0;
		ifile>>sm>>s;
		for(int j=0;j<s.length();j++)
		{
			if(j>pe){
				mo=j-pe;
				ad+=mo;
				pe+=mo;}
			pe+=s[j]-'0';
		}
		ofile<<"Case #"<<i<<": "<<ad<<endl;
	}
	return 0;

}