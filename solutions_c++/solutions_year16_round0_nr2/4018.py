#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;

string flip(string old, int n)
{

	string ret = "";
	for(int i=n-1; i>-1; i--)
		ret += old[i]=='+' ? '-' : '+';
	for(int i=n; i<old.size(); i++)
		ret += old[i];
	return ret;
}


int main(int argc, char** argv)
{
string fName = argv[1];

fstream In((fName+".in").c_str(), ios::in);
fstream Out((fName + ".out").c_str(), ios::out);

int tests;

In >> tests;

cout << tests << endl;



for(int h=0; h<tests; h++)
{
	map<string, int> mp1;

	queue<pair<string, int> > q;

	string start;
	In >> start;

	q.push(make_pair(start, 0));
	string goal(start.size(), '+');	
	int ret = 0;

	while(!q.empty() )
	{

		string s = q.front().first;
		ret = q.front().second;
		q.pop();

		if(mp1[s] > 0)
			continue;
		mp1[s] = ret + 1;
		if(s==goal) break;

		for(int i=1; i<=s.size(); i++)
		{
			string temp = flip(s, i);
			q.push(make_pair(temp, ret+1));
		}
	}
	Out << "Case #" << h+1 << ": " << ret << endl;


}

In.close();

Out.close();

return 0;

}
 
