#include <iostream>
using namespace std;

void digit(long long p, long long a[]) {

	while(p != 0){
		a[p%10] = 1;
		p = p/10;
	}
}

int main()
{
	long long t;
	cin >> t;

	for(long long i = 0; i < t; i++){

			long long a[10];
			long long n;
			cin >> n;

			
			for(long long j = 0; j < 10; j++){
				a[j] = 0;
			}
            
            if(n == 0) {
            	 cout << "Case #"<<i+1 << ": " <<"INSOMNIA" << endl;
                 continue;
            }
            long long j;
			for( j = 1; ; j++){
				long long fl = 0;
				long long p = n * j;
				
				digit(p,a);

				for(long long k = 0; k < 10; k++){
					if(a[k] == 0) {
				
						fl = 1;
						break;
					}

				}

				
				if(fl == 0) {
					break;
				}


			}
            
               
            cout << "Case #"<<i+1 << ": " <<n*j << endl;



	}

	return 0;
}