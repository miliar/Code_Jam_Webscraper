#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

int main() {
	ofstream output;
	output.open("output.txt");
	int T;
	cin>>T;
	cin.ignore();
	for(int t=0; t<T; t++) {
		string ipstr;
		int count = 0;
		getline(cin,ipstr);
		int ipstr_length = ipstr.length();
		if(ipstr_length == 1) {
			if(ipstr[0] == '+') {
				output<<"Case #"<<(t+1)<<": "<<"0"<<endl;
			} else if(ipstr[0] == '-') {
				output<<"Case #"<<(t+1)<<": "<<"1"<<endl;
			}
		} else {
			if(ipstr[ipstr_length-1] == '-'){
				count = 1;
			}

			for (int i = 0; i < ipstr_length-1; ++i) {
				if(ipstr[i] != ipstr[i+1]) {
					count++;
				}
			}
			output<<"Case #"<<(t+1)<<": "<<count<<endl;
		}
	}
	output.close();
	return 0;
}