#include<vector>
#include<iostream>
#include<iomanip>
#include<string>
#include<sstream>
using namespace std;
void main(){
	int cases;
	cin >> cases;
	vector<string> answer;
	for (int i = 0; i != cases; ++i){
		long double c, f, x;
		cin >> c >> f >> x;
		int n = ((x / c)*f - 2) / f;
		if (x > c){
			long double time = x / (2 + n*f);
			for (int k = 0; k != n; ++k){
				time += c / (2 + (k*f));
			}
			stringstream buffer;
			buffer << "Case #" + to_string(i + 1) + ": " << setprecision(15) << time;
			answer.push_back(buffer.str());
		}
		else{
			long double m = x / 2;
			stringstream buffer;
			buffer << "Case #" + to_string(i + 1) + ": " << setprecision(15) << m;
			answer.push_back(buffer.str());
		}
	}
	for (auto i : answer)
		cout << i << endl;
}