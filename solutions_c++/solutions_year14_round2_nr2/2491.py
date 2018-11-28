#include<iostream>
using namespace std;
int main(){
	int t,a,b,k,i,j;
	scanf("%d",&t);
	for(int p=1;p<=t;p++){
		cin>>a>>b>>k;
		long long int cnt=0;
		for(i=0;i<a;i++){
			for(j=0;j<b;j++){
				if((i&j)<k)
					++cnt;
				}
			}
			printf("Case #%d: %lld\n",p,cnt);
			//cout<"Case<cnt<<endl;
	}
	return 0;
}
