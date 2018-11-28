#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <list>
#include <set>
#include <map>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int x,y;
string s;

void solve()
{
	int i=1;
	string dx, dy;
	s="";
	if(x<0)
		dx = "EW";
	else
		dx = "WE";

	if(y<0)
		dy = "NS";
	else
		dy = "SN";

	for(i=1; i<=abs(x); ++i)
		s+=dx;
	for(i=1; i<=abs(y); ++i)
		s+=dy;
}

int main()
{
	int t,tt;
	fin>>tt;
	for(t=1; t<=tt; ++t)
	{
		fin>>x>>y;
		solve();
		fout<<"Case #"<<t<<": "<<s<<endl;
	}
	return 0;
}
