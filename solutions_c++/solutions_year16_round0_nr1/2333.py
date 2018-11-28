#include <cstdio>
#include <iostream>
#include <sstream>
#include <set>

using namespace std;

long long metodo(long long n) {
	int mult = 1;
	set<int> vals;
	long long n2, n3;
	while(vals.size() < 10){
		n2 = n * mult;
		n3 = n2;
		mult++;
		while(n2 > 0) {
			vals.insert(n2 % 10);
			n2 /= 10;
		}
		
	}
	return n3;
}


int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int i, t;
	long long n;
	//cin >> t;
	scanf("%d", &t);

	for(i = 1; i <= t; i++){

		scanf("%lld", &n);
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", i);
		}else{
			printf("Case #%d: %lld\n", i, metodo(n));
		}

		//cout << "Case #" << i << ": " << endl; 
		
	}

	return 0;
}