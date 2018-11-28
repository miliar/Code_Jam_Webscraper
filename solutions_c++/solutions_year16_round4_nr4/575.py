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


int n,ans;
char mat[5][5];
bool mark[5][5];
int f[5]={1,1,2,6,24};

bool check(int mask){
	bool ret=true;
	for(int i=0;i<n*n;i++){
		if((mask&(1<<i))){
			int x=i/n;
			int y=i%n;
			if(mat[x][y]=='1')ret=false;
		}
	}
	return ret;
}
void update(int mask){
	memset(mark,0,sizeof(mark));
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(mat[i][j]=='1'){
				mark[i][j]=true;
			}
			int bit=i*n+j;
			if((mask&(1<<bit))){
				mark[i][j]=true;
			}
		}
	}
}
bool ok(){
	vi per,mac;
	per.clear();
	mac.clear();
	for(int i=0;i<n;i++){
		per.pb(i);
		mac.pb(i);
	}
	for(int i=0;i<f[n];i++){
		for(int j=0;j<f[n];j++){
			bool is[4];
			memset(is,0,sizeof(is));
			for(int k=0;k<n;k++){
				bool find=false;
				for(int d=0;d<n;d++){
					if(mark[per[k]][d] && !is[d]){
						find=true;
						break;
					}
				}
				if(!find)return false;
				if(!mark[per[k]][mac[k]])break;
				is[mac[k]]=true;
			}
			next_permutation(mac.begin(),mac.end());
		}
		next_permutation(per.begin(),per.end());
	}
	return true;
}
int main(){
	ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		cout<<"Case #"<<l<<": ";
		ans=1e9;
		cin>>n;
		for(int i=0;i<n;i++)for(int j=0;j<n;j++)cin>>mat[i][j];
		for(int mask=0;mask<(1<<(n*n));mask++){
			if(check(mask)){
				update(mask);
				if(ok()){
					ans=min(ans,__builtin_popcount(mask));
				}
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
