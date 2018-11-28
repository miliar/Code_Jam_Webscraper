//GCJ Fair and Square
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <cmath>
#include <cassert>

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i=x; i<y; i++)
#define FOR(it,A) for(typeof A.begin(); it!=A.end(); it++)
#define quad(x) (x)*(x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second

typedef long long ll;
typedef pair<int,int> pii;

long long int getreverse(long long int n){
	long long int ans = 0;
	while(n){
		ans *= 10;
		ans += n % 10;
		n /= 10;
	}
	return ans;
}

long long int palin(long long int n){
	long long int r, ans;
	r = getreverse(n);
	//cout<<"recive "<<n<<endl;
	//cout<<"reverse "<<r<<endl;
	ans = r==n? 1:0;
	return ans;
}

int main(){
	long long int t, a, b, n, cont;
	scanf("%lld",&t);
	f(ncase,1,t+1){
		cont = 0;
		scanf("%lld %lld",&a, &b);
		n = 1;
		while(n*n<a){
			n++;
		}
		while(n*n<=b){
	//		printf("analize n = %d\n",n);
			if(palin(n) && palin(n*n)){
				cont++;
			}
			n++;
		}
		printf("Case #%d: %lld\n",ncase, cont);
	}
	return 0;
}
