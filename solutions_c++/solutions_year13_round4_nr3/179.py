#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<string.h>
#include<set>
#include<map>
using namespace std;

typedef long long Int;
#define FOR(i,a,b)  for(int i=(a);i<=(b);++i)
#define sz(s) (int)(s).size()
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
void assert(bool x){if(!x)throw -1;}
const int inf = 1000000000;
const int MOD = 1000002013;
const double pi = acos(-1.0);
const Int INF = inf*(Int)inf;

const int N = 21;
int a[N+1],b[N+1];
bool used[N+1];
bool found;
int n;
vector<int> ans;
bool have[N+1];

void Run(int id){
	if(id==n+1){
		for(int i=1;i<=n;++i){
			bool goodb=(b[i]==1);
			for(int j=i+1;j<=n;++j)if(ans[i]>ans[j] && b[i]==b[j]+1)goodb=true;
			if(!goodb)return;
		}
		found=true;
	}
	
	if(have[id]){Run(id+1);return;}
	if(found)return;

	for(int val=1;val<=n;++val)if(!used[val]){
		if(val>=a[id] && val>=b[id]){
			if(found)return;
			ans[id]=val;
			bool valid = true;
			bool gooda=(a[id]==1);
			for(int j=1;j<id;++j){
				if(ans[id]>ans[j] && a[id]<a[j]+1)valid=false;
				if(ans[id]>ans[j] && a[id]==a[j]+1)gooda=true;
				if(ans[id]<ans[j] && b[j]<b[id]+1)valid=false;
			}
			if(!gooda)valid=false;

			if(valid){
				used[val]=true;
				Run(id+1);
				used[val]=false;
			}
		}
	}
}

vector<int> solve(){
	cin>>n;
	FOR(i,1,n)cin>>a[i];
	FOR(i,1,n)cin>>b[i];
	ans.resize(n+1);
	found=false;
	memset(have,false,sizeof(have));
	memset(used,false,sizeof(used));
	int val=1;
	for(int i=n;i>=1;--i)if(a[i]==1){
		have[i]=true;
		ans[i]=val;
		used[val]=true;
		val++;
	}
	Run(1);
	if(!found)cerr<<"FAILED"<<endl;
	return ans;
}


int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","wb",stdout);
	int tests;
	scanf("%d\n",&tests);
	for(int test_id=1;test_id<=tests;++test_id){
		vector<int> ans = solve();
		cout<<"Case #"<<test_id<<": ";
		FOR(i,1,sz(ans)-1)cout<<ans[i]<<" ";cout<<endl;
		cerr<<"found "<<test_id<<endl;
	}
}  