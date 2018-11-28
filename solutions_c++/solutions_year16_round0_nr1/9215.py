#include<bits/stdc++.h>
#define LL long long int
using namespace std;

map<LL, bool> m;
bool digs[10];
void init(){
	for(int i = 0; i < 10; i++){
		digs[i] = false;
	}
	m.clear();
}

bool getdigs(LL x){
	
	while(x > 0){
		digs[x%10] = true;
		x /= 10;
	}
	for(int i = 0; i < 10; i++){
		if(!digs[i])
			return false;
	}
	return true;
}


int main(){
	int t;
	cin >> t;
	for(int z = 1; z <= t; z++){
		init();
		printf("Case #%d: ", z);
		LL N, temp;
		scanf("%lld", &N);
		temp = N;
		m[N] = true;
		bool flag = true;
		while(!getdigs(temp)){
			temp += N;
			if(m.find(temp) != m.end()){
				flag = false;
				break;
			}
			m[temp] = true;
		}
		if(!flag){
			printf("INSOMNIA\n");
		}
		else{
			printf("%lld\n", temp);
		}
	}
}