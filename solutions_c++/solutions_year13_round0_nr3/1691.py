#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll unsigned long long int
#define uli unsigned long int
#define MAX (int)1e6

using namespace std;

ofstream fout ("C.out");
ifstream fin ("C-large-1.in");
//ifstream fin ("C.in");
#define cout fout
#define cin fin

bool isPalin(ll n) {
    stringstream sout;
    sout<<n;
    string s = sout.str();
    int l = s.size();
    for(int i = 0 ; i < l/2; i++) {
        if(s[i] != s[l - i - 1]) {
            return false;
        }
    }
    return true;
}

void add(int i, string &k) {
	if(k[i] == '9')
	{
		if(i==k.size()-1)
		{
			k += "1";
			k[i] = '0';
		}
		else
		{
			k[i] = '0';
			add(i+1, k);
		}
	}
	else
		k[i] = (char)((int)k[i] +1);
}	

ll getNext(ll n) {
    stringstream sout;
    sout<<n;
    string s = sout.str();
    
    reverse(s.begin(),s.end());
	add(0, s);
	
	int l = s.size();
	for(int i=0; i<l/2; i++) {
		if(s[i]==s[l-i-1])
			continue;
		else if(s[i] < s[l-i-1])
			s[i] = s[l-i-1];
		else {
			add(i+1, s);
			s[i] = s[l-i-1];
		}
	}
    stringstream sin(s);	
    ll ret;
    sin >> ret;
    return ret;
}


int main() {
    int t;
    cin>>t;
    REP(T,t) {
        ll a, b, cnt = 0, palin = 0;
        cin>>a>>b;
        ll le = (ll)ceil(sqrt(a));
        ll ge = (ll)floor(sqrt(b));
        for(ll i = le; i <= ge ; i = getNext(i)) {
            if(isPalin(i) && isPalin(i*i)) {
                cnt++;
            }
        }
        cout<<"Case #"<<T+1<<": "<<cnt<<endl;
    }
    system("pause");
    return 0;
}
