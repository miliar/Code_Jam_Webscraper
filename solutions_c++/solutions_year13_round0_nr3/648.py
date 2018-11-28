#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define fi first
#define se second

vector<string> v;

string inv(const string& s){
	string res = "";
	for(int i=s.length()-1;i>=0;i--)
		res.pb(s[i]);
	return res;
}

inline bool cmp(const string& l, const string& r){
	if(l.size() == r.size())
		return lexicographical_compare(l.begin(), l.end(), r.begin(), r.end());
	else
		return l.size() < r.size();
}

inline string minStr(int l, int k){
	string res = "";
	for(int i=0;i<l-k;i++)
		res.pb('0');
	for(int i=0;i<k;i++)
		res.pb('1');
	return res;
}

inline char mult(char a, char b){
	return char('0' + (a-'0')*(b-'0'));
}

inline char pls(char a, char b){
	return char(a + b - '0');
}

string sqr(const string& s){
	string res(2*s.size()-1, '0');
	for(int i=s.size()-1;i>=0;i--)
		for(int j=s.size()-1;j>=0;j--)
			res[i+j] = pls(res[i+j], mult(s[i],s[j]));
	return res;
}

inline void init(){
	string s, is;
	for(int l=3;l<26;l++){
		s = minStr(l, 3);
		do{
			is = inv(s);
			v.pb(sqr("1"+s+"1"+is+"1"));
			v.pb(sqr("1"+s+"0"+is+"1"));
			v.pb(sqr("1"+s+is+"1"));
		}while(next_permutation(s.begin(), s.end()));		
	}
	for(int l=2;l<26;l++){
		s = minStr(l, 2);
		do{
			is = inv(s);
			v.pb(sqr("1"+s+"1"+is+"1"));
			v.pb(sqr("1"+s+"0"+is+"1"));
			v.pb(sqr("1"+s+is+"1"));
		}while(next_permutation(s.begin(), s.end()));		
	}
	for(int l=1;l<26;l++){
		s = minStr(l, 1);
		do{
			is = inv(s);
			v.pb(sqr("1"+s+"1"+is+"1"));
			v.pb(sqr("1"+s+"0"+is+"1"));
			v.pb(sqr("1"+s+is+"1"));
			v.pb(sqr("1"+s+"2"+is+"1"));
		}while(next_permutation(s.begin(), s.end()));		
	}
	for(int l=0;l<26;l++){
		s = minStr(l, 0);
		is = inv(s);
		v.pb(sqr("1"+s+"1"+is+"1"));
		v.pb(sqr("1"+s+"0"+is+"1"));
		v.pb(sqr("1"+s+is+"1"));
		v.pb(sqr("2"+s+"1"+is+"2"));
		v.pb(sqr("2"+s+"0"+is+"2"));
		v.pb(sqr("2"+s+is+"2"));
		v.pb(sqr("1"+s+"2"+is+"1"));
	}
	v.pb("1");
	v.pb("4");
	v.pb("9");
	sort(v.begin(), v.end(), cmp);
}

pii bp(int l, int r, const string& s){
	if(r-l < 2)	return mp(l, r);
	if(cmp(v[(l+r)/2], s))
		return bp((l+r)/2, r, s);
	else
		return bp(l, (l+r)/2, s);
}

inline int findL(const string& s){
	pii res = bp(0, v.size()-1, s);
	return (v[res.fi] == s) ? res.fi : res.se;
}

inline int findR(const string& s){
	pii res = bp(0, v.size()-1, s);
	return (v[res.se] == s) ? res.se : res.fi;
}

inline int ans(int l, int r){
	return r-l+1;
}

int main(){
	init();
    freopen("C-large1.in","r",stdin);
    freopen("C-large1.out","w",stdout);
    int T;
 	scanf("%d\n", &T);
 	string l, r;
 	for(int t=1;t<=T;t++){
		cin >> l >> r;
        printf("Case #%d: %d\n", t, ans(findL(l), findR(r)));		
	}
	return 0;
}
