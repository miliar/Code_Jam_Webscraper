#include<iostream>
using namespace std;



int main(){
	
	int t;
	cin >> t;
	int j,p,s,k;
	
	for(int iter = 0; iter < t; iter++){
		
		cin >> j >> p >> s >> k;
		
		cout << "Case #" << iter + 1 << ": ";
		
		if(k >= s){
			cout << j*p*s << endl;
			for(int a = 0; a < j; a++){
				for(int b = 0; b < p; b++){
					for(int c = 0; c < s; c++)
					cout << a + 1 << " " << b + 1 << " " << c + 1 << endl;
				}
			}
		}
		else if(s == 1){
			cout << 1 << endl;
			cout << 1 << " " << 1 << " " << 1 << endl;
		}
		else if(s == 2){
			if(j == 1 && p == 1){
				cout << 1 << endl;
				cout << 1 << " " << 1 << " " << 1 << endl;
			}
			if(j == 1 && p == 2){
				cout << 2 << endl;
				cout << 1 << " " << 1 << " " << 1 << endl;
				cout << 1 << " " << 2 << " " << 2 << endl;
			}
			if(j == 2 && p == 2){
				cout << 4 << endl;
				cout << 1 << " " << 1 << " " << 1 << endl;
				cout << 1 << " " << 2 << " " << 2 << endl;
				cout << 2 << " " << 1 << " " << 2 << endl;
				cout << 2 << " " << 2 << " " << 1 << endl;
			}			
		}
		else{
			// s=3, k<=2;
			if(p == 1){
				if(k == 1){
					cout << 1 << endl;
					cout << 1 << " " << 1 << " " << 1 << endl;
				}
				else{
					cout << 2 << endl;
					cout << 1 << " " << 1 << " " << 1 << endl;
					cout << 1 << " " << 1 << " " << 2 << endl;
				}
			}
			else if(p == 2){
				if(j == 1){
					if(k == 1){
						cout << 2 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 2 << " " << 2 << endl;
					}
					else{
						cout << 4 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 1 << " " << 2 << endl;
						cout << 1 << " " << 2 << " " << 1 << endl;
						cout << 1 << " " << 2 << " " << 3 << endl;
					}
				}
				else{
					if(k == 1){
						cout << 4 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 2 << " " << 2 << endl;
						cout << 2 << " " << 1 << " " << 2 << endl;
						cout << 2 << " " << 2 << " " << 1 << endl;
					}
					else{
						cout << 8 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 1 << " " << 2 << endl;
						cout << 1 << " " << 2 << " " << 1 << endl;
						cout << 1 << " " << 2 << " " << 2 << endl;
						cout << 2 << " " << 1 << " " << 2 << endl;
						cout << 2 << " " << 1 << " " << 3 << endl;
						cout << 2 << " " << 2 << " " << 2 << endl;
						cout << 2 << " " << 2 << " " << 3 << endl;
					}
				}
			}
			else{
				if(k == 1){
					if(j == 1){
						cout << 3 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 2 << " " << 2 << endl;
						cout << 1 << " " << 3 << " " << 3 << endl;
					}
					else if(j == 2){
						cout << 6 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 2 << " " << 2 << endl;
						cout << 1 << " " << 3 << " " << 3 << endl;
						cout << 2 << " " << 1 << " " << 3 << endl;
						cout << 2 << " " << 2 << " " << 1 << endl;
						cout << 2 << " " << 3 << " " << 2 << endl;
					}
					else{
						cout << 9 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 2 << " " << 2 << endl;
						cout << 1 << " " << 3 << " " << 3 << endl;
						cout << 2 << " " << 1 << " " << 2 << endl;
						cout << 2 << " " << 2 << " " << 3 << endl;
						cout << 2 << " " << 3 << " " << 1 << endl;
						cout << 3 << " " << 1 << " " << 3 << endl;
						cout << 3 << " " << 2 << " " << 1 << endl;
						cout << 3 << " " << 3 << " " << 2 << endl;
					}
				}
				else{
					if(j == 1){
						cout << 6 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 2 << " " << 2 << endl;
						cout << 1 << " " << 3 << " " << 3 << endl;
						cout << 1 << " " << 1 << " " << 2 << endl;
						cout << 1 << " " << 2 << " " << 3 << endl;
						cout << 1 << " " << 3 << " " << 1 << endl;
					}
					else if(j == 2){
						cout << 12 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 1 << " " << 2 << endl;
						cout << 1 << " " << 2 << " " << 3 << endl;
						cout << 1 << " " << 2 << " " << 2 << endl;
						cout << 1 << " " << 3 << " " << 1 << endl;
						cout << 1 << " " << 3 << " " << 3 << endl;
						cout << 2 << " " << 1 << " " << 1 << endl;
						cout << 2 << " " << 1 << " " << 2 << endl;
						cout << 2 << " " << 2 << " " << 3 << endl;
						cout << 2 << " " << 2 << " " << 2 << endl;
						cout << 2 << " " << 3 << " " << 1 << endl;
						cout << 2 << " " << 3 << " " << 3 << endl;
					}
					else{
						cout << 18 << endl;
						cout << 1 << " " << 1 << " " << 1 << endl;
						cout << 1 << " " << 1 << " " << 2 << endl;
						cout << 1 << " " << 2 << " " << 3 << endl;
						cout << 1 << " " << 2 << " " << 1 << endl;
						cout << 1 << " " << 3 << " " << 2 << endl;
						cout << 1 << " " << 3 << " " << 3 << endl;
						
						cout << 2 << " " << 1 << " " << 2 << endl;
						cout << 2 << " " << 1 << " " << 3 << endl;
						cout << 2 << " " << 2 << " " << 1 << endl;
						cout << 2 << " " << 2 << " " << 2 << endl;
						cout << 2 << " " << 3 << " " << 3 << endl;
						cout << 2 << " " << 3 << " " << 1 << endl;
						
						cout << 3 << " " << 1 << " " << 3 << endl;
						cout << 3 << " " << 1 << " " << 1 << endl;
						cout << 3 << " " << 2 << " " << 2 << endl;
						cout << 3 << " " << 2 << " " << 3 << endl;
						cout << 3 << " " << 3 << " " << 1 << endl;
						cout << 3 << " " << 3 << " " << 2 << endl;
					}
				}
			}
		}
	}

	
	return 0;
}
