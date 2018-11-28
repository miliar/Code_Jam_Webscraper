#include <bits/stdc++.h>
#define fr(a,b,c) for (int a = b; a < c; a++)
#define ms(a,b) memset((a), b, sizeof(a))
#define inf 0x3f3f3f3f
#define pb push_back
#define ll long long
#define MAXN 59

using namespace std;

int ri, rf;
int grid[20][20];
int grid1[20][20];

pair<set<int>::iterator , int> ret;

int main(){
	int casen = 1;
	int numc; scanf("%d", &numc);
	while(numc--){
		set<int> S;
		//printf("%d",S.size());
		//printf("A\n");
		scanf("%d", &ri);
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++){
				scanf("%d", &grid[i][j]);
				if (i == ri){
					//printf("%d ",grid[i][j]);
					S.insert(grid[i][j]);
				}
			}
		}
		//printf("\n");
		scanf("%d", &rf);
		int opa = 0;
		int res = 0;
		for (int i = 1; i <= 4; i++){
			for (int j = 1; j <= 4; j++){
				scanf("%d", &grid1[i][j]);
				if (i == rf){
					//printf("%d ",grid1[i][j]);
					ret = S.insert(grid1[i][j]);
					if (ret.second == false){
						res = grid1[i][j];
						opa++;
					}
				}
			}
		}
		if (opa == 0) printf("Case #%d: Volunteer cheated!\n", casen++);
		else if(opa == 1) printf("Case #%d: %d\n", casen++, res);
		else{
			printf("Case #%d: Bad magician!\n", casen++);
		}
	}
	return 0;
}