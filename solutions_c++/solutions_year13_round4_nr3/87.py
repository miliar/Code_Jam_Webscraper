//Orz Sevenkplus
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cctype>
#include<complex>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<bitset>
#define un using namespace
un std;
#define pb push_back
#define pf pop_front

#define mp make_pair

#define c0 first
#define c1 second
#define sqr(x)((x)*(x))
#define clr(x)memset(x,0,sizeof(x))
#define clr1(x)memset(x,-1,sizeof(x))
#define clr80(x)memset(x,0x80,sizeof(x))
#define clr7F(x)memset(x,0x7F,sizeof(x))

#define ll long long
#ifdef __unix__
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif
#define pii pair<int,int>
#define pip pair<int,pii>
#define vi vector<int>
#define vpi vector<pii>
#define pq priority_queue

template<typename T>inline bool chkmin(T&a,T&b){return a>b?a=b,1:0;}
template<typename T>inline bool chkmax(T&a,T&b){return a<b?a=b,1:0;}
#define modadd(a,b,c)(((a)+(b))%(c))
#define modmul(a,b,c)((int)(((ll)(a)*(b))%(c)))

#define P 1000000007

#define getint(x){\
	char __next__char__;\
	while(!isdigit(__next__char__=getchar()));x=__next__char__-48;\
	while(isdigit(__next__char__=getchar()))x=x*10+__next__char__-48;\
}
#define getint2(x1,x2){getint(x1);getint(x2);}
#define getint3(x1,x2,x3){getint(x1);getint(x2);getint(x3);}
#define getint4(x1,x2,x3,x4){getint(x1);getint(x2);getint(x3);getint(x4);}
#define getint5(x1,x2,x3,x4,x5){getint(x1);getint(x2);getint(x3);getint(x4);getint(x5);}
#define getint6(x1,x2,x3,x4,x5,x6){getint(x1);getint(x2);getint(x3);getint(x4);getint(x5);getint(x6);}

int n,a[2000],dis[2001];
bool V[2001];
vector<int>E[2001];
void go(int x){
	V[x]=1;
	dis[x]++;
	for(int i=E[x].size();i--;)if(!V[E[x][i]]&&dis[x]==dis[E[x][i]])go(E[x][i]);
}
void run(){
	getint(n);
	dis[n]=0;
	for(int i=n;i--;)E[i].clear();
#define ae(x,y) E[y].pb(x)
	for(int i=-1;++i!=n;){
		dis[i]=0;
		getint(a[i]);
		ae(i,n);
		for(int j=i;j--;)if(a[j]==a[i]){
			ae(j,i);//xj>xi
			break;
		}for(int j=i;j--;)if(a[j]==a[i]-1){
			ae(i,j);//xi>xj
			break;
		}
	}
	for(int i=-1;++i!=n;)getint(a[i]);
	for(int i=-1;++i!=n;){
		for(int j=i;++j!=n;)if(a[j]==a[i]){
			ae(j,i);//xj>xi
			break;
		}for(int j=i;++j!=n;)if(a[j]==a[i]-1){
			ae(i,j);//xi>xj
			break;
		}
	}
	deque<int>Q(1,n);
	static bool v[2001];
	clr(v);
	v[n]=1;
	while(!Q.empty()){
		int x=Q.front();Q.pop_front();
		for(int i=E[x].size();i--;){
			int y=E[x][i];
			if(dis[y]<dis[x]+1){
				dis[y]=dis[x]+1;
				if(!v[y]){
					v[y]=1;
					Q.pb(y);
				}
			}
		}v[x]=0;
	}
	for(int i=0;i++!=n;){
		bool flag=0;
		for(int j=-1;++j!=n;){
			if(dis[j]==i){
				if(flag){
					go(j);
				}else flag=1;
			}
		}
		clr(V);
	}
	//printf("%d\n",n);
	for(int i=-1;++i!=n;)printf(" %d",dis[i]);
	printf("\n");
}
int main(){
	int t;
	getint(t);
	for(int _=1;_<=t;_++){
		printf("Case #%d:",_);
		run();
	}
	return 0;
}
