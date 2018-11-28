#include <stdio.h>
#include <iostream>

bool isPowerOf2(long long x){
	while(x%2==0){
		x=x/2;
	}
	if(x==1) return true;
	else return false;
}

long long gcd(long long a, long long b){
	if(a>b) return gcd(b,a);
	if(b%a==0) return a;
	else return gcd(b%a, a);
}

long long greatestPowerOf2LessThan(long long a){
	long long result =1;
	while (a>1){
		result*=2;
		a/=2;
	}
	return result;
}

using namespace std;

int main(){
	int n, test=1, g;
	long long p, q, gcd_;
	scanf("%d", &n);
	while (n--){
		g=0;
		scanf("%lld/%lld", &p, &q);
		//cout << "p "<<p << " q "<< q << " g "<< g <<"\n";
		gcd_ = gcd(p,q);
		p/= gcd_;
		q/= gcd_;
		//cout << "p "<<p << " q "<< q << " g "<< g << " gcd "<< gcd_ << " irreductible \n";
		if(!isPowerOf2(q)) printf("Case #%d: impossible\n", test++);
		else {
			while(p!=q){
				g++;
				p=greatestPowerOf2LessThan(p);
				q/=2;
		//		cout << "p "<<p << " q "<< q << " g "<< g <<" go to a parent \n";
				gcd_ = gcd(p,q);
				p/= gcd_;
				q/= gcd_;
		//		cout << "p "<<p << " q "<< q << " g "<< g << " gcd "<< gcd_ << " irreductible \n";
			}
			printf("Case #%d: %d\n", test++, g);
		}
	}
	return 1;
}

