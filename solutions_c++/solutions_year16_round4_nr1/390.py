#include<bits/stdc++.h>
using namespace std;

#define int long long
typedef pair<int,int>pint;
typedef vector<int>vint;
typedef vector<pint>vpint;
#define pb push_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define all(v) (v).begin(),(v).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
template<class T,class U>inline void chmin(T &t,U f){if(t>f)t=f;}
template<class T,class U>inline void chmax(T &t,U f){if(t<f)t=f;}

//G,C,P=0,1,2

int dp[20][3][3];
string str[20][3];
string lis="RSP";

void solve(int Case){
	cout<<"Case #"<<Case+1<<": ";

	int N,H[3];
	cin>>N;
	cin>>H[0]>>H[2]>>H[1];

	string ans=string(1,'Z'+1);
	for(int i=0;i<3;i++){
		bool ok=true;
		for(int j=0;j<3;j++)if(dp[N][i][j]!=H[j])ok=false;
		if(ok)chmin(ans,str[N][i]);
	}

	if(ans[0]=='R'||ans[0]=='S'||ans[0]=='P')cout<<ans<<endl;
	else cout<<"IMPOSSIBLE"<<endl;
}

signed main(){
	for(int i=0;i<=12;i++){
		for(int j=0;j<3;j++){
			dp[i][j][j]=1;
			str[i][j]=string(1,'Z'+1);
			for(int k=0;k<i;k++){
				for(int l=0;l<3;l++)dp[i][j][l]+=dp[k][(j+1)%3][l];
			}

			for(int b=0;b<1<<i;b++){
				string t=string(1,lis[j]);
				for(int k=0;k<i;k++){
					if(b>>k&1){
						t=str[k][(j+1)%3]+t;
					}
					else{
						t+=str[k][(j+1)%3];
					}
				}
				chmin(str[i][j],t);
			}
		}

	}

	int T;
	cin>>T;
	rep(i,T)solve(i);
    return 0;
}
