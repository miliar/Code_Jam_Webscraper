#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#define vi vector<int>
#define vc vector<char>
#define pb push_back
#define mp make_pair
#define I vector<int>::iterator
#define rI vector<int>::iterator
#define ss(a) scanf("%s",a)
#define si(a) scanf("%d",&a)
#define sll(a) scanf("%lld",&a)
#define pi(a) printf("%d ",a)
#define pll(a) printf("%lld ",a)
#define ps(a) printf("%s ",a)
#define For(i,n) for(i=0;i<n;i++)
#define foR(i,n) for(i=n-1;i>=0;i--)
#define nl printf("\n")
#define ll long long int
#define ull unsigned long long
#define MAX
using namespace std;

#define gc getchar_unlocked
void read(int &x)
{
	register int c = gc();
	x = 0;
	for(;(c<48 || c>57);c = gc());
	for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}
int main()
{
	int t,ca=1;
	read(t);
	while(t--){
		int n,i,j,cnt1=0,cnt2=0,k;
		double naomi[1005],ken[1005];
		read(n);
		For(i,n)
			scanf("%lf",&naomi[i]);
		For(i,n)
			scanf("%lf",&ken[i]);
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		i=n-1;k=n-1;j=0;
		while(j<=k){
			if(naomi[i]>ken[k]){
				j++;cnt1++;
			}
			else
				k--;
			i--;
		}
		j=0;k=n-1;i=n-1;
		while(j<=k){
			if(naomi[k]>ken[i]){
				k--;cnt2++;
			}
			else
				j++;
			i--;
		}
		printf("Case #%d: %d %d",ca,cnt2,cnt1);nl;
		ca++;
	}
	return 0;
}
