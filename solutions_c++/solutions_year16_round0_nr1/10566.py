#include <iostream>
using namespace std;

void upd(int &mask, long long n){
	while (n){
		mask|=1<<(n%10);
		n/=10;
	}	
}

int doit(int i){
	int mask = 0;
	long long n = 0;
	int step = 0;
	while (mask != (1<<10) - 1){
		n += i;
		upd(mask, n);
		step++;
	}
	return step;
}

int main() {
	int t;
	cin>>t;
	for (int test = 1; test <= t; test++){
		int n;
		cin>>n;
		if (!n)
		cout<<"Case #"<<test<<": "<<"INSOMNIA"<<endl;
		else
		cout<<"Case #"<<test<<": "<<1ll*doit(n)*n<<endl;
	}
	return 0;
}