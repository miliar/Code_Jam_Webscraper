#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

	
int tobase10(int n, LL base){
	int a = 0;int i = 0;
	while(n>0){
		a += (pow(base, i))*(n%10);
		n/=10;
		++i;	
	}
	return a;
}
	
vector<int> tobase2(int n, int size) {
	vector<int> tmp(size);
	int i =0 ;
	while(n > 0){
		tmp[i++] = n%2;
		n/=2;
	}



	return tmp;
}

LL unprime(vector<int> num, int base){
	LL a = 0;
	LL i = 0;
	for_each(num.rbegin(), num.rend(), [&](int val) {
			
			a += (pow(base, i))*val;

			i++;
	});



	for(LL i = 2; i < sqrt(a); ++i){
		
		if(a%i == 0){

			return i;
		}
	}
	return -1;
}


int main() {

	LL t; cin >> t;

	LL n, j; cin >> n >> j;


	vector<int> vec(n);
	vec[0] = 1; vec[n-1] = 1;
	LL l = n-2;
	LL count=0;

	LL lim=1;
	for(int i = 0; i < l; ++i){
		
		lim *= 2;}
	lim -= 1;
	for(int i = 0; i <= lim; ++i){
		
		vector<int> from = tobase2(i, n-2);
		
		copy(from.rbegin(), from.rend(), vec.begin()+1);
	
		int valid=1;
		vector<LL> divs;
	
		for(int j = 2; j <= 10; ++j){
	
			LL div = unprime(vec, j);
			if(div==-1) valid=0;
			divs.push_back(div);
	
		}
		if(valid){
			++count;	
			for_each(vec.begin(), vec.end(), [](int val) {std::cout << val;});
			for_each(divs.begin(), divs.end(), [](LL val) {std::cout << " " << val;});		
			std::cout << endl;
		}
	
		if(count==j)break;
	}
}
			
