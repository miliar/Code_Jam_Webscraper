#include <iostream>
using namespace std;


long flip(long n){
	long fliped =0;
	while(n){
		fliped*=10;
		fliped+=n%10;
		n=n/10;
	}
	return fliped;
}

int main(){
	int t, caso=1;
	long n, min;
	cin >> t;
	while(t--){
		cin >> n;
		min = 1;
		long i=1;
		while(i<n){
			bool doflip=true;
			long fliped = flip(i);
			long dif = fliped - i;
		//	cout<< i << " fliped "<<fliped<<" dif "<<dif<<endl;
			if(dif>1 && fliped <=n ){
				for(long j=i+1;j<fliped;j++){
					long fliped2 = flip(j);
					if(fliped2 <=n && fliped2 > fliped 
									&& dif<(fliped2-i-(j-i))){
						doflip =false;
		//				cout << fliped<<" rejeitado pelo "<< j<<endl;
						break;	
					}	
				}			
			}else{
				doflip = false;
			}	

			if(doflip){
				i=fliped;
			}else{
				i++;
			}

			min++;
		}				
		cout << "Case #"<< caso++ << ": "<<min<<endl;
	} 
	return 0;
}
