#include <iostream>
#include <fstream>
#include <string> 

using namespace std;

string process(int k, int g, int s);

int main(){
	ofstream myfile;
	myfile.open("output.txt");

	ifstream myReadFile;
	myReadFile.open("D-small-attempt3.in");

	int t;

	int K, G, S;

	myReadFile >> t;

	for (int i = 1; i < t + 1; i++) {
		myReadFile >> K >> G >> S;

		string ss = process(K, G, S);

		myfile << "Case #" << i << ": " << ss << endl;


	}
}

string process(int k, int g, int s){
	if (g == 1 && (s < k)){
		return "IMPOSSIBLE";
	}
	if (g>1 && s < ceil(k / 2)){
		return "IMPOSSIBLE";
	}
	if (k == 1){
		return "1";
	}

	string ss;

	if (g == 1){
		for (int j = 1; j < k+1; j++){
			ss += to_string(j);
			ss += " ";
		}
	}
	else{
		ss += "2";
		ss += " ";

		int c = 1;

		if (k <= 2){
			return ss;
		}
		else{
			while (c*2 < k){
				int j;
				if (c*2+1==k && k%2!=0){
					j = (k*c * 2) + c * 2 + 1;
				}
				else{
					j = (k*c * 2) + c * 2 + 2;
				}
				
				ss += to_string(j);
				ss += " ";
				c++;
			}
			
		}
	}
	return ss;
}