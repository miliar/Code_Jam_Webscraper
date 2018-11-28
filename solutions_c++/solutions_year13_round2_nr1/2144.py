//Author: Amit Mittal
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<stack>
#include<queue>
#include<deque>
#include<algorithm>

using namespace std;

#define mod 1000000007
#define inf 2147483647
#define ninf -2147483648
#define FOR(i,a,b) for(i=a;i<b;i++)
#define s(a) scanf("%d",&a)
#define lls(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define sp(a) printf("%s",a)
#define cp(a) printf("%c",a)
#define nline printf("\n")
#define space printf(" ")
#define ll long long

int n;

int func(int val, int a[], int index){
	if(index>=n){
		return 0;
	}

	if(val>a[index]){
		return func(val+a[index], a, index+1);
	}

	int ans;
	if(val<=a[index]){
		if(val==1)
			ans = 1+func(val, a, index+1);
		else
			ans = min(1+func((2*val)-1, a, index), 1+func(val, a, index+1));
		return ans;
	}
}

int main() {
	int test, a[105], val;
	s(test);

	for(int t=1;t<=test;++t){
		s(val), s(n);
		for(int i=0;i<n;++i)
			s(a[i]);

		sort(a, a+n);
		int ans = func(val, a, 0);
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}
