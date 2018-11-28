#include <iostream>
using namespace std;
bool seen[10] = {false};
int main() {
	// your code goes here
	long long t ;
	cin >> t ;
	for( int i = 0 ; i < t ; i++){
		int ar[10] = {0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 };
		long long n ;
		cin >> n ;
		if(n == 0){
			cout <<"Case #"<<i+1<<": INSOMNIA\n";
		}else{
			long long j = 1 , x = 0 , num  , dig , sum = 0;
			while(x < 1){
				num = j * n;
				while(num > 0){
					dig = num % 10;
					num = num / 10;
					if(seen[dig]==0){
						seen[dig] = 1;
						sum++;
					}
				}
				if(sum == 10){
					cout << "Case #"<<i+1<<": "<< n * j << endl;
					break;
				}else{
					j++;
				}
			}
		}
		for( int v = 0 ; v < 10 ; v++){
			seen[v] = 0;
		}
	}
	return 0;
}