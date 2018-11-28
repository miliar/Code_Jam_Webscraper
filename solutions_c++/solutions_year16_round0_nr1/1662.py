#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
int A[10];
bool sett(int num){
	while(num){
		int dig=num%10;
		num/=10;
		A[dig]=1;
	}
	int cnt=0;
	for(int i=0;i<10;i++){
		cnt+=A[i];
	}
	return cnt!=10;
}
ll f(ll num){
	memset(A,0,sizeof(A));
	ll num2=num;
	while(sett(num2)){
		num2+=num;
	}
	return num2;
}
int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	ll num;
	
	for(int i=0;i<T;i++){
		cin >> num;
		cout << "Case #" << i+1 << ": ";
		if(num ==0){
			cout << "INSOMNIA";
		} else {
			cout << f(num);
		}
		cout << endl;
	}
	
	return 0;
}