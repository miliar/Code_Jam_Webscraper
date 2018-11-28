#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main () {
	
	ifstream in ("A-large.in");
	ofstream cout("A-large.out");
	int T;
	in>>T;
	
	for (int t=0; t<T; t++) {
		int max;
		in>>max;
		
		int f = 0;
		char temp; 
		in>>temp;
		
		int runningSum = temp - '0';
		
		for (int i=1; i<=max; i++) {
			in >> temp;
			if(temp - '0' > 0 && runningSum + f < i) {
				f += i - runningSum - f;			
			}
			runningSum += temp - '0';
			
			if(i != max && runningSum >= max) {
				string s; in>>s; break;
			}
		}
		
		cout<<"Case #"<<t+1<<": "<<f<<endl;
	}
	
	return 0;
}
