#include <bits/stdc++.h>
#define fr(i,a,b) for(int i = (a); i < (b); ++i)
#define pb push_back
#define eps 1e-7

using namespace std;
typedef long long ll;

int mat1[5][5], mat2[5][5], mark[20], passo;

int main(){
	int t, caso = 1, p, s;
	scanf("%d", &t);
	
	while(t--){
		scanf("%d", &p);
		fr(i, 0, 4) fr(j, 0, 4) scanf("%d", &mat1[i][j]);
		scanf("%d", &s);
		fr(i, 0, 4) fr(j, 0, 4) scanf("%d", &mat2[i][j]);
		
		passo++;
		
		fr(i, 0, 4) mark[mat1[p-1][i]] = passo;
		int cont = 0, ans;
		fr(i, 0, 4){
			if(mark[mat2[s-1][i]] == passo){
				cont++;
				ans = mat2[s-1][i];
			}
		}
		
		if(cont == 0){
			printf("Case #%d: Volunteer cheated!\n", caso++);
		}else if(cont == 1){
			printf("Case #%d: %d\n", caso++, ans);
		}else{
			printf("Case #%d: Bad magician!\n", caso++);
		}
	}

	return 0;
}

