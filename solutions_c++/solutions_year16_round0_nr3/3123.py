#include <iostream>
#include <cstring>
#include <cmath>



using namespace std;


long long valueOf(string n, int base_of_n){
 
    char aux[n.size()], *end;
    strcpy(aux,n.c_str());
    return strtoll(aux,&end,base_of_n);
 
}


int main(){

	int tc;
	int n,j;
	cin>>tc;
	for(int i = 0; i < tc; i++){
		cin>>n>>j;
		int cnt = 0;
		cout<<"Case #1:"<<endl;

			if(n % 2 == 0){
				
				int theValue = 3;
				while(cnt != j){
					//cout<<"yes"<<endl;
				string res;
				string curr = "";
				for (i = 0; i < n-2; ++i) {  // assuming a 32 bit int
					string s = theValue & (1 << i) ? to_string(1) :to_string(0);
    				curr=  s + curr;
				}

				res = "1" + curr + "1";
				
				string factors = "";
				int count = 0;
				for(int base = 2; base <= 10; base++){

					long long num = valueOf(res,base);
					//cout<<"no"<<endl;
					
					for(long long k = 2; k <= sqrt(num); k++){

							if(num % k == 0){
								count++;
								factors += to_string(k) + " ";
								break;
							} 
					}


				}

				if(count == 9){
					cnt++;
					cout<<res<<" "<<factors<<endl;
				}
				theValue += 3;
			}
			}
			else{
				int theValue = 2;
				while(cnt != j){
				string res;
				string curr = "";
				for (i = 0; i < n-2; ++i) {  // assuming a 32 bit int
					string s = theValue & (1 << i) ? to_string(1) :to_string(0);
    				curr=  s + curr;
				}
				res = "1" + curr + "1";
				//cout<<res<<" ";
				string factors = "";
				int count = 0;
				for(int base = 2; base <= 10; base++){

					long long  num = valueOf(res,base);
					for(long long  k = 2; k <= sqrt(num); k++){

							if(num % k == 0){
								count++;
								factors += to_string(k) + " ";
								break;
							} 
					}

				}
				if(count == 9){
					cnt++;
					cout<<res<<" "<<factors<<endl;
				}
				

				theValue += 3;
			}


			}
			

		
    }

}

