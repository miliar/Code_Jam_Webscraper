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

string st[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int ar[26], ans[10];
string sts;
int rec(int i){
	if(i>9) return 0;
	int ppp=0;
	for(int j=0;j<26;j++){
		if(ar[j]!=0)ppp=1;
	}
	if(ppp==0){
		for(int j=0;j<10;j++) while(ans[j]--) cout<<j;
			return 1;
	}
	int p[26]={0};
	for(int j=0;j<st[i].length();j++) p[st[i][j]-'A']++;
	int mini = 9999;
	for(int j=0;j<26;j++){
		if(p[j]>0){
			mini = min(mini, ar[j]/p[j]);
		}
	}
	if(rec(i+1))return 1;
	if(mini>0){
		for(int j=0;j<26;j++){
			ar[j]-=p[j];
		}
		ans[i]+=1;
		if(rec(i)) return 1;
		for(int j=0;j<26;j++){
			ar[j]+=p[j];
		}
		ans[i]-=1;
	}
	return 0;
}
int main(){
	int ite;
	cin>>ite;
	int co=1;
	while(ite--){
		memset(ar,0,sizeof(ar));
		memset(ans,0,sizeof(ans));
		cout<<"Case #"<<co++<<": ";
		string s;
		cin>>s;
		for(int i=0;i<s.length();i++){
			ar[s[i]-'A']+=1;
		}
		rec(0);
		cout<<endl;
		}
}
