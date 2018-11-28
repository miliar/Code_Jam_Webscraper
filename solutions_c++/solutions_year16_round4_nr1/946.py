#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define dforn(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(v) v.begin(),v.end()

string convert(string st)
{
	string res = "";
	forn(i,st.size())
	{
		if(st[i] == 'S')
			res += "PRPS";
		else if(st[i] == 'P')
			res += "PRRS";
		else if(st[i] == 'R')
			res += "PSRS";
	}
	return res;
}

string calc3(int n, int p, int r, int s, string orden)
{
	if(n == 1)
	{
		if(p == 1)
			return "P";
		else if(r == 1)
			return "R";
		else if(s == 1)
			return "S";
	}
	if(orden == "SPR")
	{
		if(n == 2)
		{
			if(p == 0)
				return "SR";
			else if(r == 0)
				return "SP";
			else if(s == 0)
				return "PR";
		}
		int n2 = n/4;
		int p2 = p-n2, r2 = r-n2, s2 = s-n2;
		return convert(calc3(n2,r2,s2,p2,"RSP"));
	}
	else if(orden == "PRS")
	{
		if(n == 2)
		{
			if(p == 0)
				return "RS";
			else if(r == 0)
				return "PS";
			else if(s == 0)
				return "PR";
		}
		int n2 = n/4;
		int p2 = p-n2, r2 = r-n2, s2 = s-n2;
		return convert(calc3(n2,r2,s2,p2,"SPR"));
	}
	else if(orden == "RSP")
	{
		if(n == 2)
		{
			if(p == 0)
				return "RS";
			else if(r == 0)
				return "SP";
			else if(s == 0)
				return "RP";
		}
		int n2 = n/4;
		int p2 = p-n2, r2 = r-n2, s2 = s-n2;
		return convert(calc3(n2,r2,s2,p2,"PRS"));
	}
}

bool calc2(int n, int p, int r, int s)
{

	if(n == 1)
		return true;
	if(n == 2)
		return p != 2 && r != 2 && s != 2;
	int n2 = n/4;
	int p2 = p-n2, r2 = r-n2, s2 = s-n2;
	if(p2 < 0 || r2 < 0 || s2 < 0)
		return false;
	return calc2(n/4,r2,s2,p2);
}

string calc(int n, int p, int r, int s)
{
	if(n == 2)
	{
		if(p == 2 || r == 2 || s == 2)
			return "IMPOSSIBLE";
		if(p == 0)
			return "RS";
		if(r == 0)
			return "PS";
		if(s == 0)
			return "PR";
	}
	int n2 = n/4;
	int p2 = p-n2, r2 = r-n2, s2 = s-n2;
	if(p2 < 0 || r2 < 0 || s2 < 0)
		return "IMPOSSIBLE";
	if(!calc2(n/4,r2,s2,p2))
		return "IMPOSSIBLE";
	return convert(calc3(n2,r2,s2,p2,"SPR"));
}

int main()
{
	int casos;
	cin >> casos;
	for(int casito = 1; casito <= casos; casito++)
	{
		int n,r,p,s;
		cin >> n >> r >> p >> s;
		n = 1<<n;
		cout << "Case #" << casito << ": " << calc(n,p,r,s) << endl;
	}
}