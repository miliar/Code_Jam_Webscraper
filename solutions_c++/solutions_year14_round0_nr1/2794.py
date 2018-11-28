#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cstring>
#include <cmath>
#include <set>
#define maxl 1000000000
#define mod 1000000007
#define maxn 5010
#define maxs 150
using namespace std;

int v[100];
void solve(){
	for(int i = 1; i <= 16; ++i) v[i] = 0;
	for(int k = 0; k <= 1; ++k){
		int id1;
		scanf("%d",&id1);
		for(int i = 1; i <= 4; ++i)
			for(int j = 1; j <= 4; ++j){
				int x;
				scanf("%d", &x);
				if(id1 == i) ++v[x];
			}
	}
	int ans = -1;
	for(int i = 1; i <= 16; ++i) if(v[i] == 2){
		if(ans != -1){
			printf("Bad magician!\n");
			return;
		}
		ans = i;
	}
	if(ans == -1){
		printf("Volunteer cheated!\n");
		return;
	}
	printf("%d\n", ans);
	
}


int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}

}