#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> P;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define INF 2000000000
#define sz(x) ((int)(x).size())
#define fi first
#define sec second
#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define repn(i,a,n) for(int (i)=(a);(i)<(int)(n);(i)++)
#define EQ(a,b) (abs((a)-(b))<eps)
template<class T> void chmin(T& a,const T& b){if(a>b)a=b;}
template<class T> void chmax(T& a,const T& b){if(a<b)a=b;}
int pan[105],tmp[105];
void flip(int x){
	for(int i=0;i<x;i++)tmp[i]=pan[i];
	for(int i=0;i<x;i++)pan[x-i-1]=tmp[i]^1;
}
int solve(){
	string s;
	cin >> s;
	int N = sz(s);
	for(int i=0;i<N;i++)pan[i]=(s[i]=='+')?1:0;
	int ans = 0;
	for(int i=N-1;i>=0;i--){
		if(pan[i]==0){
			ans++;
			if(i>0&&pan[0]==1){
				for(int j=0;j<i;j++){
					if(pan[j]==0)break;
					pan[j]^=1;
				}
				ans++;
			}
			flip(i+1);
		}
	}
	return ans;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)printf("Case #%d: %d\n",i+1,solve());
	return 0;
}
