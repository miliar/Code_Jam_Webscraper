#include <iostream>
#include <string>
using namespace std;
int main(){
	string out, source;
	int t;
	cin >> t;
	for(int k = 1; k <= t; k++){
		cin >> source;
		out = source[0];
		for(int i=1;i<source.size();i++){
			if(out[0] <= source[i]){
				out = source[i] + out;
			} else {
				out = out + source[i];
			}
		}
		cout << "Case #" << k << ": " << out << endl;
	}
	return 0;
}