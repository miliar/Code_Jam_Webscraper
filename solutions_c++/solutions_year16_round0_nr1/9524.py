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
bool used[12];
int cnt;
void apply(int x){
	while(x){
		int dig = x%10;
		if(!used[dig]){
			used[dig]=true;
			cnt++;
		}
		x/=10;
	}
}
int solve(int N){
	memset(used,false,sizeof(used));
	cnt = 0;
	for(int i=1;;i++){
		apply(N*i);
		if(cnt==10)return N*i;
	}
}
int main(){
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		int N;
		scanf("%d",&N);
		if(N==0)printf("Case #%d: INSOMNIA\n",i+1);
		else printf("Case #%d: %d\n",i+1,solve(N));
	}
	return 0;
}
