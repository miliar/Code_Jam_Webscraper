#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
#include <functional>
#include <map>
#include <string>
#include <fstream>

using namespace std;
typedef long long ll;

void invert(string S,int pos)
{
	if(S[pos]=='+')
	
		S[pos]=='-';
	else
		S[pos]=='+';
}

void pancake(string s,ll &count)
{
	ll i;
	for(i=0;(i<s.length()-1);i++)
	{
		if(s[i]!=s[i+1])
		count++;
	}
	
	if(s[i]=='-')
	{
		count++;
	}
}





int main()
{
	ifstream in;
	ofstream out;
	in.open("b.in");
	out.open("b.out");
	int t;
	in>>t;
	for(int k=1;k<=t;k++)
	{
		string s;
		ll count=0;
		in>>s;
		pancake(s,count);
		out<<"Case #"<<k<<": "<<count<<'\n';
	}
}




