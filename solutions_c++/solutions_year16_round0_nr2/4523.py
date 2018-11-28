#include <bits/stdc++.h>

using namespace std;
typedef pair<double, double> pi;
typedef pair<int,pi> pii;
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
const ll MOD = 1e9 + 7;

#define MAXN 200100
#define _PI 3.14159265358979323846
bool all_ok(string & s)
{
	for (char c: s) if ( c == '-') return false;
	return true;
}
int compute(string s)
{
	int cnt = 0;
	while (!all_ok(s))
	{
		char first = s[0];
		int inx = 0; 
		while (inx < s.size() && s[inx] == first) inx++;
		for (int i = 0; i < inx; i++) s[i] = s[i] == '+'? '-':'+';
		cnt++;
	}
	return cnt;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	cin>>T;
	int caseN = 1;
	while (T--)
	{
		cout<<"Case #"<<caseN++<<": ";
		string s; cin>>s;
		cout<<compute(s)<<"\n";
	}
}
