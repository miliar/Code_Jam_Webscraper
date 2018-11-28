#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <array>
using namespace std;

#ifdef _LOCAL_
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif

#define prev pppppppprev
#define next nnnnnnnnext

#ifdef _LOCAL_
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define DB(args...) cerr<<__LINE__<<": ";DBin(#args, args)
#define DBcont(cont) cerr<<__LINE__<<": "<<#cont<<" = ", print_cont(cont)
#else
#define eprintf(...) static_cast<void>(0)
#define DB(args...) static_cast<void>(0)
#define DBcont(cont) static_cast<void>(0)
#endif
void DBcontinue() {}
template <typename T, typename... Args>
void DBcontinue(T head, Args... tail)
{
	char *head_name = strtok(NULL, ",");
	cerr << "," << string(head_name) << "=" << head;
	DBcontinue(tail...);
}
template <typename T, typename... Args>
void DBin(const char *names, T head, Args... tail)
{
	char *names_buf = new char[strlen(names) + 1];
	strcpy(names_buf, names);
	char *head_name = strtok(names_buf, ",");
	cerr << string(head_name) << "=" << head;
	DBcontinue(tail...);
	cerr << "\n";
	delete[] names_buf;
}
template <class Container>
void print_cont(const Container &cont)
{
	cerr << "{ ";
	for(auto it = begin(cont); it != end(cont); ++it)
	{
		if(it != begin(cont))
			cerr << ", ";
		cerr << *it;
	}
	cerr << " }\n";
}

#define rep(x,y,z) for (int x = (y), e##x = (z);x < e##x; x++)
typedef long long ll;
typedef pair<int,int> pii;

int ceil(int num, int denom)
{
	return num / denom + (num % denom != 0);
}
void test(int tnum)
{
	int r, c, w;
	scanf("%d%d%d", &r, &c, &w);
	if(w == 1)
	{
		printf("Case #%d: %d\n", tnum, r * c);
		return;
	}
	int ans = r * ceil(c, w) + w - 1;
	printf("Case #%d: %d\n", tnum, ans);
}

void run()
{
	int T, t;
	scanf("%d", &T);
	for(t = 1; t <= T; ++t)
		test(t);
}

//#define file_name "barduck"

int main()
{
#ifdef _LOCAL_
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
#else
#ifdef file_name
    freopen(file_name".in", "r", stdin);
    freopen(file_name".out", "w", stdout);
#endif
#endif
    run();
#ifdef _LOCAL_
    //puts("================");
#endif

    return 0;
}
