
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stack>
#include <cctype>
#include <complex>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


int PalTF(long long int a){
	int n=0;
	string str;
	
	while(a){
		char c = '0' + a%10;
		str += c;
		a /= 10;
		n++;
	}
	
	for(int i=0;i<n/2;i++){
		if(str[i] != str[n-1-i]) return 0;
	}

	return 1;
} 

int FasnTF(long long int a){
	if(PalTF(a) == 0) return 0;
	long long int b = (long long int)sqrt((double)a);
	if(a != b*b) return 0;
	if(PalTF(b) == 0) return 0;
		
	return 1;
}

int solve(){
	int ans=0;
	long long int a,a2;
	cin>> a>> a2;
	
	while(1){
		if(a==a2){
			if(FasnTF(a)){
				ans++;
			}
			break;
		}
		if(FasnTF(a)){
			ans++;
		}
		a++;
	}
	
	return ans;
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(10);

	int n;
	cin>> n;
	for(int k=0;k<n;k++){
		int ans = solve();
		cout<<"Case #"<< k+1<< ": "<< ans<< endl;
	}

	return 0;
}

 