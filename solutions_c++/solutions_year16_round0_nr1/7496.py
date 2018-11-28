#include <bits/stdc++.h>
using namespace std;

// Macro Tools /////////////////////////////////////////////////////////////////
#define GET_MACRO_09(A0, A1, A2, A3, A4, A5, A6, A7, A8, NAME, ...) NAME

#define EXPAND_01(MACRO, A0, ...) \
	MACRO(A0, ##__VA_ARGS__) 
#define EXPAND_02(MACRO, A0, A1, ...) \
	MACRO(A0, ##__VA_ARGS__) MACRO(A1, ##__VA_ARGS__) 
#define EXPAND_03(MACRO, A0, A1, A2, ...) \
	MACRO(A0, ##__VA_ARGS__) MACRO(A1, ##__VA_ARGS__) MACRO(A2, ##__VA_ARGS__) 
#define EXPAND_04(MACRO, A0, A1, A2, A3, ...) \
	MACRO(A0, ##__VA_ARGS__) MACRO(A1, ##__VA_ARGS__) MACRO(A2, ##__VA_ARGS__)  \
	MACRO(A3, ##__VA_ARGS__) 
#define EXPAND_05(MACRO, A0, A1, A2, A3, A4, ...) \
	MACRO(A0, ##__VA_ARGS__) MACRO(A1, ##__VA_ARGS__) MACRO(A2, ##__VA_ARGS__)  \
	MACRO(A3, ##__VA_ARGS__) MACRO(A4, ##__VA_ARGS__) 
#define EXPAND_06(MACRO, A0, A1, A2, A3, A4, A5, ...) \
	MACRO(A0, ##__VA_ARGS__) MACRO(A1, ##__VA_ARGS__) MACRO(A2, ##__VA_ARGS__)  \
	MACRO(A3, ##__VA_ARGS__) MACRO(A4, ##__VA_ARGS__) MACRO(A5, ##__VA_ARGS__) 
#define EXPAND_07(MACRO, A0, A1, A2, A3, A4, A5, A6, ...) \
	MACRO(A0, ##__VA_ARGS__) MACRO(A1, ##__VA_ARGS__) MACRO(A2, ##__VA_ARGS__)  \
	MACRO(A3, ##__VA_ARGS__) MACRO(A4, ##__VA_ARGS__) MACRO(A5, ##__VA_ARGS__)  \
	MACRO(A6, ##__VA_ARGS__) 
#define EXPAND_08(MACRO, A0, A1, A2, A3, A4, A5, A6, A7, ...) \
	MACRO(A0, ##__VA_ARGS__) MACRO(A1, ##__VA_ARGS__) MACRO(A2, ##__VA_ARGS__)  \
	MACRO(A3, ##__VA_ARGS__) MACRO(A4, ##__VA_ARGS__) MACRO(A5, ##__VA_ARGS__)  \
	MACRO(A6, ##__VA_ARGS__) MACRO(A7, ##__VA_ARGS__) 
#define EXPAND_09(MACRO, A0, A1, A2, A3, A4, A5, A6, A7, A8, ...) \
	MACRO(A0, ##__VA_ARGS__) MACRO(A1, ##__VA_ARGS__) MACRO(A2, ##__VA_ARGS__)  \
	MACRO(A3, ##__VA_ARGS__) MACRO(A4, ##__VA_ARGS__) MACRO(A5, ##__VA_ARGS__)  \
	MACRO(A6, ##__VA_ARGS__) MACRO(A7, ##__VA_ARGS__) MACRO(A8, ##__VA_ARGS__) 

#define GET_EXPAND(...) GET_MACRO_09(__VA_ARGS__, EXPAND_09, EXPAND_08, \
	EXPAND_07, EXPAND_06, EXPAND_05, EXPAND_04, EXPAND_03, EXPAND_02, EXPAND_01)
#define EXPAND_ARG_0(MACRO, ...) GET_EXPAND(__VA_ARGS__)(MACRO, __VA_ARGS__)
#define EXPAND_ARG_1(MACRO, A0, ...) GET_EXPAND(__VA_ARGS__)(MACRO, __VA_ARGS__, A0)

#define EXPAND(MACRO, ...) EXPAND_ARG_0(MACRO, __VA_ARGS__)

#define Q(x) #x
#define QUOTE(x) Q(x)

// Input ///////////////////////////////////////////////////////////////////////
#define SCANF_INT(a) scanf("%d", &(a));
#define ID(...) int __VA_ARGS__;
#define IR(...) EXPAND(SCANF_INT, __VA_ARGS__)
#define I(...) ID(__VA_ARGS__) IR(__VA_ARGS__)

// #define DEFINE_INT_ARRAY(a, n) int a[n];
// #define INT_ITH_ARRAY(a, i) a[i]
// #define IAD(N, ...) EXPAND_ARG_1(DEFINE_INT_ARRAY, N, __VA_ARGS__)
// #define IAR(N, ...) REP(array_reader_i, N){ \

#define SCANF_LL(a) scanf("%lld", &(a));
#define LD(...) ll __VA_ARGS__;
#define LR(...) EXPAND(SCANF_LL, __VA_ARGS__)
#define L(...) LD(__VA_ARGS__) LR(__VA_ARGS__)

#define DEFINE_STR(a, n) char a[n];
#define SCANF_STR(a) scanf("%s", a);
#define SD(N, ...) EXPAND_ARG_1(DEFINE_STR, N, __VA_ARGS__)
#define SR(...) EXPAND(SCANF_STR, __VA_ARGS__)
#define S(N, ...) SD(N, __VA_ARGS__) SR(__VA_ARGS__)

// Output //////////////////////////////////////////////////////////////////////
#define LN printf("\n");

#define IP(a, ...) printf("%d", a); 

// Types ///////////////////////////////////////////////////////////////////////
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef set<int> si;
typedef set<ll, ll> sll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef list<int> li;
typedef list<ll> lll;
typedef map<int, int> mii;
typedef map<int, ll> mil;
typedef map<ll, int> mli;
typedef map<ll, ll> mll;

// Loop & Iteration ////////////////////////////////////////////////////////////
#define FOR(i, a, b) for(int i = (a), loop_end_##i=(b); i < (loop_end_##i); i++)
#define REP(i, n) FOR(i, 0, n)
#define EACH(i,c) for(auto i=(c).begin(); i!=(c).end(); ++i)

#define EXIST(s,e) ((s).find(e)!=(s).end())
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort(ALL(a))
#define SORTA(a, n) sort(a, a+n);

#define PB push_back
#define itr iterator

// Range ///////////////////////////////////////////////////////////////////////
#define IN(x, a, b) (a<=x && x<b)
int dx[8] = { 1, 0, 0,-1, 1, 1,-1,-1};
int dy[8] = { 0,-1, 1, 0,-1, 1,-1, 1};

#define LARGER(a, b) a=max(a, b)
#define SMALLER(a, b) a=min(a, b)

////////////////////////////////////////////////////////////////////////////////

int main(){
	I(t);
	REP(testcase, t){
		L(n);
		printf("Case #%d: ", testcase + 1);
		if(n==0){
			printf("INSOMNIA\n");
			continue;
		}
		ll k = n;
		set<ll> ok;
		while(1){
			ll l=k;
			while(l){
				ok.insert(l%10);
				l/=10;
			}
			if(ok.size()==10){
				printf("%lld\n", k);
				break;
			}
			k+=n;
		}
	}
}

