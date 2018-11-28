#include<iostream>
using namespace std;
int a[14];

long long comp(int base){
	long long ans = 1;
	for(int i = 0; i < 14; i++){
		ans *= base;
		ans += a[i];
	}
	ans *= base;
	ans += 1;
	return ans;
}

int main(){
	int t, nn, jj;
	cin >> t >> nn >> jj;
	cout << "Case #1:" << endl;
	for(int i = 0; i < 500; i++){
		int t = i;
		string s = "1";
		for(int j = 13; j >= 0; j--){
			a[j] = t % 2;
			char temp = '0' + a[j];
			s = temp + s;
			t /= 2; 
		}
		s = "1" + s;
		cout << s << s;
		for(int base = 2; base <= 10; base++)cout << " "<< comp(base);
		cout << endl;
	}
	//system("pause");
	return 0;
}
