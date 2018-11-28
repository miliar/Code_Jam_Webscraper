#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>

#define REP(a,b) for (int a = 0; a < b; a++)
#define FOR(a,b,c) for (int a = b; a <= c; a++)
#define RESET(a,b) memset(a,b,sizeof a)

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define PII pair<int,int>
#define INF 2123123123

#define LL long long
using namespace std;

int T;
int ar[5][5];
int a;

void read(int &mask){
	scanf("%d", &a);
	a--;
	REP(i,4){
		REP(j,4){
			scanf("%d", &ar[i][j]);
		}
	}
	
	mask = 0;	
	REP(i,4){
		mask |= (1 << ar[a][i]);
	}
}

int bpc(int a){
	if (a == 0) return 0;
	return 1 + bpc(a & (a-1));
}

int main(){		
	scanf("%d", &T);
	REP(jt,T){
		int mask1, mask2;

		read(mask1);
		read(mask2);
		
		int un = mask1 & mask2;
		int bc = bpc(un);		
		
		printf("Case #%d: ", jt+1);
		if (bc == 1){
			int ans = 0;
			while (un > 1){
				ans++;
				un = un >> 1;
			}
			printf("%d\n", ans);
		}else if (bc == 0){
			printf("Volunteer cheated!\n");
		}else{
			printf("Bad magician!\n");
		}
	}
	return 0;
}
