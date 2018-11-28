/*****************************************************/
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <map>
#include <set>
#include <ctime>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
#define   sigma_size    26
#define   lson          l,m,v<<1
#define   rson          m+1,r,v<<1|1
#define   slch          v<<1
#define   srch          v<<1|1
#define   sgetmid       int m = (l+r)>>1
#define   LL            long long
#define   ull           unsigned long long
#define   mem(x,v)      memset(x,v,sizeof(x))
#define   lowbit(x)     (x&-x)
#define   bits(a)       __builtin_popcount(a)
#define   mk            make_pair
#define   pb            push_back

const int    INF   = 0x3f3f3f3f;
const LL     INFF  = 1e18;
const double pi    = acos(-1.0);
const double inf   = 1e18;
const double eps   = 1e-9;
const LL     mod   = 1e9+7;
const int    maxmat= 10;

/*****************************************************/

const int MAX = 1e5+5;
int a[MAX<<2];
char s[3] = {'R','S','P'};
int num[3];
void solve(int n,int N,int cur,int v){
	// cout<<n<<" "<<v<<endl;
	a[v] = cur;
	if (n==N)
		num[cur]++;
	else if (n<N){
		solve(n+1,N,cur,slch);
		solve(n+1,N,(cur+1)%3,srch);
	}
}
int main(int argc, char const *argv[])
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for (int kase=1;kase<=T;kase++){
		int N,R,P,S;
		bool flag=false;
		cin>>N>>R>>P>>S;
		printf("Case #%d: ",kase);
		for (int i=0;i<3;i++){
			// a[1] = i;
			mem(num,0);
			solve(1,N+1,i,1);
			// cout<<R<<" "<<S<<" "<<P<<endl;
			// cout<<num[0]<<" "<<num[1]<<" "<<num[2]<<endl;
			if (num[0]==R&&num[1]==S&&num[2]==P){
				flag=true;
				for (int k=1<<N;k<1<<(N+1);k++)
					printf("%c",s[a[k]]);
				cout<<endl;
				break;
			}
		}
		if (!flag)
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}