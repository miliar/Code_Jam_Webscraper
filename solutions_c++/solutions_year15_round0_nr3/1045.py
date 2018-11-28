/***********************************************************************/
/**********************By Asm.Def-Wu Jiaxin*****************************/
/***********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <algorithm>
using namespace std;
#define SetFile(x) ( freopen(#x".in", "r", stdin), freopen(#x".out", "w", stdout) );
#define getc() getchar() 
template<class T>inline void getd(T &x){
	char ch = getc();bool neg = false;
	while(!isdigit(ch) && ch != '-')ch = getc();
	if(ch == '-')ch = getc(), neg = true;
	x = ch - '0';
	while(isdigit(ch = getc()))x = x * 10 - '0' + ch;
	if(neg)x = -x;
}
/***********************************************************************/
const int maxn = 10003;
typedef long long LL;
const LL maxl = 0x7fffffffffffffffll;
int mul[8][8] = {{0,1,2,3},{1,4,3,6},{2,7,4,1},{3,2,5,4}};
inline int f(int ch){
	switch(ch){
		case '1':return 0;
		case 'i':return 1;
		case 'j':return 2;
		default:return 3;
	}
}

inline void init(){
	int i, j;
	for(i = 0;i < 4;++i)for(j = 4;j < 8;++j)mul[i][j] = (mul[i][j - 4] + 4) & 7;
	for(i = 4;i < 8;++i)for(j = 0;j < 8;++j)mul[i][j] = (mul[i - 4][j] + 4) & 7;
}

int str[maxn], trv[8][maxn];

inline int power(int a, LL N){
	int ans = 0;
	while(N){if(N & 1)ans = mul[ans][a];a = mul[a][a];N >>= 1;}
	return ans;
}

inline void work(){
	LL L, X;getd(L), getd(X);
	int ch, i, j, t, segS = 0;
	for(i = 1;i <= L;++i){
		ch = getchar();while(ch != '1' && !isalpha(ch))ch = getchar();
		str[i] = f(ch);
		segS = mul[segS][str[i]];
	}
	if(power(segS, X) != 4){
		printf("NO\n");
		return;
	}
	segS = 1;
	for(j = 0;j < 8;++j)
		for(i = 1,segS = j;i <= L;++i)segS = trv[j][i] = mul[segS][str[i]];
	bool vis[8] = {0}, knownl = false, knownr = false;
	for(j = 0, t = 0;!vis[j] && t < X && !knownl;j = trv[j][L], ++t){
		vis[j] = true;
		for(i = 1;i <= L;++i)if(trv[j][i] == 1){
			knownl = true;
			for(int k = i + 1;k <= L;++k)if(trv[j][k] == 3){
				knownr = true;
				break;
			}
			break;
		}
	}
	if(!knownl){printf("NO\n");return;}
	memset(vis, 0, sizeof(vis));
	for(;!vis[j] && t < X && !knownr;j = trv[j][L], ++t){
		vis[j] = true;
		for(i = 1;i <= L;++i)if(trv[j][i] == 3){
			knownr = true;
			break;
		}
	}
	if(!knownr)printf("NO\n");
	else printf("YES\n");
}
int main(){

#ifdef DEBUG
	freopen("test.txt", "r", stdin);
#elif !defined ONLINE_JUDGE
	//SetFile();
#endif
	int T, i;getd(T);
	init();
	for(i = 1;i <= T;++i){
		printf("Case #%d: ", i);
		work();
	}

#ifdef DEBUG
	printf("\n%lf sec \n", (double)clock() / CLOCKS_PER_SEC);
#endif
	return 0;
}

