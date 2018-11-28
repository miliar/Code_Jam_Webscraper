#include <iostream>
#include <string>
#include <fstream>

using namespace std;

inline double miniTime(double perS, double X){
	return(X / perS);
}

int main(int argc, char* argv[]){
	int n;
	cin >> n;
	int cases = 0;
	string *output = new string[n];
	while (n > 0){
		double perS = 2;
		double cookies = 0;
		/*
			C = How much to farm.
			F = How much to add TO per second.
			X = Goal.
		*/
		double input[3];//0=C, 1=F,2=X
		for (int i = 0; i < 3; i++)
			cin >> input[i];
		bool found = false;
		double time = miniTime(perS, input[2]);
		double extraTime = 0;
		int count = 0;
		while (!found){
			extraTime += miniTime(perS, input[0]);
			perS += input[1];
			double newTime = (extraTime + miniTime(perS, input[2]));
			if (time >= newTime){
				time = newTime;
				count = 0;
			}
			if (count >= 100)
				found = true;
			count++;
		}
		output[cases++] = "Case #" + to_string(cases+1) + ": " + to_string(time);
		n--;
	}
	ofstream file("output.txt");
	for (int i = 0; i < cases; i++){
		file << output[i] + "\n";
	}
	file.close();
	cin.ignore();
	cin.ignore();
	return 0;
}