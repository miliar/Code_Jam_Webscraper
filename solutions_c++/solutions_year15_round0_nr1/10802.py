#include <iostream>
#include <cstring>
#include <cmath>

using namespace std; 

int main()
{
	
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	char cad[100]	;
	int L,T, car[100], cont, cp, k, i, j, Smax;
	
	
	cin>>T;
	

	for(int i = 1;i<=T;i++) {
		
	
		cin>>Smax;
	
	
		
		cin>>cad;
		
		for (int j=0; j<=Smax;j++) {
			switch (cad[j]) {
			case '0': car[j]=0; break;
			case '1': car[j]=1; break;
			case '2': car[j]=2; break;
			case '3': car[j]=3; break;
			case '4': car[j]=4; break;
			case '5': car[j]=5; break;
			case '6': car[j]=6; break;
			case '7': car[j]=7; break;
			case '8': car[j]=8; break;
			case '9': car[j]=9; break;
			}
		}
		

		
		cont=car[0]; 
		cp=0;
		
		for (int k=1; k<=Smax;k++) {
			if (car[k] != 0) {
				while (cont<k) {
					cont = cont +1;
					cp = cp  +1;
				}
			}
			
			cont = cont + car[k];
		}
		
		cout<<"Case #"<<i<<": "<<cp<<endl;	
	}	
	
	return 0;
}
