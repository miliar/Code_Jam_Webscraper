#include<cstdio>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

#define mo 1000002013

int T;
long long ans1,ans2;
int n,m;
vector<long long>pos;
map<long long,long long>ins,ous;
map<long long,long long>::iterator it;
long long has[1111];

long long add(long long a,long long b){ return (a+b)%mo; }
long long mul(long long a,long long b){ return 1LL*a*b%mo; }

long long calc(long long l,long long r){
	long long det=abs(r-l);
	if(det==0)return 0;
	long long res=n;
	res=add(res,n-det+1);
	res=mul(res,det);
	if(res%2==0)return res/2;
	return add(res,mo)/2;
}

int main(){
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%d%d",&n,&m);
		ans1=ans2=0;
		pos.clear();
		ins.clear();ous.clear();
		for(int i=0;i<m;i++){
			long long l,r,p;
			scanf("%I64d%I64d%I64d",&l,&r,&p);
			ans1=add(ans1,mul(calc(l,r),p));
			pos.push_back(l);pos.push_back(r);
			it=ins.find(l);
			if(it==ins.end())ins[l]=0;
			ins[l]+=p;
			it=ous.find(r);
			if(it==ous.end())ous[r]=0;
			ous[r]+=p;
		}
		sort(pos.begin(),pos.end());
		pos.resize(unique(pos.begin(),pos.end())-pos.begin());

		memset(has,0,sizeof has);
		for(int i=0;i<(int)pos.size();i++){
			long long v=pos[i];
			it=ins.find(v);
			if(it!=ins.end()) has[i]+=(*it).second;

			long long need=0;
			it=ous.find(v);
			if(it!=ous.end())need=(*it).second;
			for(int j=i;j>=0&&need;j--){
				long long t=min(need,has[j]);
				ans2=add(ans2,mul(t%mo,calc(pos[j],pos[i])));
				has[j]-=t;need-=t;
			}
		}
		printf("Case #%d: %I64d\n",_,add(ans1,mo-ans2));
	}

	return 0;
}