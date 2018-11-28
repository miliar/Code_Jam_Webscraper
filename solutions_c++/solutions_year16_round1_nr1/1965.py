#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <functional>
#include <list>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;

int main()
{
	string s;
	ifstream in;
	ofstream out;
	in.open("A.in");
	out.open("A.out");
	int t;
	in>>t;
	for(int i=1;i<=t;i++)
	{
		in>>s;
		list <char> v;
		v.push_back(s[0]);
		for(int j=1;j<s.length();j++)
		{
			if(s[j]>=s[0] && s[j]>=v.front())
			{
				v.push_front(s[j]);
			}
			
			else
			v.push_back(s[j]);	
		} 
		out <<"Case #"<<i<<": ";
		for (std::list<char>::const_iterator i = v.begin(); i != v.end(); ++i)
    		out << *i;
    		
    		
    	out<<'\n';	
	}
	return 0;
}
