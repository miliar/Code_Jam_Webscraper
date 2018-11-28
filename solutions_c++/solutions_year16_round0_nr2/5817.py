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
	stack<int> P;
	string N;
	int answer;

	cin>>T;

	rep(inst, 0, T){
		cin>>N;
		answer = 0;

		while(!P.empty()) P.pop();

		rep(i, 0, SZ(N)){
			P.push( (N[i] == '+' ? 1 : 0) ); 
		}

		//cout<<N<<endl;

		while(!P.empty()){
			if((P.top() + answer)% 2 == 1){
				P.pop();
			}else{
				answer++;
				P.pop();
			}
		}	

		cout<<"Case #"<<inst+1<<": "<<answer<<endl;
	}

	return 0;
}





















