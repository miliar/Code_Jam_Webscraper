#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
void main(){
	int cases;
	ifstream input;
	ofstream output;
	output.open("output.txt");
	input.open("input.in");
	input >> cases;
	for (int n = 0; n != cases; ++n){
		int l;
		double temp;
		int a=0, b=0;
		input >> l; 
		vector<double> N;
		vector<double> K;
		for (int i = 0; i != l; ++i){
			input >> temp; 
			N.push_back(temp);
		}
		for (int i = 0; i != l; ++i){
			input >> temp; 
			K.push_back(temp);
		}
		if (N.end() - N.begin() > 1){
			sort(N.begin(), N.end());
			sort(K.begin(), K.end());
		}
		int y = 0, z = 0;
		while (y != N.end() - N.begin()){
			if (N[y]>K[z]){
				++a, ++y, ++z;
			}
			else{
				++y;
			}
		}
		int s = 0, t = 0,sum=0;
		while (s != K.end() - K.begin()){
			if (K[s] > N[t]){
				++s, ++t, ++sum;
			}
			else
				++s;
		}
		b = K.end() - K.begin() - sum;
		output << "Case #" + to_string(n + 1) + ": " + to_string(a) + " " + to_string(b) << "\n"; 
	}
}