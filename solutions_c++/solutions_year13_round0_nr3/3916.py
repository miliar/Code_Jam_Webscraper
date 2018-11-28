#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<list>
#include<algorithm>

using namespace std;
long long int arr[] = {1LL,
4LL,
9LL,
121LL,
484LL,
10201LL,
12321LL,
14641LL,
40804LL,
44944LL,
1002001LL,
1234321LL,
4008004LL,
100020001LL,
102030201LL,
104060401LL,
121242121LL,
123454321LL,
125686521LL,
400080004LL,
404090404LL,
10000200001LL,
10221412201LL,
12102420121LL,
12345654321LL,
40000800004LL, //200002
1000002000001LL, //1000001
1002003002001LL, //1001001
1004006004001LL, //1002001
1020304030201LL, //1010101
1022325232201LL, //1011101
1024348434201LL, //1012101
1210024200121LL, //1100011
1212225222121LL, //1101011
1214428244121LL, //1102011
1232346432321LL, //1110111
1234567654321LL, //1111111
4000008000004LL, //2000002
4004009004004LL, //2001002
0
};

int main()
{
	freopen("Cinp.txt","r",stdin);
	freopen("Cout.txt","w",stdout);
	int t, n, i, out;
	long long int a, b;
	n = 0;
	scanf("%d", &t);
	while(t--)
	{
		++n;
		scanf("%lld %lld", &a, &b);
		for(i=0; i<38 && arr[i] <= b; ++i) ;
		out = i;
		for(i=0; i<38 && arr[i] < a; ++i);
		out -= i;
		printf("Case #%d: %d\n", n, out);
	}
	return 0;
}
