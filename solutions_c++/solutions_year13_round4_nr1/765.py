#include <cstdio>
#include <map>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <map>
using namespace std;
#define mod 1000002013 
map<int,long long> num;
typedef long long LL;
struct P
{
	int s,p,id;
	bool operator < (const P & b)const {
		if(s==b.s) return id<b.id;
		return s<b.s;
	}
}seg[2200*2];
int era[4000];
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;
	int ca=0;
	scanf("%d",&T);
	while(T--){
		int n,M;
		scanf("%d%d",&n,&M);
		int tol=0;
		for(int i=0;i<M;i++){
			int a,b,c;
			scanf("%d%d%d",&a,&b,&c);
			LL len=b-a;
			tol=(tol+len*n%mod*c-len*(len-1)/2%mod*c)%mod;
			seg[i].s=a ,seg[i].p=c , seg[i].id=0;
			seg[i+M].s=b, seg[i+M].p=c ,seg[i+M].id=1;
		}
		sort(seg,seg+2*M);
		num.clear();
		int tol1=0;
		for(int i=0;i<2*M;i++){
			int s=seg[i].s,p=seg[i].p ,id=seg[i].id;
//			printf("%d %d %d\n",s,p,id);
			if(id==0){
				if(num.find(s)==num.end()) num[s]=p;
				else num[s]+=p;
			}
			else {
				map <int,long long> :: iterator it;
				int ct=0;
				int tmp=0;
				for(it=num.end(),it--;;it--){
					long long x=it->second;
					long long y=it->first;
//					printf("%d %d\n",y,x);
					if(x>p){
						LL len=s-y;
						tmp=(tmp+len*n%mod*p-len*(len-1)/2%mod*p)%mod;
						num[y]-=p;
						p=0;
					}
					else {
						LL len=s-y;
						tmp=(tmp+len*n%mod*x-len*(len-1)/2%mod*x)%mod;
						p-=x;
						era[ct++]=y;
					}
					if(!p) break;
				}
				tol1=(tol1+tmp)%mod;
				for(int i=0;i<ct;i++) num.erase(era[i]);
			}
		}
		
//		printf("%d\n",num.size());
		int ans=(tol-tol1)%mod;
		if(ans<0) ans+=mod;
		printf("Case #%d: %d\n",++ca,ans);
	}
}






