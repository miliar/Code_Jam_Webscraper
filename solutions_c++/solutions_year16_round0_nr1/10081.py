#include <bits/stdc++.h>
#define ll long long

using namespace std;

ll t,num;
ll nums[20];

bool all_visited(ll nume[]){
	for(int i=0;i<10;i++)
		if(nume[i] == 0) return false;
	return true;
}

int main(){
	scanf("%lld",&t);

	for(int test=1;test<=t;test++){
		scanf("%lld",&num);

		memset(nums,0,sizeof nums);

		ll x = 1;
		ll aux = -1;
		if(num != 0){
			while(!all_visited(nums)){
				aux = num*x;	
				ll res = aux;			

				while(res != 0){
					nums[res%10]++;
					res /= 10;
				}


				x++;
			}
		}
	
		printf("CASE #%d: ",test);
		if(num != 0) printf("%lld\n",aux);
		else printf("INSOMNIA\n");
	}

	return 0;
}
