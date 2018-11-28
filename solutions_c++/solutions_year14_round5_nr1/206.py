#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
#define SORT(x) sort(x.OP,x.ED)
#define SQ(x) ((x)*(x))
#define SSP system("pause")
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
typedef long long LL;
typedef pair<int, int> PII;
const double eps=1e-8;
const double INF=1e20;
const double PI=acos( -1. );
const int MXN = 50;
const LL MOD = 1000000007;
LL w[1000005];
LL sum[1000005];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j;
	int T;
	scanf("%d",&T);
	for(int CASE=1;CASE<=T;++CASE){
		int N,p,q,r,s;
		scanf("%d%d%d%d%d",&N,&p,&q,&r,&s);
		for(i=0;i<N;i++)w[i+1]=(1LL*i*p+q)%r+s;
		sum[0]=0;
		for(i=1;i<=N;i++)sum[i]=sum[i-1]+w[i];
		int P,Q;
		LL ans=sum[N];
		for(P=1;P<=N;P++){
			//r in l~N
			int l=P,r=N;
			while(r>=l){
//				cout<<l<<"~"<<r<<endl;
				if(r-l<=2){
					if(r-l==0)break;
					LL fl=max(sum[N]-sum[l],sum[l]-sum[P-1]);
					LL fr=max(sum[N]-sum[l+1],sum[l+1]-sum[P-1]);
					if(fl<fr)r=l;else l=l+1;
					continue;
				}
				int lm=l+(r-l)/3;
				int rm=r-(r-l)/3;
				LL fl=max(sum[N]-sum[lm],sum[lm]-sum[P-1]);
				LL fr=max(sum[N]-sum[rm],sum[rm]-sum[P-1]);
				if(fl>fr)l=lm;
				else r=rm;
			}
//			cout<<r<<endl;
			LL z=max(sum[N]-sum[r],max(sum[r]-sum[P-1],sum[P-1]));
			cmin(ans,z);
		}
		printf("Case #%d: %.10lf\n",CASE,(sum[N]-(double)ans)/sum[N]);
	}
	return 0;
}
