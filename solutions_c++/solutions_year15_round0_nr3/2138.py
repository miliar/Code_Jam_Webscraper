#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <bitset>
using namespace std;

#ifdef _LOCAL_
#define LLD "%lld"
#else
#define LLD "%lld"
#endif

#define prev pppppppprev
#define next nnnnnnnnext

#ifdef _LOCAL_
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define DB1(x) cerr<<#x<<" = "<<(x)<<"\n"
#define DB2(x, y) cerr<<#x<<" = "<<(x)<<", "<<#y<<" = "<<(y)<<"\n"
#define DB3(x, y, z) cerr<<#x<<" = "<<(x)<<", "<<#y<<" = "<<(y)<<", "<<#z<<" = "<<(z)<<"\n"
#define DB4(x, y, z, w) cerr<<#x<<" = "<<(x)<<", "<<#y<<" = "<<(y)<<", "<<#z<<" = "<<(z)<<", "<<#w<<" = "<<(w)<<"\n"
#define DB5(x, y, z, w, t) cerr<<#x<<" = "<<(x)<<", "<<#y<<" = "<<(y)<<", "<<#z<<" = "<<(z)<<", "<<#w<<" = "<<(w)<<", "<<#t<<" = "<<(t)<<"\n"
#define DB6(x0, x1, x2, x3, x4, x5) cerr<<#x0<<" = "<<(x0)<<", "<<#x1<<" = "<<(x1)<<", "<<#x2<<" = "<<(x2)<<", "<<#x3<<" = "<<(x3)<<", "<<#x4<<" = "<<(x4)<<", "<<#x5<<" = "<<(x5)<<"\n"
#define DB7(x0, x1, x2, x3, x4, x5, x6) cerr<<#x0<<" = "<<(x0)<<", "<<#x1<<" = "<<(x1)<<", "<<#x2<<" = "<<(x2)<<", "<<#x3<<" = "<<(x3)<<", "<<#x4<<" = "<<(x4)<<", "<<#x5<<" = "<<(x5)<<", "<<#x6<<" = "<<(x6)<<"\n"
#define DB8(x0, x1, x2, x3, x4, x5, x6, x7) cerr<<#x0<<" = "<<(x0)<<", "<<#x1<<" = "<<(x1)<<", "<<#x2<<" = "<<(x2)<<", "<<#x3<<" = "<<(x3)<<", "<<#x4<<" = "<<(x4)<<", "<<#x5<<" = "<<(x5)<<", "<<#x6<<" = "<<(x6)<<", "<<#x7<<" = "<<(x7)<<"\n"
#define DB9(x0, x1, x2, x3, x4, x5, x6, x7, x8) cerr<<#x0<<" = "<<(x0)<<", "<<#x1<<" = "<<(x1)<<", "<<#x2<<" = "<<(x2)<<", "<<#x3<<" = "<<(x3)<<", "<<#x4<<" = "<<(x4)<<", "<<#x5<<" = "<<(x5)<<", "<<#x6<<" = "<<(x6)<<", "<<#x7<<" = "<<(x7)<<", "<<#x8<<" = "<<(x8)<<"\n"
#else
#define eprintf(...) static_cast<void>(0)
#define DB1(x) static_cast<void>(0)
#define DB2(x, y) static_cast<void>(0)
#define DB3(x, y, z) static_cast<void>(0)
#define DB4(x, y, z, w) static_cast<void>(0)
#define DB5(x, y, z, w, t) static_cast<void>(0)
#define DB6(x0, x1, x2, x3, x4, x5) static_cast<void>(0)
#define DB7(x0, x1, x2, x3, x4, x5, x6) static_cast<void>(0)
#define DB8(x0, x1, x2, x3, x4, x5, x6, x7) static_cast<void>(0)
#define DB9(x0, x1, x2, x3, x4, x5, x6, x7, x8) static_cast<void>(0)
#endif

#define rep(x,y,z) for (int x = (y), e##x = (z);x < e##x; x++)
typedef long long ll;
typedef pair<int,int> pii;

