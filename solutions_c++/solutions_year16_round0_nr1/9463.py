#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string find_answer(long s){
	if (s==0){
		return "INSOMNIA";
	}
	bool bitmap[10] = {false};
	int total = 0;
	int i = 1;
	while (total < 10){
		long temp = i * s;
		while ((temp > 0) && (total < 10)){
			int bittemp = temp % 10;
			
			if (!bitmap[bittemp]){
				//cout << "I'm here" << endl;
				//cout << temp << ',' << bittemp << endl;
				total++;
				bitmap[bittemp] = true;
			}
			//cout << temp << endl;
			temp = temp / 10;
		}
		i++;
	}
	return to_string((i-1)*s);
}

int main(int argc, char *argv[]) {
	int n;
	ifstream infile("A-large.in");
	//infile.open();
	ofstream outfile("outputlarge.txt");
	//outfile.open();

	infile >> n;
	for (int i = 0; i < n; i++){
		long s;
		infile >> s;
		outfile << "Case #"<< i+1 << ": "<< find_answer(s) << endl;
	}	
	
	infile.close();
	outfile.close();
}