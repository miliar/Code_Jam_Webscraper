#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<string.h>
#include<cmath>
#include<algorithm>
#include<iterator>
#include<numeric>
using namespace std;

#define SMALL 1
#define LARGE 1

string all = "RPS";
string other = "SRP";

bool construct(int n, int r, int p, int s, char c, string& res) {
	res = "";
	res.push_back(c);
	int rem[3] = {r, p, s};
	for(int i=0;i<n;i++) {
		string next = "";
		for(int j=0;j<res.size();j++) {
			int pos = all.find(res[j]);
			next.push_back(all[pos]);
			next.push_back(other[pos]);
		}
		res = next;
	}
	//cout<<res<<endl;
	for(int i=0;i<res.size();i++) {
		int pos = all.find(res[i]);
		rem[pos]--;
	}
	for(int i=0;i<3;i++) {
		if(rem[i])
			return false;
	}
	return true;
}

void zabat(string& s, int st, int end) {
	if(st == end) return;
	int n = end-st+1;
	zabat(s, st, st+(n/2)-1);
	zabat(s, st+(n/2), end);
	string a = s.substr(st, n/2);
	string b = s.substr(st+n/2, n/2);
	if(b < a) {
		s.replace(st, n/2, b);
		s.replace(st+n/2, n/2, a);
	}
}

int main() {
#ifdef LARGE
	freopen("a_large.i", "rt", stdin);
	freopen("a_large.o", "wt", stdout);
#elif SMALL
	freopen("a_small.i", "rt", stdin);
	freopen("a_small.o", "wt", stdout);
#else
	freopen("a_sample.i", "rt", stdin);
#endif

	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) {
		int n, r, p, s;
		cin>>n>>r>>p>>s;
		string res;
		for(int i=0;i<3;i++) {
			string cur;
			if(construct(n, r, p, s, all[i], cur) && (res.size() == 0 || cur < res))
				res = cur;
		}
		cout<<"Case #"<<tt<<": ";
		if(res.size() == 0) {
			cout<<"IMPOSSIBLE";
		} else {
			zabat(res, 0, res.size()-1);
			cout<<res;
		}
		cout<<endl;
	}

	return 0;
}
