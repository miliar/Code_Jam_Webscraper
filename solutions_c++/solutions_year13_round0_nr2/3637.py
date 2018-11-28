//GCJ Lawnmower
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <cmath>
#include <cassert>

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i=x; i<y; i++)
#define FOR(it,A) for(typeof A.begin(); it!=A.end(); it++)
#define quad(x) (x)*(x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second

typedef long long ll;
typedef pair<int,int> pii;

int mx[110][110];

int main(){
	int t, n, m, cont, flag;
	scanf("%d",&t);
	f(i,1,t+1){
		scanf("%d %d",&n, &m);
		f(p,0,n){
			f(q,0,m){
				scanf("%d",&mx[p][q]);
			}
		}
		
		//test
		printf("Case #%d: ",i);
		flag = 0;
		f(p,0,n){
			f(q,0,m){
				cont = 0;
				f(x,0,n){
					if(mx[x][q]>mx[p][q] && x!= p){
						cont++;
						break;
					}
				}
				f(y,0,m){
					if(mx[p][y]>mx[p][q] && y!=q){
						cont++;
						break;
					}
				}
				if(cont>1){
					flag = 1;
					break;
				}
			}
			if(flag)
				break;
		}
		if(flag){
			printf("NO\n");
		}else{
			printf("YES\n");
		}

	}
	return 0;
}
