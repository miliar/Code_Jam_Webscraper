#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string.h>
#include <string>
#include <set>
#include <queue>
#include <cstdlib>
#include <fstream>
#include <map>
#include <sstream>
#include <iterator>
#include <bitset>
#include <cctype>
#include <cmath>
#include <functional>
#include <iomanip>
#include <list>
#include <numeric>
#include <stack>
#include <utility>
#include <conio.h>
using namespace std;
#define ll long long
bool isPalin(string s) {
	for(int i=0; i<s.length()/2; i++) {
		if(s[i]!=s[s.length()-i-1]) return false;
	}
	return true;
}
bool ans[10000001];

int main2(){
	for(ll i=1; i<=10000000; i++) {
		stringstream ss;
		ll sq = i*i;
		ss<<sq;
		stringstream ss2;
		ss2<<i;
		ans[i] = isPalin(ss2.str()) && isPalin(ss.str());
	}
	for(ll i=1; i<=10000000; i++) {
		if(ans[i]) cout<<(i*i)<<endl;
	}
	//_getch();
	return 0;
}

void main3() {
	int t;
	scanf("%d",&t);
	ll arr[] = {
		1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0
	};
	for(int z=0; z<t; z++) {
		ll a,b;
		scanf("%lld",&a);
		scanf("%lld",&b);
		int tot = 0;
		for(int i=0; i<50; i++) {
			if(arr[i]>=a && arr[i]<=b) tot++;
		}
		printf("Case #%d: %d\n",(z+1),tot);
	}
}

int main() {
	freopen("in2.in","r",stdin);
	freopen("out.txt","w",stdout);
	main3();
	return 0;
}