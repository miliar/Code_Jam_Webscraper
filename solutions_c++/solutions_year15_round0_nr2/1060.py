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
const int maxn = 1003;
int D, P[maxn];
inline void work(int T){
	int i, j, maxP = 0, ans = 0x7fffffff, cost;
	getd(D);
	for(i = 1;i <= D;++i)getd(P[i]), maxP = max(maxP, P[i]);
	for(i = maxP;i;--i){
		cost = 0;
		for(j = 1;j <= D;++j)cost += (P[j] - 1) / i;
		ans = min(ans, cost + i);
	}
	printf("Case #%d: %d\n", T, ans);
}

int main(){

#ifdef DEBUG
	freopen("test.txt", "r", stdin);
#elif !defined ONLINE_JUDGE
	//SetFile();
#endif
	int T, i;getd(T);
	for(i = 1;i <= T;++i)
		work(i);

#ifdef DEBUG
	printf("\n%lf sec \n", (double)clock() / CLOCKS_PER_SEC);
#endif
	return 0;
}

