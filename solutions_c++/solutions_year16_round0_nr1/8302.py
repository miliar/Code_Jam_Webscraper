#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<set>
using namespace std;
set<char> s;
void adder(long long N){
	while(N){
		s.insert(N % 10 + 48);
		N /= 10;
	}
}
int main(){
	long long t, n, i, k, j;
	cin >> t;
	
	for(j = 0; j < t; j++){
		cin >> n;
		if(n==0) cout << "Case #" << j+1 << ": INSOMNIA" << endl;
		else {
			i = 0;
			k = n;
			while(s.size() < 10){
				i++;
				adder(n);
				n+=k;
			}
			cout << "Case #" << j+1 << ": " << i * k << endl;
		}
		s.clear();
	}
	return 0;
}
