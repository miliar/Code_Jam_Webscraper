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
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

// int i, j, k, m, n, l;

int main() {
    //freopen("x.in", "r", stdin);

	// freopen("A-small-attempt2.in", "r", stdin);
	// freopen("zzA-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	F1(tt,tn) {
		//cerr << tt << endl;
		string s,q;
		cin>>s;
		int ar[26]={0};
		int j,p[10]={0};
		F0(j,SZ(s)) ar[s[j]-'A']++;
int k;
		// F0(k,ar[25])

		while (ar[25]&&ar['E'-'A']&&ar['R'-'A']&&ar['O'-'A'])
		{
			// q+='0';
			p[0]++;
			ar[25]--;
			ar['E'-'A']--;
			ar['R'-'A']--;
			ar['O'-'A']--;
		}
		while (ar['T'-'A']&&ar['W'-'A']&&ar['O'-'A'])
		{
			// q+='2';
			p[2]++;
			ar['T'-'A']--;
			ar['W'-'A']--;
			ar['O'-'A']--;
		}
		while (ar['F'-'A']&&ar['U'-'A']&&ar['R'-'A']&&ar['O'-'A'])
		{
			// q+='4';
			p[4]++;
			ar['F'-'A']--;
			ar['U'-'A']--;
			ar['R'-'A']--;
			ar['O'-'A']--;
		}
		while (ar['S'-'A']&&ar['I'-'A']&&ar['X'-'A'])
		{
			// q+='6';
			p[6]++;
			ar['S'-'A']--;
			ar['I'-'A']--;
			ar['X'-'A']--;
		}
		while (ar['G'-'A']&&ar['E'-'A']&&ar['I'-'A']&&ar['H'-'A']&&ar['T'-'A'])
		{
			// q+='8';
			p[8]++;
			ar['E'-'A']--;
			ar['G'-'A']--;
			ar['H'-'A']--;
			ar['I'-'A']--;
			ar['T'-'A']--;
		}

		while(ar['O'-'A']&&ar['N'-'A']&&ar['E'-'A'])
		{
			// q+='1';
			p[1]++;
			ar['O'-'A']--;
			ar['N'-'A']--;
			ar['E'-'A']--;
		}


		
		while (ar['T'-'A']&&ar['E'-'A']>=2&&ar['R'-'A']&&ar['H'-'A'])
		{
			// q+='3';
			p[3]++;
			ar['E'-'A']-=2;
			ar['T'-'A']--;
			ar['R'-'A']--;
			ar['H'-'A']--;
		}
		
		while (ar['F'-'A']&&ar['E'-'A']&&ar['I'-'A']&&ar['V'-'A'])
		{
			// q+='5';
			p[5]++;
			ar['E'-'A']--;
			ar['F'-'A']--;
			ar['V'-'A']--;
			ar['I'-'A']--;
		}
		// F0(k,ar['X'-'A'])
		
		while (ar['S'-'A']&&ar['E'-'A']>=2&&ar['N'-'A']&&ar['V'-'A'])
		{
			// q+='7';
			p[7]++;
			ar['E'-'A']-=2;
			ar['S'-'A']--;
			ar['V'-'A']--;
			ar['N'-'A']--;
		}
		
		while (ar['E'-'A']&&ar['I'-'A']&&ar['N'-'A']>=2)
		{
			// q+='9';
			p[9]++;
			ar['E'-'A']--;
			// ar['F'-'A']--;
			ar['N'-'A']-=2;
			ar['I'-'A']--;
		}
  		printf("Case #%d: ", tt);
		// cout << q << endl;?
		int w,v;
		F0(w,10){
			F0(v,p[w])
			cout<<w;
		} 
		cout<<endl;
	}
	return 0;
}