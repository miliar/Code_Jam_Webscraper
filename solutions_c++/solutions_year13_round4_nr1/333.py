//by david942j
#include <cstdio>
#include <queue>
#include <algorithm>
#include <stack>
#include <vector>
using namespace std;
typedef long long LL;
const int N=1010;
const LL mod=1000002013LL;
struct unit1{
	int a,b,p;
	bool operator<(const unit1 &A)const
	{return a<A.a||(a==A.a&&b<A.b);}
	unit1(int A=0,int B=0,int P=0)
	{
		a=A;b=B;p=P;
	}
};
struct unit{
	int t,p;
	bool in;
	bool operator<(const unit &A)const
	{return t<A.t||(t==A.t&&in);}
	unit(int A=0,bool B=0,int P=0)
	{
		t=A;in=B;p=P;
	}
};
vector<unit1>A;
vector<unit>B;
LL la(LL len,LL N,LL p)
{
	LL ans=(N*len)%mod-(((len-1)*len)/2)%mod;
	ans=(ans+mod)%mod;
	ans=ans*p%mod;
	return ans;
}
LL calc(int N)
{
	int n=A.size();
	LL ans=0;
	for(int i=0;i<n;i++)
		ans=(ans+la(A[i].b-A[i].a,N,A[i].p))%mod;
	return ans;
}
void adjust()
{
	
}
LL greedy(int N)
{
	stable_sort(B.begin(),B.end());
	stack<unit>Q;
	int n=B.size();
	LL ans=0;
	for(int i=0;i<n;i++)
	{
		if(B[i].in)
			Q.push(B[i]);
		else{
			while(!Q.empty())
			{
				unit a=Q.top();
				Q.pop();
				if(a.p > B[i].p){
					ans=(ans+la(B[i].t-a.t,N,B[i].p))%mod;
					a.p-=B[i].p;
					Q.push(a);
					break;
				}
				else{
					ans=(ans+la(B[i].t-a.t,N,a.p))%mod;
					B[i].p-=a.p;
				}
			}
		}
	}
	return ans;
}
int main()
{
	int w=1,T;
	scanf("%d",&T);
	while(T--)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		//fprintf(stderr,"%d %d\n",n,m);
		//if(n==2 && m==1000)continue;
		A.clear();
		B.clear();
		for(int i=0;i<m;i++){
			int a,b,p;
			scanf("%d%d%d",&a,&b,&p);
			A.push_back(unit1(a,b,p));
			B.push_back(unit(a,true,p));
			B.push_back(unit(b,false,p));
		}
		stable_sort(A.begin(),A.end());
		LL before=calc(n);
		//printf("%lld\n",before);
		//fprintf(stderr,"QQ");
		LL after=greedy(n);
		//fprintf(stderr,"Case #%d: %lld\n",w,(before-after+mod)%mod);
		printf("Case #%d: %lld\n",w++,(before-after+mod)%mod);		
	}
}
