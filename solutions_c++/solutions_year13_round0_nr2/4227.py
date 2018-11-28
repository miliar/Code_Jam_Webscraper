#include<cstdio>
#include<cstdlib>
#include<cmath>
//#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<cstring>

#define fr(i,j,k) for(int (i)=(j);(i)<(k);++(i))
#define cl(i) memset(i,0,sizeof(i))
#define F first
#define S second
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define PI acos(-1)
#define db(x) cerr << #x << " = " << x << endl;
#define _ << ", " << 
#define ll long long
#define PI acos(-1)
#define EPS 1e-9

using namespace std;

int in[111][111];
int pd[111][111];

int main(){
	
	int t; scanf("%d", &t); int caso =1;
	while(t--){
		int n, m;
		scanf("%d%d", &n ,&m );
		cl(in); cl(pd);
		
		fr(i,0,n) fr(j,0,m){
			scanf("%d", &in[i][j]);
		}
		fr(i,0,n){
			int maior = 0;
			fr(j,0,m){
				maior = max( maior, in[i][j]);
			}
			fr(j,0,m){
				if( in[i][j] < maior ) pd[i][j]++;
			}
		}
		fr(i,0,m){
			int maior = 0;
			fr(j,0,n){
				maior = max( maior, in[j][i]);
			}
			fr(j,0,n){
				if( in[j][i] < maior ) pd[j][i]++;
			}
		}
		bool bug = false;
		fr(i,0,n)fr(j,0,m) if(pd[i][j] > 1) { bug = true; break; }
		printf("Case #%d: %s\n", caso++, (bug)?"NO":"YES");
	}
	return 0;
	
}