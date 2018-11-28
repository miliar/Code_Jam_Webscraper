#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

//int i, j, k, m, n, l;
//int a[1005], v[1005], d[1005];

int main() {
    //freopen("x.in", "r", stdin);

	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);

	freopen("proba2.txt", "r", stdin);
	freopen("probaki2.txt", "w", stdout);

	int  tn; cin >> tn;
    map<char,int> m;
    vector<int> szamok;

	for(int tt=1; tt<=tn; ++tt)
    {
	    m.clear();
	    szamok.clear();
		string s;
		cin>>s;
		for(int i=0; i<s.size(); ++i)
        {
            m[s[i]]++;
        }
        int a=m['Z'];
        for(int i=0; i<a; i++)
        {
            szamok.push_back(0);
            m['Z']--;
            m['E']--;
            m['R']--;
            m['O']--;
        }
        a=m['G'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(8);
            m['E']--;
            m['I']--;
            m['G']--;
            m['H']--;
            m['T']--;
        }

         a=m['W'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(2);
            m['T']--;
            m['W']--;
            m['O']--;
        }

          a=m['X'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(6);
            m['S']--;
            m['I']--;
            m['X']--;
        }

          a=m['U'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(4);
            m['F']--;
            m['O']--;
            m['U']--;
            m['R']--;
        }

          a=m['F'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(5);
            m['F']--;
            m['I']--;
            m['V']--;
            m['E']--;
        }

          a=m['V'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(7);
            m['S']--;
            m['E']--;
            m['V']--;
            m['E']--;
            m['N']--;
        }

            a=m['H'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(3);
            m['T']--;
            m['H']--;
            m['R']--;
            m['E']--;
            m['E']--;
        }

            a=m['I'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(9);
            m['N']--;
            m['I']--;
            m['N']--;
            m['E']--;
        }

            a=m['N'];
          for(int i=0; i<a; i++)
        {
            szamok.push_back(1);
            m['O']--;
            m['N']--;
            m['E']--;

        }
        sort(szamok.begin(),szamok.end());
        cout<<"Case #"<<tt<<": ";
        for(int i=0; i<szamok.size(); ++i) cout<<szamok[i];
        cout<<endl;


	}
	return 0;
}
