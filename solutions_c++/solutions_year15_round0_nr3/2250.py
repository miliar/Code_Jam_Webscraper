#include <iostream>
using namespace std;

enum state { s1, s_1, si, sj, sk, s_i, s_j, s_k};

state mul_table[8][8] = {
	{ s1,  s_1, si,  sj,  sk,  s_i, s_j, s_k }, // s11
	{ s_1, s1,  s_i, s_j, s_k, si,  sj,  sk  }, // s_11
	{ si,  s_i, s_1, sk,  s_j, s_1, s_k, sj  }, // si
	{ sj,  s_j, s_k, s_1, si,  sk,  s1,  s_i }, // sj
	{ sk,  s_k, sj,  s_i, s_1, s_j, si,  s1  }, // sk
	{ s_i,  si, s1,  s_k, sj,  s1,  sk,  s_j }, // si
	{ s_j,  sj, sk,  s1,  s_i, s_k, s_1, si  }, // sj
	{ s_k,  sk, s_j, si,  s1,  sj,  s_i, s_1 } // sk
};

state neg[8] = { s_1, s1,  s_i, s_j, s_k, si,  sj,  sk  };

void printcur(state s)
{
	switch(s)
	{
		case si: cout << "i\n"; break;
		case sj: cout << "j\n"; break;
		case sk: cout << "k\n"; break;
		case s_i: cout << "-i\n"; break;
		case s_j: cout << "-j\n"; break;
		case s_k: cout << "-k\n"; break;
		case s1: cout << "1\n"; break;
		case s_1: cout << "-1\n"; break;
	}
}

state next(state cur, char c)
{
	state to_mul = c == 'i' ? si : c == 'j' ? sj : sk;
	return mul_table[cur][to_mul];
}

void test(int64_t testnum)
{
	int64_t l, x;
	cin >> l >> x;
	bool ifound = false, jfound = false;
	
	string s;
	cin >> s;
	
	state cur = s1;
	for (int64_t i = 0; i < l * min(int64_t(8), x); i++)
	{
		cur = next(cur, s[i % l]);
		if (cur == si && !ifound)
		{
			ifound = true;
			cur = s1;
		}
		else if (cur == sj && ifound && !jfound)
		{
			jfound = true;
			cur = s1;
		}
	}
	//cout << ifound << " " << jfound << " ";
	
	
	if (ifound && jfound && x > 8)
	{
		if (x % 2 == 1)
			for (int64_t i = 0; i < l; i++)
				cur = next(cur, s[i]);
		state lval = s1;
		for (int64_t i = 0; i < l; i++)
			lval = next(lval, s[i]);
		
		int64_t left = x - 8 - x % 2;
		if (lval != s_1 && lval != s1 && left % 4 != 0)
			cur = neg[cur];
	}
	
	cout << "Case #" << testnum << ": " << (cur == sk && ifound && jfound ? "YES\n" : "NO\n");
}

int main()
{
	int64_t n;
	cin >> n;
	for (int64_t i = 1; i <= n; i++)
		test(i);
}