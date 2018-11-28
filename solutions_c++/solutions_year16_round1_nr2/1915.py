#include <bits/stdc++.h>
#include <string>
using namespace std;


#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	

	int t; cin >> t;
	forn(cas, t) {
		int n; cin >> n;
		int h;
		std::map<int,int> aparece;
		for (int i=0; i< ((2*(n*n))-n); i++)
		{
			cin >> h;
			aparece[h]++;
		}
		
		cout << "Case #" << cas+1 << ": ";
		
		std::map<int,int>::iterator rit;
		for (rit=aparece.begin(); rit!=aparece.end(); ++rit)
		{
			
			if ((aparece[rit->first] % 2) != 0)
			{
				cout << rit->first << " ";
			}
		}
		cout << endl;
	}

    return 0;
}
