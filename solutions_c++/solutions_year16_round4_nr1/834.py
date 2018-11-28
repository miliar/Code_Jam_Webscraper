#include<bits/stdc++.h>
using namespace std;

char lett[] = {'P', 'R', 'S'};

struct ris_t
{
	int cR = 0, cP = 0, cS = 0;
	string s="";
};

ris_t calcola(char c, int prof)
{
	if(prof == 0)
	{
		ris_t r ;
		r.cP = 0, r.cS = 0, r.cR = 0, r.s = "";

		if(c == 'P')
			r.cP=1, r.s="P";
		else if(c == 'R')
			r.cR=1, r.s="R";
		else
			r.cS=1, r.s="S";

		return r;
	}

	ris_t a,b;

	if(c == 'P')
	{
		a = calcola('P', prof-1);
		b = calcola('R', prof-1);
	}
	else if(c == 'S')
	{
		a = calcola('S', prof-1);
		b = calcola('P', prof-1);
	}
	else
	{
		a = calcola('R', prof-1);
		b = calcola('S', prof-1);
	}

	if(b.s < a.s)
		swap(a,b);

	ris_t r;
	r.cP = a.cP + b.cP;
	r.cS = a.cS + b.cS;
	r.cR = a.cR + b.cR;
	r.s = a.s + b.s;

	return r;
}

string foo()
{
	int N, R, P, S;
	cin >> N >> R >> P >> S;
	string sol = "Z";

	for(int i=0; i<3; ++i)
	{
		ris_t x = calcola(lett[i], N);

		if(x.cR == R && x.cS == S && x.cP == P)
			sol = min(sol, x.s);
	}

	if(sol == "Z")
		return "IMPOSSIBLE";
	return sol;
}

int main()
{
	int T;
	cin >> T;
	for(int i=1; i<=T; ++i)
		cout << "Case #" << i << ": " << foo() << "\n";
}
