#include <iostream> 
#include <fstream>
#include <sstream> 
#include <cstring>
#include <string> 
#include <vector> 
#include <queue> 
#include <deque> 
#include <set> 
#include <map> 
#include <algorithm> 
#include <utility> 
#include <functional> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <ctime> 

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,a) FOR(i,0,a)
#define foreach(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();++itr) 
#define X first
#define Y second
#define PB push_back
#define MP make_pair
int a[11111];
int n,x,T;
int main() {
	cin>>T;
	rep(z,T){
		memset(a,0,sizeof(a));
		cin>>n>>x;
		rep(i,n)cin>>a[i];
		int res=0;
		int ll=0,rr=n-1;
		sort(a,a+n);
		while(ll<=rr){
			if(a[ll]+a[rr]>x){
				--rr;
				++res;
			}else{
				++ll;
				--rr;
				++res;
			}
		}
		printf("Case #%d: %d\n", z+1,res);
	}
 	return 0;
}
