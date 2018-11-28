#include <cstdio>
using namespace std;
#define bad 0
#define cheat 17

int main(){
	int f, s, fa[5][5], sa[5][5], ans, cases;
	scanf("%d", &cases);
	for(int ca=1;ca<=cases;++ca){
		scanf("%d", &f);
		for(int i=1;i<=4;++i)
			for(int j=1;j<=4;++j)
				scanf("%d", &fa[i][j]);
		scanf("%d", &s);
		for(int i=1;i<=4;++i)
			for(int j=1;j<=4;++j)
				scanf("%d", &sa[i][j]);
		for(int i=1,count=0;i<=4;++i){
			for(int j=1;j<=4;++j){
				if(fa[f][i]==sa[s][j]){
					++count;
					if(count==1)
						ans = fa[f][i];
					else{
						ans = bad;
						i = 5;
						break;
					}
				}
			}
			if(i==4 && count==0)
				ans = cheat;
		}
		printf("Case #%d: ", ca);
		if(ans==bad)
			puts("Bad magician!");
		else if(ans==cheat)
			puts("Volunteer cheated!");
		else
			printf("%d\n", ans);
	}
}
