#include <iostream>
#include <cstdio>
#define MAX 10e9+7

using namespace std;
typedef unsigned long long ull;

int val[10];

bool verify(){
	for(int i=0; i<10; i++)
		if(val[i]==0)
			return 1;
	return 0;
}

bool check(ull m){
	while(m>0){
		val[m%10]++;
		m /= 10;
	}
	return verify();
}

ull sleep(ull n){
	int temp = n;
	for(int i=0; i<10; i++)
		val[i] = 0;
	while(check(temp) && n<MAX){
		temp += n;
		//cout << n << endl;
	}
	if(verify())
		return 0;
	else
		return temp;
}

int main() {
	freopen("A-large.in","r",stdin);
	freopen("out1.io","w",stdout);
	int test,i=1;
	ull ans,n;
	cin >> test;
	while(i<=test){
		cin >> n;
		if(n==0){
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else{
			ans = sleep(n);
			if(ans==0)
				cout << "Case #" << i << ": INSOMNIA" << endl;
			else
				cout << "Case #" << i << ": "<<ans << endl;
		}
		i++;
	}
	return 0;
}