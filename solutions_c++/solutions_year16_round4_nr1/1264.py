#include<iostream>
#include<vector>
#include<string>
#define f first
#define s second
#define mp make_pair
using namespace std;

string weapon = "PSR";
string out[3] = {"PR", "PS", "RS"};

pair<pair<int, int>, int> getCount(int type, int N) {
	pair<pair<int, int>, int> ret = mp(mp(0, 0), 0);
	if(type == 0)
		ret.f.f = 1;
	else if(type == 1)
		ret.f.s = 1;
	else if(type == 2)
		ret.s = 1;
	
	for(int i=0;i<N;i++) {
		pair<pair<int, int>, int> next = mp(mp(ret.f.f + ret.f.s , ret.f.s + ret.s), ret.f.f + ret.s);
		ret = next;
	}
	
	return ret;
}


string expand(int basetype, int N) {
	string ret = string(1, weapon[basetype]);
	for(int i=0;i<N;i++) {
		string next(ret.size()*2, ' ');
		
		for(int j=0;j<(int)ret.size();j++){
			int type = weapon.find(ret[j]);
			
			next[2*j] = out[type][0];
			next[2*j+1] = out[type][1];
		}
		ret = next;
	}
	
	
	//Now the reordering
	for(int sz = 1; sz < (int)ret.size(); sz*=2) {
		string next;
		
		for(int i=0;i<(int)ret.size();i+=sz*2) {
			string s1 = ret.substr(i, sz);
			string s2 = ret.substr(i+sz, sz);
			
			if(s2 < s1)
				swap(s1, s2);
			next += s1;
			next += s2;
		}
		
		ret = next;
	}
	
	return ret;
}



int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		int N, R, P, S;
		cin >> N >> R >> P >> S;
		
		pair<pair<int, int>, int> desired = mp(mp(P, S), R);
		string ret="Z";
		
		for(int i=0;i<3;i++)
			if(getCount(i, N) == desired)
				ret = min(ret, expand(i, N) );
		
		cout << "Case #" << TCASE << ": ";
		if(ret == "Z")
			cout << "IMPOSSIBLE\n";
		else
			cout << ret << '\n';
	}
	
	return 0;
}






















































