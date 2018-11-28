#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main (){
	int ncases;
	cin >> ncases;
	cin.ignore();
	string line;
	for(int i = 1; i <= ncases; i++){
		getline(cin,line);
		while(line[line.length()-1] == '+') line.erase(line.length()-1,1);
//		cout << line << " " << line.length() <<  endl;
		char last = line[0];
		int result = 1;
		for(int j = 0; j < (int)line.length(); j++){
			if(line[j] != last){
				result++;
			}
			last = line[j];

		}
		if(line.length() == 0) result = 0;
		cout << "Case #" << i << ": " << result << endl;
	}


  
	return 0;
}


