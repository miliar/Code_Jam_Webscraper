#include <iostream>
#include <limits>
#include <string>
#include <sstream>
using namespace std;
int main(){
  int t, n, m;
  cin >> t;
  for (int c = 1; c <= t; c++){
	bool f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, ok;
	f0 = f1 = f2 = f3 = f4 = f5 = f6 = f7 = f8 = f9 = ok = false;
    cin >> n;
	for (int i = 1; i <= SHRT_MAX; i++){
		std::ostringstream stm;
        stm << (n * i);
        string str = stm.str();
        
		for (int j = 0; j < str.length(); j++){
			switch (str[j]){
				case '0': f0 = true; break;
				case '1': f1 = true; break;
				case '2': f2 = true; break;
				case '3': f3 = true; break;
				case '4': f4 = true; break;
				case '5': f5 = true; break;
				case '6': f6 = true; break;
				case '7': f7 = true; break;
				case '8': f8 = true; break;
				case '9': f9 = true; break;
			}
		}
		
		if (f0 && f1 && f2 && f3 && f4 && f5 && f6 && f7 && f8 && f9){
			ok = true;
			cout << "Case #" << c << ": " << (str) << endl;
			break;
		}
	}
		
	if (!ok){
    	cout << "Case #" << c << ": INSOMNIA" << endl;
	}
  }
}
