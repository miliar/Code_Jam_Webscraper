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
int maxn = 1003;
inline void work(int T){
	int i, N, S = 0, ans = 0, t;
	getd(N);
	for(i = 0;i <= N;++i){
		while(!isdigit(t = getchar()));t -= '0';
		if(i <= S)S += t;
		else ans += i - S, S = i + t;
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

