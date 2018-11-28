#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

#include <ctime>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>

#define all(v) v.begin(),v.end()
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const ld epsylon = 1e-9;
typedef unsigned int ui;
inline long double get_time(){   
	return (long double)clock()/CLOCKS_PER_SEC;
};

ll n;
int m;

struct state{
	int beg, end, pass;
	state(int b, int e, int p):beg(b),end(e),pass(p){}
	bool operator < (const state & oth) const
	{
		return beg < oth.beg;
	}
};
vector <state> states;
ll MOD = 1000002013;

bool goodForSwap(int i, int j)
{
	if (states[i].beg > states[j].beg) swap(states[i], states[j]);
	if (states[i].end < states[j].beg) return false;
	if (states[i].beg < states[j].beg && states[i].end < states[j].end)
		return true;
	return false;
}

void clear0()
{
	nach:
	for (int i = 0; i < states.size(); ++i)
	{
		if(states[i].pass == 0) {
			states.erase(states.begin() + i);
			goto nach;
		}
	}
}

void swapmax(int i, int j)
{
	int pass = min(states[i].pass, states[j].pass);
	if (pass == 0) return;
	states[i].pass -= pass;
	states[j].pass -= pass;
	states.push_back(state(states[i].beg, states[j].end,pass));
	states.push_back(state(states[j].beg, states[i].end, pass));
}

ll form(int i)
{
	ll rez = 0;
	ll res = states[i].end - states[i].beg;
	res--;
	rez = (((res+1)*n)%MOD - ((res*(res+1))%MOD)/2)%MOD;
	return (rez*states[i].pass)%MOD;
}

ll calc()
{
	ll res = 0;
	for (int i = 0; i < states.size(); ++i)
	{
		res = (res + form(i) % MOD);
	}
	return res;
}

ll solve()
{
	ll firstwil = calc();
	for (int k = 0; k < 15; ++k)
	{	
		cerr << k << endl;
		for (int i = 0; i < states.size(); ++i)
		{
			for (int j = i + 1; j < states.size(); ++j)
			{
				if (goodForSwap(i, j))
				{
					swapmax(i, j);
					clear0();
				}
			}
		}
	}
	ll res = calc();
	return firstwil - res;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	//program
	int tests;
 	scanf("%d\n",&tests);
	for (int CASE = 1; CASE <= tests; ++CASE){
		states.clear();
		cin >> n >> m;
		state st(0,0,0);
		for (int i = 0; i < m; ++i)
		{
			cin >> st.beg >> st.end >> st.pass;
			states.push_back(st);
		}
		sort(states.begin(), states.end());
		cout << "Case #" << CASE << ": " << solve() << endl;
	}
	//end program
	return 0;
}




