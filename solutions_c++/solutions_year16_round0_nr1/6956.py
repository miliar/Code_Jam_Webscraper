#include<bits/stdc++.h>
#define ll long long int
#define user hardik
#define ld done
#define hmm ios_base::sync_with_stdio(0)
using namespace std;
void func(int *hash,ll  n,int *count){
	while(n){
		ll t = n%10;
		if(hash[t]==0){
			(*count)++;
		}
		hash[t]=1;
		n=n/10;
	}
}
ll  t,n,i,j,k;
int main(){
 cout.tie(0);
	scanf("%lld",&t);
	ll lol=0;

	for(k=1;k<=t;k++)
{
lol++;
		scanf("%lld",&n);

		if(n==0){
			printf("case #%lld: INSOMNIA\n",k);
			continue;
		}
		int hash[10]={0};
        int count=0;

		ll  old=n,i=2;
		while(1){

			func(hash,n,&count);
			if(count==10){
				printf("case #%lld: %lld\n",k,n);
				break;
			}
			else{
				n=i*old;
				i++;
			}
		}
	}
	return 0;
}
