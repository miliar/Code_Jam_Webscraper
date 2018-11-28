#include<iostream>
#include<cstring>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int t;
long long n,p;

bool try1(long long x){
	long long a=x,b=(1LL<<n)-1-x;
	long long c=0;
	for(int i=0;i<n;i++){
		c*=2;
		if(a>0){
			c++;
			a--;
			b/=2;
			if(a%2==1)b++;
			a/=2;
		}else{
			b--;
			b/=2;
		}
	}
	return c<p;
}

bool try2(long long x){
	long long a=x,b=(1LL<<n)-1-x;
	long long c=0;
	for(int i=0;i<n;i++){
		c*=2;
		if(b==0){
			c++;
			a--;
			a/=2;
		}else{
			b--;
			a/=2;
			if(b%2==1)a++;
			b/=2;
		}
	}
	return c<p;
}

int main(){
	int h;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%lld%lld",&n,&p);
		long long l,r,mid,y,z;
		l=0;r=(1LL<<n)-1;
		while(r>l){
			mid=(r+l+1)/2;
			if(try1(mid))l=mid;
			else r=mid-1;
		}
		y=l;
		l=0;r=(1LL<<n)-1;
		while(r>l){
			mid=(r+l+1)/2;
			if(try2(mid))l=mid;
			else r=mid-1;
		}
		z=l;
		printf("Case #%d: %lld %lld\n",h,y,z);
	}
	return 0;
}
