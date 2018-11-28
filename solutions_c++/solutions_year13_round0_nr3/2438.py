#include <iostream>
#include <cmath>
#include <cstdio>
#include <set>
using namespace std;

//typedef unsigned long long ull;
typedef long long ull;

ull len(ull n) {
	string s,aux;
	ull i = 0;
	while (n>0) {
		n/=10;
		aux=s;
		s=((n%10)+'0');
		s+=aux;
		++i;
	}
	return i;
}


ull reverso (ull n) {
	ull longitud = len(n);
	ull resto;
	ull r=0;
	while(longitud>0){
		resto=n%10;
		n/=10;
		r=r*10+resto;
		--longitud;
	}
	return r;
	
}



int main(int argc, char *argv[]) {
	freopen ("cuadrados_bonitos.out","w",stdout);
	set <ull> C;
	//  1 e 10^14
	ull max = 10000001;
	ull cuad;
	for (ull num=1; num<max; num++) {
		if (num == reverso(num)) {
			long double cuad = num*num;
			if (cuad == reverso(cuad)) {
				C.insert(cuad);
			}
		}
	}
	set <ull>::iterator itC = C.begin();
	
	ull min_,max_,n;
	int res = 0;
	cin>>n;
	n++;
	for (ull i=1; i<n; i++) {
		cin>>min_;
		cin>>max_;
		while (itC != C.end()) {
		if (min_ <= *itC && *itC <= max_)
			res++;
		itC++;
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
		itC = C.begin();
		res = 0;
	}
	
	return 0;
}