string idx2str[8] = {"1", "-1", "i", "-i", "j", "-j", "k", "-k"};
map<string, int> str2idx;
int mul[8][8];
const int MAXLEN = 10000;
char S[10 * MAXLEN+1], buf[MAXLEN+1];

int inv(int q)
{
	if(idx2str[q] == "1" || idx2str[q] == "-1")
		return q;
	return (q ^ 1);
}

void test(int tnum)
{
	int L, i, j;
	long long X;
	scanf("%d%lld%s", &L, &X, buf);
	int pprod = str2idx["1"], prod;
	string op("1");
	for(i = 0; i < L; ++i)
	{
		op[0] = buf[i];
		pprod = mul[pprod][str2idx[op]];
	}
	prod = pprod;
	for(i = 1; i < ((X - 1) % 4) + 1; ++i)
		prod = mul[prod][pprod];
	if(L * X < 3 || prod != str2idx["-1"])
	{
		printf("Case #%d: NO\n", tnum);
		return;
	}

	for(i = 0; i < X && i < 8; ++i)
		strcpy(S + i * L * sizeof(char), buf);
	prod = str2idx["1"];
	for(i = 0; i < X * L && i < 8 * L; ++i)
	{
		op[0] = S[i];
		prod = mul[prod][str2idx[op]];
		if(prod == str2idx["i"])
			break;
	}
	prod = str2idx["1"];
	for(j = min(X, 8LL) * L - 1; j >= 0; --j)
	{
		op[0] = S[j];
		prod = mul[str2idx[op]][prod];
		if(prod == str2idx["k"])
			break;
	}
	printf("Case #%d: %s\n", tnum, i + 1 < j ? "YES" : "NO");
}

void run()
{
	for(int i = 0; i < 8; ++i)
		str2idx.insert(pair<string,int>(idx2str[i], i));
	mul[str2idx["1"]][str2idx["1"]] = str2idx["1"];
	mul[str2idx["1"]][str2idx["i"]] = str2idx["i"];
	mul[str2idx["1"]][str2idx["j"]] = str2idx["j"];
	mul[str2idx["1"]][str2idx["k"]] = str2idx["k"];

	mul[str2idx["i"]][str2idx["1"]] = str2idx["i"];
	mul[str2idx["i"]][str2idx["i"]] = str2idx["-1"];
	mul[str2idx["i"]][str2idx["j"]] = str2idx["k"];
	mul[str2idx["i"]][str2idx["k"]] = str2idx["-j"];

	mul[str2idx["j"]][str2idx["1"]] = str2idx["j"];
	mul[str2idx["j"]][str2idx["i"]] = str2idx["-k"];
	mul[str2idx["j"]][str2idx["j"]] = str2idx["-1"];
	mul[str2idx["j"]][str2idx["k"]] = str2idx["i"];

	mul[str2idx["k"]][str2idx["1"]] = str2idx["k"];
	mul[str2idx["k"]][str2idx["i"]] = str2idx["j"];
	mul[str2idx["k"]][str2idx["j"]] = str2idx["-i"];
	mul[str2idx["k"]][str2idx["k"]] = str2idx["-1"];

	for(int i = 1; i < 8; i += 2)
		for(int j = 0; j < 8; ++j)
			mul[i][j] = (mul[i^1][j] ^ 1);
	for(int i = 0; i < 8; ++i)
		for(int j = 1; j < 8; j += 2)
			mul[i][j] = (mul[i][j^1] ^ 1);

	int T;
	scanf("%d", &T);
	for(int tnum = 1; tnum <= T; ++tnum)
		test(tnum);
}

//#define file_name "barduck"

int main()
{
//#ifdef _LOCAL_
    if(freopen("input.txt", "r", stdin) == NULL)
    {
        printf("Can't open input.txt\n");
        return 0;
    }
    if(freopen("output.txt", "w", stdout) == NULL)
    {
        printf("Can't open output.txt\n");
        return 0;
    }
//#else
#ifdef file_name
    freopen(file_name".in", "r", stdin);
    freopen(file_name".out", "w", stdout);
#endif
//#endif
    run();
//#ifdef _LOCAL_
    //puts("================");
//#endif

    return 0;
}
