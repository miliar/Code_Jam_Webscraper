#include<stdio.h>
#include<string.h>
using namespace std;
#define M 222
char s[M][M];
int sr[M][M];
int sc[M][M];
int ans;
int T;
main(){
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&T);
	int nT = 0;
	while(T > 0){
		memset(sr , 0 , sizeof sr);
		memset(sc , 0 , sizeof sc);
		ans = 0;
		int r,c;
		scanf("%d %d",&r,&c);
		for(int i = 0 ; i < r ; i++)	scanf("%s",&s[i]);
		for(int i = 1 ; i <= r ; i++)
			for(int j = 1 ; j <= c ; j++)
				sr[i][j] = sr[i][j - 1] + (s[i - 1][j - 1] != '.');
		for(int i = 1 ; i <= c ; i++)
			for(int j = 1 ; j <= r ; j++)
				sc[j][i] = sc[j - 1][i] + (s[j - 1][i - 1] != '.');
		bool ok = true;
		for(int i = 1 ; i <= r ; i++){
			if( !ok ) break;
			for(int j = 1 ; j <= c ; j++){
				if(s[i - 1][j - 1] == '.') continue;
				if(sr[i][c] == 1 && sc[r][j] == 1){
					ok = false;
					break;
				}
				ans++;
				if(s[i - 1][j - 1] == '>' && sr[i][c] - sr[i][j] >= 1) ans--;
				if(s[i - 1][j - 1] == '<' && sr[i][j - 1] >= 1) ans--;
				if(s[i - 1][j - 1] == '^' && sc[i - 1][j] >= 1) ans--;
				if(s[i - 1][j - 1] == 'v' && sc[r][j] - sc[i][j] >= 1) ans--;
			}
		}
		nT++;
		printf("Case #%d: ",nT);
		if(!ok) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
		T--;
	}
}
