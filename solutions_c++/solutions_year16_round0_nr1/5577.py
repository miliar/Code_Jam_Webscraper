#include<bits/stdc++.h>
using namespace std;
int main(){
	long long int i,n,k,m,r,test,j=1,s;
	scanf("%lld",&test);
	while(test--){
	scanf("%lld",&n);
	if(n==0){
	printf("Case #%d: ",j);
	printf("INSOMNIA\n");
	j++;
	continue;
	}
	long long int arr[11];
	for(i=0;i<=9;i++){
	arr[i]=-1;
	s=0;
	}
	for(i=1;;i++){
	k=n*i;
	m=0;
	while(k>0){
	arr[k%10]=k%10;
	k=k/10;
	}
	for(r=0;r<=9;r++){
		if(arr[r]==r)
			{
				m++;
			}
	}
	if(m==10){
		s=i*n;
		break;
	}
	}
	printf("Case #%d: ",j);
	printf("%lld\n",s);
	j++;
}
return 0;}
