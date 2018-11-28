#include<iostream>
#include<cstdio>
#include<sstream>
#include<fstream>
#include<cctype>
#include<cstdlib>
#include<cmath>
#include<ctime>
#include<cstring>
#include<string>
#include<complex>
#include<bitset>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<queue>
#include<deque>
#include<stack>
#include<iomanip>
#include<utility>

#define pb push_back
#define pp pop_back
#define xx first
#define yy second
#define mp make_pair

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int maxn=200+10;
const double eps=1e-9;

double p[maxn],ans;
bool mark[maxn];
int n,k;
vi per;

double calc(){
	double ret=0;
	for(int mask=0;mask<(1<<k);mask++){
		double cur=1.;
		if(__builtin_popcount(mask)==k/2){
			for(int i=0;i<per.size();i++){
				if((mask&(1<<i))){
					cur*=p[per[i]];
				}
				else{
					cur*=(1.-p[per[i]]);
				}
			}
		}
		else cur=0;
		ret+=cur;
	}
	return ret;
}

void bt(int pos,int cnt){
	if(pos==n+1){
		if(cnt!=k)return;
		per.clear();
		for(int i=1;i<=n;i++)if(mark[i])per.pb(i);
		ans=max(ans,calc());
		return;
	}
	mark[pos]=true;
	bt(pos+1,cnt+1);
	mark[pos]=false;
	bt(pos+1,cnt);
}

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		cout<<"Case #"<<l<<": ";
		memset(mark,0,sizeof(mark));
		ans=0;
		cin>>n>>k;
		for(int i=1;i<=n;i++)cin>>p[i];
		bt(1,0);
		cout<<setprecision(10)<<fixed<<ans<<endl;
	}
	return 0;
}
