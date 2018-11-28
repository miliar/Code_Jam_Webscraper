//joyneel
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	LL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))

#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

//#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
	cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
	const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
string d[10];
int cnt[10][26];
int c[26];
VI v,vv;
string s;
void solve(){
	if(!vv.empty()){
		return;
	}
	int tp = 1;
	for(int i=0;i<26;i++){
		if(c[i]>0){
			tp = 0;
			break;
		}
	}
	if(tp and vv.empty()){
	   	vv = v;
		return;
	}
	for(int i=0;i<10;i++){
		if(!vv.empty()) return;
		int fl = 1;
		for(int j=0;j<26;j++){
			if(cnt[i][j]>c[j]){
				fl = 0;
				break;
			}
		}
		trace(i,fl);
		if(fl){
			v.PB(i);
			for(int j=0;j<26;j++){
				c[j] -= cnt[i][j];
			}
			solve();
			for(int j=0;j<26;j++){
				c[j] += cnt[i][j];
			}
			v.pop_back();
		}
	}
}

int main(){
	d[0] = "ZERO";
	d[1] = "ONE";
	d[2] = "TWO";
	d[3] = "THREE";
	d[4] = "FOUR";
	d[5] = "FIVE";
	d[6] = "SIX";
	d[7] = "SEVEN";
	d[8] = "EIGHT";
	d[9] = "NINE";
	for(int i=0;i<10;i++){
		for(int j=0;j<SZ(d[i]);j++){
			cnt[i][d[i][j]-'A']++;
		}
	}
	int n;
	si(n);
	for(int t=1;t<=n;t++){
		trace(t);
		v.clear();
		vv.clear();
		SET(c,0);
		cin>>s;
		for(int i=0;i<SZ(s);i++){
			c[s[i]-'A']++;
		}
		solve();
		sort(ALL(vv));
		printf("Case #%d: ",t);
		for(int i=0;i<SZ(vv);i++){
		   	cout<<vv[i];
		}
		cout<<endl;
	}
	return 0;
}
