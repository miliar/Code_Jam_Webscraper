#include<iostream>
#include<cstdio>
using namespace std;
int main(){		
		int t;
		cin>>t;
		int caso = 1;
		while(t--){
			
				double C, F, X;
				cin>>C>>F>>X;
//cout<<"?\n";
			double actual = 2;
				double nueva;
				double resp = 0.0;
				for(;;){
					nueva = actual + F;
					if(C*nueva + X*actual >= X*nueva){												
							//cout<<"Case #"<< caso++ <<": " <<resp + X/actual << "\n";
							printf("Case #%d: %.7lf\n",caso++,(resp + X/actual));
							break;
					}
					else{
							resp += C / actual;
							actual += F;							
					}
					
				}
				
		}
return 0;
}
