#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    int t, x, r, c, product;
    cin >> t;
           
    for(int i=0; i<t; i++){
    	cin >> x;
    	cin >> r;
		cin >> c;
		product = r*c;
		if(x > 2 && product <= x){
			cout << "Case #" << i+1 << ": RICHARD" /*<< "pro less" */<< endl;
		}else{
			if(product % x != 0)
				cout << "Case #" << i+1 << ": RICHARD" /*<< "not divi" */<< endl;
			else if(r < x-1 || c < x-1){
				cout << "Case #" << i+1 << ": RICHARD" /*<< "r < x-1" */<< endl;
			}
			else{
				cout << "Case #" << i+1 << ": GABRIEL" << endl;
			}	
		}
	}
}
