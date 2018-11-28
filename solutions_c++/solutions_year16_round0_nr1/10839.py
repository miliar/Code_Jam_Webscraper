#include<iostream>
#include<cstdio>
#include<fstream> 
using namespace std;

int main(){
	int t, i, count, j, a[10], k;
	ifstream file1;
	ofstream file2;
	file1.open("A-large.in");
	file2.open("SHEPP1.out");
	file1 >> t;
	long long int x, temp;
	for(i = 1; i <= t; i++) {
		for(j = 0; j < 10; j++) {
			a[j] = 0;
		}
		count = 0;
		file1 >> x;
		if(x == 0) {
			file2 << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		k = 0;
		while(count != 10) {
			k++;
			temp = x * k;
			while(temp) {
				if(a[temp % 10] == 0) {
					a[temp % 10] = 1;
					count++;
				}
				temp = temp / 10;
			}
		}
		file2 << "Case #" << i << ": " << x * k << endl;
	}
	file1.close();
	file2.close();
	return 0;
} 
 
