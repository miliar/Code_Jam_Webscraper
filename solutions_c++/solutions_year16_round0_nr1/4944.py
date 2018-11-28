#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream> 

using namespace std;


int main(){
	ifstream cin("input.txt"); 
	int t; cin >> t; 
	int total_cases   = t; 

	while(t--){
		int a[10]; 
		for(int i = 0; i < 10; i++){ a[i] = 0; }
		int digit_counter = 0; 
		long long counter = 1; 
		int curr          = 0; 

		long long n; cin >> n; 
		if(n == 0){
			cout << "Case #" << total_cases-t << ": " << "INSOMNIA" << endl; 
			continue; 
		}
		long long curr_n = n; 
		while(1){
			if(counter == 10000000){
				cout << "Case #" << total_cases-t << ": " << "INSOMNIA" << endl; 
				break; 
			}
			/* Finding digits in n. */
			long long temp = curr_n; 
			if(temp == 0){
				a[temp]++; 
			}
			else{
				while(temp != 0){
					int r = temp % 10; 
					temp /= 10; 
					if(a[r] == 0){
						a[r]++; 
						digit_counter ++; 
					}
				}
			}
			if(digit_counter == 10){
				cout << "Case #" << total_cases-t << ": " << curr_n << endl; 
				break; 
			}
			//cout << "dc: " << digit_counter << endl; 
			counter ++; 

			curr_n = (counter * n); 
			//cout << "curr_n: " << curr_n << endl; 
			
		}//while(1){...}
	}
	return 0; 
}