#include<iostream>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<bitset>
using namespace std;

set<string> make_trie(const string& str){
	set<string> ret;
	for(int i=0; i<str.size(); i++)
		ret.insert(str.substr(0,i+1));
	ret.insert("");
	return ret;
}

typedef long long ll;

int T,N,M; // m<=8
string s[9];

const ll MOD = 1000000007;

int main(){

	freopen("D-small-attempt0.in","r",stdin);
	freopen("dout","w",stdout);

	cin>>T;
	for(int tc=1; tc<=T; tc++){
		cout<<"Case #"<<tc<<": ";

		cin>>M>>N;
		for(int i=0; i<M; i++) cin>>s[i];

		unsigned state=0;

		set<string> trie[9];
		for(int i=0; i<M; i++) trie[i] = make_trie(s[i]);

		ll cnt = 0;
		ll node = 0;

		for(;state<(1<<(M*2));state++){
			int x[8];
			for(int i=0; i<M; i++)
				x[i] = ( (state&(3<<(i*2))) >> (i*2));

			bool isValid = true;
			for(int i=0; i<M; i++){
				if(x[i]>=N) isValid = false;
			}

			if(isValid){
				set<string> server[4];
				for(int i=0; i<M; i++){
					server[x[i]].insert(trie[i].begin(), trie[i].end());
				}

				ll now = 0;
				for(int i=0; i<N; i++)
					now += server[i].size();

				if(now > node){
					node = now;
					cnt = 1;
				}
				else if(now == node)
					cnt++;
			}
		}

		cout << node << " " << cnt << endl;
	}
}