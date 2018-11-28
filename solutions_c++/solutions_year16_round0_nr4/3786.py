#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define F first
#define S second
#define rep(i, a, b) for(int i=a;i<b;++i)
#define SZ(x) ((int)(x).size())

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;

template<typename TH>
void debug_vars(const char* data, TH head){
	cerr << data << "=" << head << "\n";
}

template<typename TH, typename... TA>
void debug_vars(const char* data, TH head, TA... tail){
	while(*data != ',') cerr << *data++;
	cerr << "=" << head << ",";
	debug_vars(data+1, tail...);
}

int main(){
	ios::sync_with_stdio(false); cin.tie(0);

	int T;
	long long int k, c, s;

	cin>>T;

	rep(inst, 0, T){
		cin>>k>>c>>s;

		long long int block = pow(k, c-1);

		cout<<"Case #"<< inst + 1 <<": ";
		rep(i, 0, s){
			cout<<i*block + 1<<" ";
		}
		cout<<endl;
	}

	return 0;
}





















