#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <functional>
#include <climits>
#include <list>
#include <ctime>
#include <complex>

#define F1(x,y,z) for(int x=(y);x<(z);x++)
#define F2(x,y,z) for(int x=(y);x<=(z);x++)
#define F3(x,y,z) for(int x=(y);x>(z);x--)
#define F4(x,y,z) for(int x=(y);x>=(z);x--)
#define mp make_pair
#define pb push_back
#define LL long long
#define co complex<double>
#define fi first
#define se second

#define MAX 100005
#define AMAX 1025*1005
#define MOD 1000000007

#define f(c,d) ((1<<(c))*(d))

using namespace std;

int t,n,k,ans;
char x[1005];
queue<int> q;

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		q=queue<int>();
		ans=0;
		scanf("%s%d",x,&k);
		n=strlen(x);
		F1(b,0,n){
			x[b]=(x[b]=='-');
			if(x[b]^(q.size()&1))q.push(b+k-1),ans++;
			if(!q.empty()&&q.front()==b)q.pop();
		}
		printf("Case #%d: ",a);
		if(q.empty())printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
		memset(x,0,n);
	}
	return 0;
}
