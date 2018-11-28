#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
#define lli long long int
char a[1002];
int main(){
freopen("A-large.in","r",stdin);
freopen("out.txt","w",stdout);
	lli t,n,sum,c1;
	cin>>t;
	for(lli j=1;j<=t;j++){
		scanf("%lld %s",&n,a);
		sum=0;
		c1=0;
		for(lli i=0;i<=n;i++){
			if(sum<i){
			c1++;
		sum++;
		}
			sum+=(a[i]-'0');
		}
		cout<<"Case #"<<j<<": "<<c1<<endl;
	}
}
