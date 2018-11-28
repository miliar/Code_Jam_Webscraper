#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <assert.h>
#include <bitset>

using namespace std;
#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 0x3f3f3f3f
#define ll long long
#define mod 10
#define B 33
#define MAX (int)10e6

typedef vector<int> vi;
typedef pair<int,int>ii;
typedef vector<ii> vii;
typedef unsigned long long hash;

int n,m,t;
int matrix[500][500];
int dp[500][2];

int main (int argc,char *argv[]){
	scanf("%d",&t);
	int cases = 0;
	while(t--){
		cases++;
		scanf("%d%d",&n,&m);
		int menor = INF;
		for(int i=0; i<n; ++i)
			for(int j=0; j<m; ++j)
				scanf("%d",&matrix[i][j]);
		printf("Case #%d: ",cases);
		int ok = 1;
		for(int i=0; i<n; ++i){
			for(int j=0; j<m; ++j){
				//checa linha
				int p = matrix[i][j];
				// printf("p:%d (%d,%d)\n",p,i,j);
				for(int k =0; k<m; ++k){
					if(matrix[i][k] > p){
						ok = 0;
						break;
					}
				}
				// printf("linha? %d\n",ok);
				if(!ok){
					ok = 1;
					//checa coluna
					for(int k =0; k<n; ++k){
						if(matrix[k][j] > p){
							ok = 0;
							break;
						}
					}
				}
				// printf("col? %d\n",ok);
				if(!ok) break;
			}

			if(!ok) break;
		}
		if(ok) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
