#include <iostream>
#include <string>
#include <set>

using namespace std ;

int main(){
	int t;
	int n;
	int i;
	int r;
	int last;
	string s;
			
	cin >> t;
	for(int k = 1 ; k <= t ; k++){
		cin >> s;
		
		r = 0;
		
		if(s.size() == 1){
			if(s[0] == '+'){
				cout << "Case #" << k << ": " << 0 << endl;
			}
			else{
				cout << "Case #" << k << ": " << 1 << endl;
			}
			continue;
		}
		
		i = s.size() - 1;
		if(s[i] == '-'){
			r++;
			last = 1;
		}
		else{
			last = 0;
		}
		
		i--;
		
		
		while(i >= 0){
			if( s[i] == '-'){
				
				if(last != 1){
					r++;
					last = 1;
				}
					
			}
			else{
				if(last != 0){
					if(r%2){
						r++;
					}
					last = 0;
				}
			}
			
			i--;
		}
		
		cout << "Case #" << k << ": " << r << endl;
		
	}
}

