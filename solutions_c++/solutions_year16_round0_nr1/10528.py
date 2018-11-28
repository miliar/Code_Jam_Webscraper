#include <iostream>
#include <fstream>
#include <limits.h>

using namespace std;

int main() {
	int i,k,l;
	long int num;
	int rem=0, count=0;
	cin>>i;
	bool a[10];
	for ( int j=0; j<i; j++ ){
		cin>>k;
		count = 0;
		if (k==0){
			cout<<"Case #"<<j+1<<": INSOMNIA"<<std::endl;
			continue;
		}
		for( int g=0; g<10;g++ )
			a[g] = 0;
		for( int l=1; l<(k*100); l++ ) {
			num = l*k;
			rem = num%10;
			num /= 10;
			if (a[rem] != 1) {
				a[rem] = 1;
				count++;
			}
			while(num > 0 && count != 10) {
				rem = num%10;
				num = num/10;
				if(a[rem] != 1){
					a[rem] = 1;
					count++;
				}
			}
			if( count == 10 ){
				cout<<"Case #"<<j+1<<": "<<l*k<<std::endl;
				break;
			}
		}
	}
	return 0;
}
