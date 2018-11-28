#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");


bool large(char a, char b)
{
	string ab = "";
	ab = ab + a + b;
	return ( (ab == "RS") || (ab == "SP") || (ab =="PR") );
}




bool test(string st)
{
	string newst;

	while (st.length() > 1)
	{
		newst = "";
		for (int i = 0; i < st.length(); i+= 2)
		{
			if ( large(st[i], st[i + 1]) )
				newst += st[i];
			else if ( large(st[i + 1], st[i]) )
				newst += st[i + 1];
			else
				return false;
		}
		st = newst;
	}
	return true;
}


string perm(int p, int r, int s, string st)
{
	if (p + r + s == 0)
	{
		if (test(st))
			return st;
		else
			return "";
	} 


	string newst, ans;
	if (p > 0) 
	{
		newst = st + "P";
		ans = perm(p - 1, r, s, newst);
		if (ans != "") return ans;
	}

	if (r > 0) 
	{
		newst = st + "R";
		ans = perm(p, r - 1, s, newst);
		if (ans != "") return ans;
	}

	if (s > 0) 
	{
		newst = st + "S";
		ans = perm(p, r, s - 1, newst);
		if (ans != "") return ans;
	}

	return "";
	
}


int main()
{
	int T;
	fin >> T;
	for (int ca = 1; ca <= T; ca++)
	{
		fout << "Case #" << ca << ": ";
		int n, r, p, s;
		fin >> n >> r >> p >> s;
		string st = perm(p, r, s, "");
		if (st == "") st = "IMPOSSIBLE";
		fout << st << endl;
	}

}