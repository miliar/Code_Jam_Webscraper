#include <bits/stdc++.h>
#define loop(i,a,b) for(i=a;i<b;i++)
#define rev(i,a,b) for(i=a;i>=b;i--)
#define itloop(i,a) for(i=a.begin();i!=a.end();i++)
#define x first
#define y second
#define pushb(a) push_back(a)
#define pushf(a) push_front(a)
#define popb()   pop_back()
#define popf()   pop_front()
#define setmem(a,val) memset(a,val,sizeof(a))
#define LEN 1000005

using namespace std;
typedef long long int large;
typedef pair<int,int> ii;

large f[LEN];

large dr(large n){
	large ans=0;
	while(n){
		ans=(ans*10)+(n%10);
		n= n/10;
	}
	return ans;
}

int main(){
	int ntc,test=1;
	large n;
	//freopen("counter.txt","r",stdin);
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	setmem(f,-1);
	deque<int> q;
	f[1]=1; q.push_back(1);
	while(q.size()>0){
		n = q.front(); q.pop_front();
		if(n+1 < LEN && (f[n + 1]==-1 || f[n]+1 < f[n+1]))
			f[n+1]=1+f[n], q.push_back(n+1);
		if(dr(n)<LEN && (f[dr(n)]==-1 || f[n]+1 < f[dr(n)]))
			f[dr(n)]=1+f[n], q.push_back(dr(n));
	}
	scanf("%d",&ntc);
	while(ntc--){
		scanf("%lld",&n);
		printf("Case #%d: %lld\n",test++,f[n]);
	}
	return 0;
}

