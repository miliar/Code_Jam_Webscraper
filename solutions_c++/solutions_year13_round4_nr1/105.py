#include <stdio.h>
#include <algorithm>
int n,m;
long long cnt[2002],time[2002],print;
#define MOD 1000002013;
struct q{
	long long su,per;
	bool se;
	bool operator() (q a,q b){
		return a.su<b.su;
	}
}su[2001];
void pro(){
	int i,j,kk=0,k;
	long long sum=0,min,s;
	std::sort(su,su+m*2,q());
	for(i=0;i<m*2;){
		for(j=i;j<m*2;j++){
			if(su[i].su!=su[j].su) break;
			if(!su[j].se)
				sum+=su[j].per;
			else
				sum-=su[j].per;
		}
		cnt[kk]=sum;
		time[kk++]=su[i].su;
		i=j;
	}
	for(i=0;i<kk-1;){
		if(cnt[i]==0){
			i++;
			continue;
		}
		min=cnt[i];
		for(j=i+1;j<kk;j++){
			if(cnt[j]==0) break;
			if(min>cnt[j])
				min=cnt[j];
		}
		s=(time[j]-time[i])*(time[j]-time[i]-1)/2;
		s%=MOD;
		for(k=i;k<j;k++)
			cnt[k]-=min;
		min%=MOD;
		print+=s*min;
		print%=MOD;
		if(cnt[i]==0)
			i++;
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,testt,i;
	long long save=0,a,b,c;
	scanf("%d",&testt);
	for(test=1;test<=testt;test++){
		scanf("%d %d",&n,&m);
		print=0;
		save=0;
		for(i=0;i<m;i++){
			scanf("%lld %lld %lld",&a,&b,&c);
			su[i*2].se=0;
			su[i*2].per=c;
			su[i*2].su=a;
			su[i*2+1].se=1;
			su[i*2+1].per=c;
			su[i*2+1].su=b;
			save+=(b-a)*(b-a-1)/2*c;
			save%=MOD;
		}
		pro();
		print-=save;
		if(print<0)
			print+=MOD;
		printf("Case #%d: %lld\n",test,print);
	}
	return 0;
}
