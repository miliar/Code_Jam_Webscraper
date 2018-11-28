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

set<int> digit;

int main(){
	ios::sync_with_stdio(false); cin.tie(0);

	int T;
	long long int n;
	string number;

	cin>>T;

	rep(inst, 1, T+1){

		digit.clear();

		cin>>n;

		if(n == 0){
			cout<<"Case #"<<inst<<": INSOMNIA"<<endl;			
			continue;
		} 

		for(long long int i = 1; 1; i++){

			long long int x = n * i;

			number = to_string(x);

			rep(j, 0, SZ(number)){
				digit.insert(number[j] - '0');
			}


			if(SZ(digit) == 10){
				cout<<"Case #"<<inst<<": "<<x<<endl;
				break;
			}
		}

	}

	return 0;
}





















