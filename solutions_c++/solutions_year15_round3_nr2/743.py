#include <bits/stdc++.h>

using namespace std;

string keys, target;
int K, L, S;

bool match(string s, int p)
{
	for(int i=p; i<s.size(); i++)
		if(s[i] != s[i-p])
			return false;
	return true;
}

bool F[26];

bool possible()
{
	for(int i=0; i<target.size(); i++)
		if(F[target[i] - 'A'] == 0)
			return 0;
	return 1;
}

int getMax()
{
	if(!possible()) return 0;
	
	int need = -1;
	for(int i=1; i<target.size(); i++)
	{
		if(match(target, i))
		{
			need = i;
			break;
		}
	}
	
	if(need == -1) need = target.size();
		
	int have = S - target.size();
	return 1 + have / need;
}

bool prefix(string &s1, string &s2)
{
	if(s1.size() > s2.size()) return 0;
	for(int i=0; i<s1.size(); i++)
		if(s1[i] != s2[i])
			return 0;
	return 1;
}

int memo2[105][26];
int g(int k, char ch)
{
	if(memo2[k][ch - 'A'] != -1) return memo2[k][ch - 'A'];
	
	string s = target.substr(0, k) + ch;
	while(!prefix(s, target)) s = s.substr(1);
	
	return memo2[k][ch - 'A'] = s.size();
}

bool done[105][105];
double memo[105][105];
double f(int k, int p)
{
	if(done[k][p]) return memo[k][p];
	
	double x = (k == L ? 1 : 0);
	if(p < S)
	{
		for(int i=0; i<keys.size(); i++)
		{
			int w = g(k, keys[i]);
			x += 1.0 / K * f(w, p + 1);
		}
	}
	done[k][p] = 1;
	return memo[k][p] = x;
}

int main()
{
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cin>>K>>L>>S;
		cin>>keys>>target;
		
		memset(F, 0, sizeof(F));
		for(int i=0; i<keys.size(); i++)
			F[keys[i] - 'A'] = 1;
		
		int cnt = getMax();
		memset(done, 0, sizeof(done));
		memset(memo2, -1, sizeof(memo2));
		double x = cnt - f(0, 0);
		printf("Case #%d: %.6lf\n", caso, x);
	}
	
	return 0;
}
