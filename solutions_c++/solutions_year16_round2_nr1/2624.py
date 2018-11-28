/*************************************************************
CodeJam 2016 - https://code.google.com/codejam/contest/11254486/dashboard
30/04/16
Sahil Arora
*************************************************************/
#include<bits/stdc++.h>
using namespace std;

#define ll 			long long
#define vll 		vector< long long >
#define vvll 		vector< vll >
#define vd 			vector< double > 
#define ford(i,x,a) for(ll i=x;i<=a;++i)
#define fore(i,x,a) for(ll i=x;i>=a;--i)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define ff first
#define ss second
#define all(a) a.begin(), a.end()
#define pb push_back 
const ll mod = 1e9+7;

int main(int argc, char const *argv[])
{
	/* code */
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	long long test;
	cin>>test;
	ford(t,1,test){
		cout<<"Case #"<<t<<": ";
		string s;
		cin>>s;
		vll v(10,0), a(26,0);
		ford(i,0,s.size()-1)
			++a[s[i]-'A'];
		v[0] = a['Z' - 'A'];
		a['Z'-'A'] -= v[0];
		a['E'-'A'] -= v[0];
		a['R'-'A'] -= v[0];
		a['O' - 'A'] -= v[0];
		v[2] = a['W' - 'A'];
		a['W' - 'A'] -= v[2];
		a['O' - 'A'] -= v[2];
		a['T' - 'A'] -= v[2];
		v[6] = a['X' - 'A'];
		a['X' - 'A'] -= v[6];
		a['I' - 'A'] -= v[6];
		a['S' - 'A'] -= v[6];
		v[7] = a['S' - 'A'];
		a['E' - 'A'] -= v[7]*2;
		a['S' - 'A'] -= v[7];
		a['V' - 'A'] -= v[7];
		a['N' - 'A'] -= v[7];
		v[4] = a['U' - 'A'];
		a['U' - 'A'] -= v[4];
		a['F' - 'A'] -= v[4];
		a['O' - 'A'] -= v[4];
		a['R' - 'A'] -= v[4];
		v[5] = a['F' - 'A'];
		a['I' - 'A'] -= v[5];
		a['F' - 'A'] -= v[5];
		a['V' - 'A'] -= v[5];
		a['E' - 'A'] -= v[5];
		
		v[1] = a['O' - 'A'];
		a['N' - 'A'] -= v[1];
		a['O' - 'A'] -= v[1];
		a['E' - 'A'] -= v[1];
		v[9] = a['N' - 'A']/2;
		a['I' - 'A'] -= v[9];
		a['E' - 'A'] -= v[9];
		a['N' - 'A'] -= v[9]*2;
		v[3] = a['R' - 'A'];
		a['T' - 'A'] -= v[3];
		a['H' - 'A'] -= v[3];
		a['R' - 'A'] -= v[3];
		a['E' - 'A'] -= v[3]*2;
		v[8] = a['I' - 'A'];
		ford(i,0,9){
			ford(j,1,v[i])
				cout<<i;
		}			
		cout<<"\n";
	}
	return 0;
}
