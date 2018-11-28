#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<cstring>
#include<cctype>
#include<complex>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<functional>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<bitset>
using namespace std;
const int dx[] = {-1,0,1,0};
const int dy[] = {0,-1,0,1};
#define INF 1e+8
#define EPS 1e-10
#define PB push_back
#define fi first
#define se second
#define ll long long 
#define reps(i,j,k) for(int i = (j); i < (k); i++)
#define rep(i,j) reps(i,0,j)
typedef pair<int,int> Pii;
typedef vector<int> vi;
int main(){
	int T;
	scanf("%d",&T);
	rep(t,T){
		bool f[20]={0};
		int a;
		int a_[5][5]={{0}};
		int cnt = 0;
		int ans = -1;
		scanf("%d",&a);
		rep(i,4){
			rep(j,4){
				scanf("%d",&a_[i][j]);
				if(i == a-1)f[a_[i][j]] = 1;
			}
		}
		int b;
		int b_[5][5]={{0}};
		scanf("%d",&b);
		rep(i,4){
			rep(j,4){
				scanf("%d",&b_[i][j]);
				if(i == b-1){
					if(f[b_[i][j]]){
						f[b_[i][j]] = 0;
						ans = b_[i][j];
						cnt++;
					}
				}
			}
		}
		if(cnt == 0){
			printf("Case #%d: Volunteer cheated!\n",t+1);
		}
		else if(cnt == 1){
			printf("Case #%d: %d\n",t+1,ans);
		}
		else{
			printf("Case #%d: Bad magician!\n",t+1);
		}
	}
	return 0;
}