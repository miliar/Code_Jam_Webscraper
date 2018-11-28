#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

long long factor(long long x, long long base){
	vector<long long> v;
	long long i, tmp = 1;
	while(x){
		v.push_back(x % 2);
		x /= 2;
	}
	for(i = 0; i < v.size(); i++){
		x += v[i] * tmp;
		tmp *= base;
	}
	for(i = sqrt(x); i >= 1; i--){
		if(x % i == 0) return i;
	}
}

long long poss(long long x){
	for(long long i = 2; i <= 10; i++){
		if(factor(x, i) == 1){
			return 0;
		}
	}
	return 1;
}

long long bin(long long x){
	vector<long long> v;
	long long i;
	while(x){
		v.push_back(x % 2);
		x /= 2;
	}
	for(i = v.size() - 1; i >= 0 ; i--){
		cout<<v[i];
	}
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long t, n, i, j;
	vector<long long> v;
	cin>>t;
	for(i = 1; i <= t; i++){
		printf("Case #%d:\n", i);
		cin>>n>>j;
		for(i = (1<<(n - 1)) + 1; i < (1<<n); i += 2){
			if(poss(i)){
				v.push_back(i);
                //cout<<i<<endl;
			}
			if(v.size() == j){
				break;
			}
		}
		for(j = 0; j < v.size(); j++){
			bin(v[j]);
			for(long long k = 2; k <= 10; k++){
				cout<<" "<<factor(v[j], k);
			}
			cout<<endl;
		}
	}
}
