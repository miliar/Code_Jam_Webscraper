#include <iostream>
#include <cstdio> 
#include <algorithm>
#include <vector>
#include <cstring>
#define maxn 105
#define inf 0x3fffffff
using namespace std;

int a[5][5], b[5][5];
int ra, rb;

int f[20];

void solve(){
	memset(f, 0, sizeof(f));
	for (int i = 0; i < 4; i++)
		f[a[ra][i]] = 1;
	int ans = -1;
	for (int i = 0; i < 4; i++){
		int tmp = b[rb][i];
		if (f[tmp]){
			if (ans != -1){
				printf("Bad magician!\n");
				return;
			}else ans = tmp;
		}
	}
	if (ans == -1) printf("Volunteer cheated!\n");		
	else printf("%d\n", ans);
}


int main(){
	freopen("A-small-attempt0.in","r",stdin); 
	freopen("out.txt","w",stdout); 
	int T;
	cin >> T;
	int cas = 1;
	while (T--){
		scanf("%d", &ra);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &a[i][j]);
		ra--;
		scanf("%d", &rb);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				scanf("%d", &b[i][j]);
		rb--;
		printf("Case #%d: ", cas++);
		solve();
	}
}