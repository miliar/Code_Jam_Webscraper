#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <list>
using namespace std;

string solve(string s)
{
	list<char> m;
	m.push_front(s[0]);
	for(unsigned int i=1;i<s.size();i++)
	{
		cout<<*m.begin()<<" "<<s[i]<<endl;
		if((*m.begin()) > s[i])
		{
			m.push_back(s[i]);
		}else{
			m.push_front(s[i]);
		}
	}

	string ret="";
	for(list<char>::iterator it = m.begin(); it!=m.end();it++)
	{
		ret += *it;
	}
	return ret;
}


int main() {

	ifstream infile("small.in");
	if(!infile.is_open())
	{
		cout << "could not open .in" <<endl;
		exit(EXIT_FAILURE);
	}
	ofstream outfile("small.out");

	if(!outfile.is_open())
	{
		cout << "could not open .out" <<endl;
		exit(EXIT_FAILURE);
	}

	int lines = 0;

	infile>>lines;
	string line;
	getline(infile,line);

	for(int i=0;i<lines;i++)
	{
		getline(infile,line);
		cout<<"Case #"<< i+1 <<": "<<solve(line)<<endl;
		outfile<<"Case #"<< i+1 <<": "<<solve(line)<<endl;
	}
	return 0;
}
