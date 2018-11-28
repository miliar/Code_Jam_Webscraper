#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main(void)
{
	ofstream out;
	ifstream in;
	out.open("BB.txt");
	in.open("BA.txt");
	int n;
	in >> n;
	for(int e=0;e<n;e++)
	{
		string tmp;
		in >> tmp;
		int tot=0;
		for(int p=1;p<tmp.size();p++) if(tmp[p]!=tmp[p-1]) tot++;
		out <<"Case #"<<e+1<<": ";
		if(tmp[tmp.size()-1]=='+') out <<  tot << endl;
		if(tmp[tmp.size()-1]=='-') out << tot+1 << endl;
 	}
	return 0;
}
