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
				string linea; cin >> linea;
				std::map<char,int> letras;
				letras['Z']=0;
				letras['E']=0;
				letras['R']=0;
				letras['O']=0;
				letras['N']=0;
				letras['T']=0;
				letras['W']=0;
				letras['H']=0;
				letras['F']=0;
				letras['I']=0;
				letras['U']=0;
				letras['V']=0;
				letras['S']=0;
				letras['I']=0;
				letras['X']=0;
				letras['G']=0;
				for (int i=0; i<linea.length(); i++)
				{
					char letra = linea.at(i);
					letras[letra]++;
				}
				int c0,c1,c2,c3,c4,c5,c6,c7,c8,c9 = 0;
				c6 = letras['X'];
				forn(i,c6)
				{
					letras['S']--; letras['I']--; letras['X']--;
				}
				c0= letras['Z'];
				forn(i,c0)
				{
					letras['Z']--; letras['E']--; letras['R']--; letras['O']--;
				}
				c2 = letras['W'];
				forn(i,c2)
				{
					letras['T']--; letras['W']--; letras['O']--; 
				}
				c4 = letras['U'];
				forn(i,c4)
				{
					letras['F']--; letras['O']--; letras['U']--; letras['R']--;
				}
				c8 = letras['G'];
				forn(i,c8)
				{
					letras['E']--; letras['I']--; letras['G']--; letras['H']--; letras['T']--;
				}
				c1 = letras['O'];
				forn(i,c1)
				{
					letras['O']--; letras['N']--; letras['E']--; 
				}
				c3 = letras['T'];
				forn(i,c3)
				{
					letras['T']--; letras['H']--; letras['R']--; letras['E']--; letras['E']--; 
				}
				c5 = letras['F'];
				forn(i,c5)
				{
					letras['F']--; letras['I']--; letras['V']--; letras['E']--; 
				}
				c7 = letras['V'];
				forn(i,c7)
				{
					letras['S']--; letras['E']--; letras['V']--; letras['E']--; letras['N']--; 
				}
				c9 = letras['I'];
				forn(i,c9)
				{
					letras['N']--; letras['I']--; letras['N']--; letras['E']--;  
				}
				
				
				
				cout << "Case #" << cas+1 << ": ";
				forn(i,c0) { cout << "0"; }
				forn(i,c1) { cout << "1"; }
				forn(i,c2) { cout << "2"; }
				forn(i,c3) { cout << "3"; }
				forn(i,c4) { cout << "4"; }
				forn(i,c5) { cout << "5"; }
				forn(i,c6) { cout << "6"; }
				forn(i,c7) { cout << "7"; }
				forn(i,c8) { cout << "8"; }
				forn(i,c9) { cout << "9"; }
				cout << endl;
	}

    return 0;
}
