#include <iostream>
#include <string>
#define config first
#define amount second
using namespace std;

string group(string a){
	string result = "";
	result += a[0];
	for(int i = 1; i < a.size(); i++){
		if(result[result.size() - 1] != a[i]){
			result += a[i];
		}
	}
	return result;
}



/*pair<string, int> calculate(string config){
	if(config.size() == 1){
		return (config == "-");
	}
	if(config[0] == "-" )
}*/

int main(){
	int t;
	pair<string, int> result;
	cin >> t;

	string tmpString;

	for(int k = 1; k <= t; k++){
		cin >> tmpString;
		tmpString = group(tmpString);
		cout << "Case #" << k << ": ";
		cout << tmpString.size() - 1 + (tmpString[tmpString.size() - 1] == '-');
		cout << endl;
	}
	return 0;
}