#include<iostream>
#include<fstream>
#include<string>
#include<set>
using namespace std;
string proc(string &nu)
{
	set<string>all_d;
	unsigned int a , a0 = stoul(nu);
	if (a0 == 0)return "INSOMNIA";
	string as;
	unsigned short i=1;
	while (1)
	{
		a = a0*i;
		as = to_string(a);
		for (unsigned short j = 0; j<as.size(); j++)
		{
			all_d.insert(as.substr(j,1));
		}
		if (all_d.size() == 10){ return as; }
		i++;
	}
	return "INSOMNIA";
}
int main()
{
	string l; unsigned short max;
	fstream in,out;
	in.open("C:/Users/rou2a/Desktop/A-large.in");
	out.open("C:/Users/rou2a/Desktop/y.txt"); out.clear();
	in >> l; max = stoi(l);
	for (unsigned short i = 1;i<=max;i++)
	{
		in >> l;
		l = proc(l);
		out << "Case #"<<i<<": "<< l << endl;
	}

	return 0;
}
