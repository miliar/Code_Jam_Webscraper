#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
	int Test;
	ll N;
	scanf("%d", &Test);
	for(int test=1; test<=Test; test++){
		scanf("%lld", &N);
		
		if(N==0){
			printf("Case #%d: INSOMNIA\n", test); continue;
		}
		stringstream SS;
		int mask=0;
		/*for(int i=0; i<=9; i++){
			mask|=(1<<i);
		}
		cout<<mask<<endl;*/
		ll I=1LL;
		while(mask!=1023){
			ll Ans=N*I;
			stringstream SS;
			SS<<Ans;
			string Aux;
			SS>>Aux;
			//cout<<Aux<<endl;
			for(int i=0; i<Aux.size(); i++){
				mask|=(1<<(Aux[i]-'0'));
			}
			//cout<<mask<<endl;
			I++;
		}
		I--;
		printf("Case #%d: %lld\n", test, I*N);
	}					 
	return 0;
}
