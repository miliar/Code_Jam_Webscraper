#include <cstdio>
#include <cstdlib>
#include <map>
#include <cstring>
#include <algorithm>
#define mk make_pair
#define MAXN 10010
using namespace std;

char S[MAXN];
int back[10];
int main(){
	back[1] = 0;
	back[2] = 1;
	back[3] = 2;
	back[5] = 3;
	int mp[] = {2, 3, 5, 1};
	int mul[][4] = { { 1, 2, 3, 5},
					 { 2,-1, 5,-3},
					 { 3,-5,-1, 2},
					 { 5, 3,-2,-1}};
	int L, X;
	int t;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d\n", &t);
	for (int tt = 1; tt<=t; tt++){
	scanf("%d %d\n", &L, &X);
	gets(S);
	int n = strlen(S);
	int len = L *X;
	int pr = 1, tmp, sgn = 1, cur = 1;
	for (int i = 0; i<len; i++){
		if (S[i%n] == '1') tmp = 1;
		else tmp = back[mp[S[i%n] - 'i']];
		//printf("tmp = %d\n", tmp);
		pr = mul[back[pr]][tmp];
		if (pr < 0) {
			sgn *= -1;
			pr = -pr;
		}
		if (back[pr] == cur) {
			//printf("Done with %c \n", (cur-1) + 'i');
			cur++;
			pr = 1;
		}
		//printf("%d %d \n", pr, sgn);
	}
	printf("Case #%d: ", tt);
	if (pr == 1 && sgn == 1 && cur == 4) printf("YES\n");
	else printf("NO\n");
	}
	return 0;
}
		
		
	
