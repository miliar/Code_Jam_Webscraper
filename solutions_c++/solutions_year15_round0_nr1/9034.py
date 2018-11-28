#include <iostream>
#include <string>
typedef unsigned long long int LL;
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	LL t = 0;
	cin >> t;
	LL a = 0;
	string b = "";
	for(LL i = 0; i < t; i++) {
			cin >> a;
			cin >> b;
			LL wynik = 0;
			LL c[a+1]; 
			for(LL j = 0; j < a+1; j++) {
			    c[j] = (LL)(b.at(j) - '0');
				//if(b.at(j) == '0') wynik ++;
			}
			
		//	for(LL j = 0; j < a+1; j++) {
			//  cout << c[j] << " ";
			//}
		//	cout << endl;
			
			LL people = c[0]; 
			
			for(LL j = 1;  j < a+1; j++) {
			//	cout << c[j] << " " << j << endl;
				if(c[j] != 0) {
			//		cout << "IN" << endl;
						if(people < j) {wynik += (j-people);people+=(j-people);}
						people+=c[j];
				}
			}
			
			
			cout << "Case #" << i+1 << ": " << wynik << endl;
	}
	return 0;
}
