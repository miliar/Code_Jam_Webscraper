#include <cstdio>
#include <memory.h>

int N,M;
int lawn[105][105];
int mylawn[105][105];

bool cekujung() {
	bool bisa1 = true;
	bool bisa2 = true;
	
	for (int i = 0; i < N; i++)
		if (lawn[i][0] > lawn[0][0]) {
			bisa1 = false;
			break;
		}
	
	for (int i = 0; i < M; i++)
		if (lawn[0][i] > lawn[0][0]) {
			bisa2 = false;
			break;
		}
		
	if (bisa1) {
		for (int i = 0; i < N; i++)
			mylawn[i][0] = lawn[0][0];
	}
	if (bisa2) {
		for (int i = 0; i < M; i++)
			mylawn[0][i] = lawn[0][0];
	}
	
	if (!bisa1 && !bisa2 && (mylawn[0][0] != lawn[0][0]))
		return false;
	else
		return true;
}

bool cekatas() {
	for (int k = 1; k < M; k++) {
		bool bisa1 = true;
		
		for (int i = 0; i < N; i++)
			if (lawn[i][k] > lawn[0][k]) {
				bisa1 = false;
				break;
			}
		int maksi = 0;
		for (int i = 0; i < N; i++)
			if (lawn[i][k] > maksi)
				maksi = lawn[i][k];
		for (int i = 0; i < N; i++)
			if (mylawn[i][k] > maksi)
				mylawn[i][k] = maksi;
		if (bisa1) {
			for (int i = 0; i < N; i++)
				if (mylawn[i][k] > lawn[0][k])
					mylawn[i][k] = lawn[0][k];
		}
		
		if (!bisa1 && (mylawn[0][k] != lawn[0][k]))
			return false;
	}
	return true;
}

bool cekkiri() {
	for (int k = 1; k < N; k++) {
		bool bisa2 = true;
		
		for (int i = 0; i < M; i++)
			if (lawn[k][i] > lawn[k][0]) {
				bisa2 = false;
				break;
			}
		int maksi = 0;
		for (int i = 0; i < M; i++)
			if (lawn[k][i] > maksi)
				maksi = lawn[k][i];
		for (int i = 0; i < M; i++)
			if (mylawn[k][i] > maksi)
				mylawn[k][i] = maksi;
		if (bisa2) {
			for (int i = 0; i < M; i++)
				if (mylawn[k][i] > lawn[k][0])
					mylawn[k][i] = lawn[k][0];
		}
		if (!bisa2 && (mylawn[k][0] != lawn[k][0])) {
			return false;
		}
	}
	return true;
}

bool cekall() {
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (mylawn[i][j] != lawn[i][j])
				return false;
	return true;
}

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int num = 1; num <= T; num++)
	{
		scanf("%d %d",&N,&M);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				scanf("%d",&lawn[i][j]);
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				mylawn[i][j] = 100;
			}
		}
		
		if (!cekujung()) {
			printf("Case #%d: NO\n",num);
			continue;
		}
		
		if (!cekatas()) {
			printf("Case #%d: NO\n",num);
			continue;
		}
		
		if (!cekkiri()) {
			printf("Case #%d: NO\n",num);
			continue;
		}
		
		if (!cekall()) {
			printf("Case #%d: NO\n",num);
			continue;
		}
		
		printf("Case #%d: YES\n",num);
		continue;
	}
	return 0;
}
