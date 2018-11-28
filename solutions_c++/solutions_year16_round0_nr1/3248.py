#include <bits/stdc++.h>
using namespace std;
#define ll long long
inline void print(ll last,ll k){
	if(last == 0)
		cout<<"Case #"<<k<<": "<<"INSOMNIA\n";
	else cout<<"Case #"<<k<<": "<<last<<"\n";
}
int main(int argc, char const *argv[])
{
	int T,k=1;
	scanf("%d",&T);
	ll n;
	n = 1;
	int sum = 0;
	while(T-- > 0){
		scanf("%lld",&n);
		if(n == 0){
			print(n,k++);
		}
		else{
			int mask = 0;
			int cnt = 1;
			ll last;
			while(mask != ((1<<10)-1)){
				//printf("%d\n",mask);
				ll t = cnt*n;
				last = t;
				while(t > 0){
					mask = mask | (1<<(t%10));
					t /= 10;
				}
				cnt++;
				
			}
			// sum += cnt;	
			// printf("%d ",cnt);
			print(last,k++);
		}
		//n++;
	}
	//printf("\n\n%d\n",sum);
	return 0;
}