using namespace std;
#include <cstdlib>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define rep(i,j,k) for(int i=j;i<k;i++)
#define rep_(i,j,k) for(k::iterator i=j.begin();i!=j.end();i++)
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

string s;
int k,S,n;

bool can()
{
	rep(i,S-k+1,S)
		if (s[i]=='-') return false;
	return true;
}

void pp(int T)
{
	cin >> s >> k;
	S=s.length();
	n=0;
	rep(i,0,S-k+1)
		if (s[i]=='-')
		{
			n++;
			rep(j,i,i+k)
				s[j]='+'+'-'-s[j];
			// cout << s << endl;
		}
	if (can()) cout << "case #" << T << ": " << n << endl;
	else cout << "case #" << T << ": IMPOSSIBLE" << endl;
}

int main()
{
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int TT;
	cin >> TT;
	rep(T,1,TT+1) pp(T);
	return 0;
}

/*
Usage:
	cin >> n;  rep(i,0,n);
	set<int> s;rep_(i,s,set<int>);
*/
