#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>     /* strtol */

using namespace std;
long long int isPrime(long long int number){

    if(number < 2) return 1;
    if(number == 2) return 0;
    if(number % 2 == 0) return 2;
    for(long long int i=3; i * i < number; i+=2){
        if(number % i == 0 ) {
//			cout << " " << i << endl;
			return i;
		}
    }
	
    return 0;

}

int main(int argc, char* argv[]) {
	int t;
	int n;
	int j;
	
	int done = 0;
	int rem = 0;
//	std::vector<int> d;
//	int c[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	
	freopen("input_file.in","r", stdin);
	freopen("output_file.out","w", stdout);
	cin >> t;
	
	for(int i = 0; i < t; i++){
		cin >> n;
		cin >> j;
		char bin[n+2];
		bin[0] = '1';
		bin[n-1] = '1';
		bin[n] = '\0';
		cout << "Case #" << i + 1 << ':' << endl;
		for(int k = 1; k <= n-2; k++){
			bin[k] = '0';			
		}			
		done = 0;

		while(done < j){
			rem = 1;
			for(int k = n-2; k > 0; k--){
				bin[k] += rem;
				if(bin[k] == '2'){
					bin[k] = '0';
					rem = 1;
				}
				else{
					rem = 0;
					//done = j;
				}
			}
			bool no = false;
			long long int ten;
			long long int nt[11];
			long long int nontr;
			
			for(int l = 2; l <= 10; l++){
				ten = strtoll(bin, '\0', l);
			//	cout << ten << ' ' << endl;
				nontr = isPrime(ten);				
				if(nontr == 0){
					no = true;
					break;
				}
				nt[l] = nontr;
			}
			if(!no){
				done++;
				cout << bin << ' ';// << done;
				for(int l = 2; l <= 10; l++){
					cout << nt[l] << ' ';
				}
				cout << endl;
			//	cout << "Case #" << i + 1 << ": " << ten << endl;
			}
		}		

	}
	return 0;
}
