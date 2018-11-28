#include <cstdio>
#include <cstdlib>
double min(double a, double b){
	return a > b ? b : a;
}
int main(){
    int t;
    //freopen("in", "r", stdin);
    //freopen("out", "w", stdout);
    scanf("%d", &t);
    for(int ct = 1;ct <= t; ct++){
        int t[5][5], s[5][5], x, y, cct[100] = {}, tct = 0, ans = 0;
        scanf("%d", &x);
        for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &s[i][j]);
		scanf("%d", &y);
        for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &t[i][j]);
		for(int i = 0; i < 4; i++)
			cct[s[x-1][i]]++, cct[t[y-1][i]]++;
		for(int i = 0; i < 100; i++)
			if(cct[i] == 2)
				tct++, ans = i;
		if(tct == 1)
			printf("Case #%d: %d\n", ct, ans);
		else if(tct > 1)
			printf("Case #%d: Bad magician!\n", ct);
		else
			printf("Case #%d: Volunteer cheated!\n", ct);
    }
    return 0;
}
