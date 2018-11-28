#include <bits/stdc++.h>
 
using namespace std;
 
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))
 
#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;

int main(){
	int ite;
	cin>>ite;
	int cc=1;
	while(ite--){
		cout<<"Case #"<<cc++<<": ";
		int n;
		cin>>n;
		string s;
		cin>>s;
		int cou=s[0]-'0';
		int ans=0;
		for(int i=1;i<s.length();i++){
			int p = s[i]-'0';
			if(cou<i){
				ans+= i-cou;
				cou+= i-cou;
			}
			cou+=p;
		}
		cout<<ans<<endl;
	}
}