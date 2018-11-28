#include <cstdio>
using namespace std;

int lawn[101][101];
int n,m;

bool check(int a, int b){
	bool result = true;
	for (int i=0; i<n; i++){
		if (lawn[i][b]>lawn[a][b]){
			result = false;
			break;
		}
	}
	if (result) return true;
	result = true;
	for (int i=0; i<m; i++){
		if (lawn[a][i]>lawn[a][b]){
			result = false;
			break;
		}
	}
	return result;
}

int main(){
	int z;
	scanf("%d", &z);
	for (int q=1; q<=z; q++){
		printf("Case #%d: ", q);
		bool yesYouCan = true;
		scanf("%d %d", &n, &m);
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				scanf("%d", &lawn[i][j]);
		for (int i=0; i<n; i++){
			for (int j=0; j<m; j++){
				if (!check(i,j)){
					yesYouCan = false;
					break;
				}
			if (!yesYouCan) break;
			}
		}
		if (yesYouCan) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
