#include <bits/stdc++.h>

#define for1(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define for2(i,a,b) for(int (i)=(a)-1;(i)>=(b);(i)--)
#define for3(i,a,b,c) for(int (i)=(a);(i)<(b);(i)+=(c))
#define for4(i,a,b,c) for(int (i)=(a)-1;(i)>=(b);(i)-=(c))
#define debugv1(v) for1(_____,0,v.size()) cout<<(v)[_____]<<' '; cout<<endl;
#define debugv2(v,size) for1(_____,0,size) cout<<(v)[_____]<<' '; cout<<endl;
#define debugv3(v,s,e) for1(_____,s,e) cout<<(v)[_____]<<' '; cout<<endl;
#define debug1(a) cout<<(a)<<endl;
#define debug2(a,b) cout<<(a)<<' '<<(b)<<endl;
#define debug3(a,b,c) cout<<(a)<<' '<<(b)<<' '<<(c)<<endl;
#define debug4(a,b,c,d) cout<<(a)<<' '<<(b)<<' '<<(c)<<' '<<(d)<<endl;
#define debug5(a,b,c,d,e) cout<<(a)<<' '<<(b)<<' '<<(c)<<' '<<(d)<<' '<<(e)<<endl;

typedef long long ll;

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cout<<fixed;
	int t; cin>>t;
	for(int _t=1;_t<=t;_t++) {
		string s; cin>>s;
		deque<char> res;
		res.push_back(s[0]);
		for1(i,1,s.size()) {
			if (s[i]>=res[0]) res.push_front(s[i]); else res.push_back(s[i]);
		}
		cout<<"Case #"<<_t<<": ";
		for1(i,0,res.size()) cout<<res[i];
		cout<<endl;
	}
	return 0;
}