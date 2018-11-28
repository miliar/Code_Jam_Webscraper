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
		double c,f,x,i,j,ans=0,ans1=0,no=0,ind=2.000000;
		scanf("%lf %lf %lf",&c,&f,&x);
		ans=x/ind;
		no=c/ind;
		ind+=f;
		while(1){
			ans1=x/ind;
			if(no+ans1<ans){
				ans=no+ans1;
				no+=c/ind;
				ind+=f;
			}
			else
				break;
		}
		std::cout << std::setprecision(7) << std::fixed;
		cout<<"Case #"<<ca<<": "<<ans;
		ca++;nl;
	}
	return 0;
}
