#include <bits/stdc++.h>



using namespace std;





#define fr(i,a,b) for(int i=a;i<b;++i)
typedef long long ll;
typedef pair<int,int> pii;
#define F first
#define S second
#define mp make_pair
const int oo = 0x3f3f3f3f;


int bit[1010];
int v[1010], v2[1010], vc[1010], vd[1010];
int vco[1010], vdo[1010];
int aux[1010];
int ond[1010];
int t,n;
int pc, pd;

int read(int pos){
	int ret = 0;
	for(int i = pos; i > 0; i -= (i&-i)){
		ret += bit[i];
	}
	return ret;
}

void up(int pos, int v){
	for(int i = pos; i <= 1001; i += (i&-i)){
		bit[i] += v;
	}
}



int cinv(int ar[], int tam){
	int ret = 0;
	memset(bit, 0, sizeof bit);
	fr(i,0,tam){
		ret += read(n)-read(ar[i]);
		up(ar[i],1);
	}
	return ret;
}
int dp[1010][1010];
int dp2[1010][1010];

int go(int a, int b){
	if(dp[a][b] != -1) return dp[a][b];
	if(a + b == n) return dp[a][b] = 0;
	dp[a][b] = oo;
	int el = a+b;
	int qtant = dp2[el][el-1], qtdep = (el-1)-dp2[el][el-1];
	int ps = ond[el] - 1;
	dp[a][b] = min(go(a+1,b) + ond[el]-a, go(a,b+1) + (n-1-b-ond[el]));
	printf("dp[%d][%d] = %d\n",a,b,dp[a][b]);
	return dp[a][b];
}


int main(){
	scanf("%d",&t);
	fr(cas,1,t+1){
		scanf("%d",&n);
		memset(dp, -1, sizeof dp);
		fr(i,0,n){
			scanf("%d",&v[i]);
			aux[i] = v[i];
		}
		sort(aux,aux+n);
		fr(i,0,n){
			v[i] = lower_bound(aux,aux+n,v[i])-aux;
			ond[v[i]] = i;
		}
		int pmai = 0;
		fr(i,0,n){
			if(v[i] == n) pmai = i;
		}
		fr(i,0,n){
			dp2[i][0] = (ond[0] < ond[i]);
			fr(j,1,n){
				dp2[i][j] = dp2[i][j-1] + (ond[j] < ond[i]);
			}
		}
		int p1 = 0, p2 = n-1;
		int ans = 0;
		fr(i,0,n){
			fr(j,0,n){
				ond[v[j]] = j;
			}
			if(abs(ond[i] - p1) < abs(ond[i] - p2)){
				for(int j = ond[i]-1; j >= p1; j--){
					ans++;
					swap(v[j],v[j+1]);
				}
				p1++;
			}
			else{
				fr(j,ond[i]+1,p2+1){
					ans++;
					swap(v[j],v[j-1]);
				}
				p2--;
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}


































