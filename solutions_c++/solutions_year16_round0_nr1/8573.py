#include <iostream>
using namespace std;
int cur;
bool check(bool digitFound[]){
	for(int i = 0; i < 10; i++)
		if(!digitFound[i])
			return false;
	return true;
}
unsigned long long func(unsigned long long n,bool digitFound[],int k){
	//cout << n << endl;
	unsigned long long p = n;
	while(n/10){
		digitFound[n%10] = true;
		n /= 10;
	}
	digitFound[n] = true;
	if(!check(digitFound)){
		func((k+1)*cur,digitFound,k+1);
	}
	else
		return p;
}
int main(){
	int t;
	cin >> t;
	for(int p = 1; p <= t; p++){
		bool digitFound[10] = {false};
		unsigned long long n;
		cin >> n;
		cur = n;
		cout << "Case #" << p << ": " ;
		if(n == 0)
			cout << "INSOMNIA" << endl;
		else
			cout << func(n,digitFound,1) << endl;

	}
	return 0;
}
