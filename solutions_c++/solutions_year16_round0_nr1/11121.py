#include<iostream>
#include<string>
#include<map>
#include<fstream>
using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T;
	in >> T;
	for(int t=0; t<T; t++)
	{
		int n;
		in >> n;
		int dn = n;
		if(n==0)
		{
			out << "Case #" << (t+1) <<": INSOMNIA\n";
			continue;
		}
		map<char,bool> nset;
		int counts = 1;
		while(true)
		{
			string str = to_string(dn);
			for(unsigned int o=0; o<str.length(); o++)
			{
				nset[str[o]] = true;
			}
			if(nset.size()==10)
			{
				break;
			}
			else
			{
				dn+=n;
			}
			counts++;
		}
		out << "Case #" << (t+1) <<": " << counts*n << '\n';
	}
}