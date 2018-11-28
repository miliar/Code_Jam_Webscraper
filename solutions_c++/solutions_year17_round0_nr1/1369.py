#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <set>

using namespace std;

void solve(string &s, int k, int c, ofstream& out)
{
    int ans=0;
	int n=s.size();
	out<<"Case #"<<c<<": ";
	for (int i=0; i<n-k+1; ++i)
	{
	    if (s[i]=='-')
		{
			for (int j=i; j<k+i; ++j)
				s[j]=s[j]=='-'?'+':'-';
			++ans;
		}
	}
	bool valid=true;
	for (int i=0; i<n; ++i)
		if (s[i]=='-')
		{
		    valid=false;
		    break;
		}
	if (!valid)
		out<<"IMPOSSIBLE\n";
	else
		out<<ans<<"\n";
}

int main()
{
    ifstream in("A-large.in");
	ofstream out("a_output.txt");
    int t;
	in>>t;
	int i=1;
	while (t--)
	{
	    string s;
		int k;
		in>>s>>k;
	    solve(s, k, i, out);
		++i;
	}
	return 0;
}