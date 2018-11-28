#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<queue>
#include<ctime>
using namespace std;
typedef long long ll;
bool used[1000000];
ll pri[1000000];
int n_pri;
void init () {
	n_pri = 0;
	for(ll i=2;i<1e6;++i) {
		if(!used[i])
			pri[n_pri++] = i;
		for(ll j=0; j<n_pri&& i*pri[j]<1e6;++j){
			used[i*pri[j]] = 1;
			if(!(i%pri[j]))
				break;
		}
	}
}
void pout(ll num) {
	vector<int> v;
	while(num){
		if(num&1)
		v.push_back(1);
		else
		v.push_back(0);
		num>>=1;
	}
	for(int i=v.size()-1 ;i>=0;--i)
		cout<<v[i];
}
ll isPri(ll num, int base, ll p) {
	ll m = 1;
	ll tmp = 0;
	while(num) {
		if(num & 1) {
			tmp += m;
			tmp %=p;
		}
		m*=base;
		m%=p;
		num>>=1;
	}
	return tmp;
}
void deal() {
	init();
	int n, j;
	cin>>n>>j;
	srand(time(0));
	ll randPart = 1<<(n-2);
	ll otherPart = 1 + (1<<(n-1));
	vector<int> ans;
	while(j) {
		ll r1 = rand();
		ll r2 = rand();
		ll tmp = ((((r1<<16) + r2)%randPart)<<1) + otherPart;
		bool showed = false;
		for(int i=0;i<ans.size();++i){
			if(ans[i]==tmp) {
				showed = true;
				break;
			}
		}
		if(showed)
			continue;
		ll ps[9];
		bool isans = true;
		for(int i=2; i<=10; ++i) {
			bool isp = true;
			for (int j=0; j<n_pri && pri[j]<tmp; ++j) {
				if(!isPri(tmp, i, pri[j])) {
					isp = false;
					ps[i-2] = pri[j];
					break;
				}	
			}
			if(isp) {
				isans = false;
			}
		}
		if(isans) {
			pout(tmp);
			for(int i=0;i<9;++i)
				cout<<" "<<ps[i];
			cout<<endl;
			ans.push_back(tmp);
			--j;
		}
	}
}
void openFile() {
	freopen("C-small-attempt0.out","w", stdout);
	freopen("C-small-attempt0.in","r",stdin);
}
int main() {
	int t;
	openFile(); 
	cin>>t;
	for(int i=0;i<t;++i) {
		cout<<"Case #"<<i+1<<": "<<endl;
		deal();
	}
}