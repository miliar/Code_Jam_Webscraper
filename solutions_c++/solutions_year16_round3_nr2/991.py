#include<iostream>
#include<math.h>
using namespace std;



int main(){
	
	int t;
	cin >> t;
	
	for(int iter = 0; iter < t; iter++){
		int b, m;
		cin >> b >> m;		
		
		cout << "Case #" << iter + 1 << ": ";
		
		//cout << b << endl;
		//cout << m << endl;
		int rr = m;
		m--;
		
		string s ="";
			
			while(m > 0){
				if(m%2 == 1)s = "1" + s;
				else s = "0" + s;
				m /= 2;
			}
		
		if(s.length() > b - 2)cout << "IMPOSSIBLE" << endl;
		else{
			cout << "POSSIBLE" << endl;
			
			cout << 0;
			if(rr == 0){
				for(int i = 0; i < b - 1; i++)cout << 0;
				cout << endl;
			}
			
			else{
				for(int i = 0; i < b - 2 - s.length(); i++)cout <<0;
				cout << s;			
				cout << 1 << endl;
			}
			
			
			for(int i = 0; i < b - 1; i++){
				for(int j = 0; j < i + 2; j++)cout << 0;
				for(int j = 0; j < b - i - 2; j++)cout << 1;
				cout << endl;
			}
		}
	}

	
	return 0;
}
