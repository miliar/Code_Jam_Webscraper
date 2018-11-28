#include<cstdio>
long long min(long long a,long long b){
	if(a>b)
	return b;
	else 
	return a;
}
int main(){
	long long t,k,n,i,max,m1,j,s,r,a[100001];
	scanf("%lld",&t);
for(k=1;k<=t;k++){max=-1;
		scanf("%lld",&n);
		for(i=0;i<n;i++)
		scanf("%lld",&a[i]);
		for(i=0;i<n;i++){
		if(a[i]>max)
		max=a[i];}
		m1=max;
		for(i=1;i<m1+1;i++){
			s=i;
			for(j=0;j<n;j++){
				if(a[j]>i){
					if(a[j]%i==0)
					s+=((a[j]/i)-1);
					else
					s+=a[j]/i;
				}}
				m1=min(m1,s);
				}
				r=m1;
				printf("Case #%lld: %lld\n",k,r);
			}
		}
	

