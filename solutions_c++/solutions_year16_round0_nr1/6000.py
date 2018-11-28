#include <iostream>
#include <cmath>
using namespace std;

int main (){
	int ncases;
	unsigned long long n;
	unsigned long long orign;
	unsigned long long ncopy;
	bool seen[10] = {false};
	cin >> ncases;
	for(int i = 0; i < ncases; i++){
		for(int j = 0; j < 10; j++) seen[j] = false;
		cin >> n;
		orign = n;	
		if(n == 0){
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		}else{
			ncopy = n;
			while(ncopy > 0){
				int digit = ncopy % 10;
				ncopy /= 10;
				seen[digit] = true;
			}
			while(seen[0] != true ||
				  seen[1] != true ||
				  seen[2] != true ||
				  seen[3] != true ||
				  seen[4] != true ||
				  seen[5] != true ||
				  seen[6] != true ||
				  seen[7] != true ||
				  seen[8] != true ||
				  seen[9] != true){
				ncopy = n;
				while(ncopy > 0){
					int digit = ncopy % 10;
					ncopy /= 10;
					seen[digit] = true;
				}
				n += orign; 
			}
			cout << "Case #" << i+1 << ": " << n-orign << endl;
		}
	}
  
	return 0;
}


