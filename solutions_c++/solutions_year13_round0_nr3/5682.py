# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <ctime>
# include <iostream>
# include <cmath>
# include <string>
# include <algorithm>
# include <vector>
# define REP(i,n) for(int i=0;i<n;i++)
# define REP1(i,n) for(int i=1;i<=n;i++)
# define CLR(a,b) memset(a,b,sizeof(a))
# define For(i,a,b) for(int i=a;i<=b;i++)
# define Trv(p,a) for(int p=head[a];p;p=next[p])
# define INF 0x7FFFFFFF
# define vi vector<int>
# define it iterator
# define pb push_back
using namespace std;

typedef long long int64;
void setIO(string name){
	string	is=name+".in",
			os=name+".out";
	freopen(is.c_str(),"r",stdin);
	freopen(os.c_str(),"w",stdout);
}

int64 ans[11000000],cnt;
const int64 maxn=10000000;
int64 val[19];
int check(int64 v){
	CLR(val,0);int k=0;
	while(v)	val[k++]=v%10,v/=10;
	REP(i,k)	if(val[i]!=val[k-1-i])	return 0;
	return 1;
}

void prepare(){
	REP1(i,maxn)	if(check(i)&&check(int64(i)*i))	ans[++cnt]=i*i;
}

int a,b;
int get(int64 v){
	if(v<1)	return 0;
	int l=1,r=cnt;
	while(l+1<r){
		int mid=(l+r)>>1;
		if(ans[mid]<=v)	l=mid;
		else	r=mid;
	}
	return l;
}

void work(){
	scanf("%lld %lld",&a,&b);
	int cc=0;
	REP1(i,cnt)	if(ans[i]>=a&&ans[i]<=b)	cc++;
	printf("%d\n",cc);
}

int main(){
	setIO("C-small-attempt0");
	prepare();
	int casen;scanf("%d",&casen);
	REP1(i,casen)	printf("Case #%d: ",i),work();
	return 0;
}
