#include <bits/stdc++.h>
using namespace std;
 
int comp(int a[]){
	for(int i = 0; i < 10; i++){
		if(a[i] == 0)
			return 1;
	}	
	return 0;
}
 
int main() {
	// your code goes here
 
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		long long n;
		cin >> n;
 
		long long count = 0;
 
		if(n == 0)
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		else{
			int k = 1;
			int a[10] = {0};
			while(comp(a) == 1){
				long long l = n * k;
				//cout << l << endl;
				while(l > 0){
					a[l % 10] = 1;
					l /= 10;
				}	
				//for(int i = 0; i < 10; i++)
				//	cout << a[i] << " ";
				//cout << endl;
				k++;
			}
			cout << "Case #" << i + 1 << ": " << n * (k - 1) << endl;
		}
	}
	return 0;
}