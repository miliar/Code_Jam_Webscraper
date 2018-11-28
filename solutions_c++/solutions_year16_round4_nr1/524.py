#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <deque>
#include <string>

using namespace std;

int t,T;

#define ULL unsigned long long

string allwin(string u, int n)
{
	string r;
	
	if (n == 0)
	{
		return u;
	}
		
	string q1, q2;
	q1 = allwin(u, n-1);
	string other;
	if (u == "P")
		other = "R";
	if (u == "S")
		other = "P";
	if (u == "R")
		other = "S";
	q2 = allwin(other, n-1);

	r = q1+q2;
	if (q2+q1<r)
		r=q2+q1;
	return r;
}


void runtestcase()
{	
	int N, R, P, S;
	cin >> N >> R >> P >> S;

	for (int n=1;n<=N;n++)
	{
		int R0, P0, S0, su;
		R0 = R;
		P0 = P;
		S0 = S;
		su = (P + R + S) / 2; 
		S = su - R0;
		P = su - S0;
		R = su - P0;		
		if ((S<0) || (R<0) || (P<0))
		{
			cout << "IMPOSSIBLE";
			return;
		}
	}
	string q;
	if (S==1)
		q = "S";
	if (R ==1)
		q = "R";
	if (P ==1)
		q= "P";
	cout << allwin(q, N);	
}

void main()
{	
	
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		cerr << t;
		cout << "Case #" << t << ": ";
		runtestcase();
		cout << endl;
	}	
}