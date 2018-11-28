#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int main(){
	int t, m, a[10];
	long long n, temp;
	string s;
	cin >> t;
	for(int i = 1; i <= t; i++){
		for(int j = 0; j < 10; j++)
			a[j] = 0;
		cin >> n;
		if(n == 0)
			cout << "Case #" << i << ": INSOMNIA\n";
		else{
			m = n;
			while(1){
				int flag = 0;
				temp = n;
				while(temp){
					a[temp % 10]++; 	
					temp /= 10;
				}
				for(int j = 0; j < 10; j++){
					if(a[j] > 0)
						flag++;
				}
				if(flag == 10)
					break;
				else
					n += m;
			}
			cout << "Case #" << i << ": " << n << endl;
		}
	}
	return 0;
}
