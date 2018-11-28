#include<iostream>
#include<sstream>
#include<fstream>
#include<string>
#include<vector>
#include<set>
#include<stack>
using namespace std;

int main(){
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
	int T;
	cin >> T;
	for (int i = 0; i < T; i++){
		cout << "Case #" << (i + 1) << ": ";
		double C, F, X;
		cin >> C >> F >> X;
		double s = 0;
		double d = 2;
		while (X / d >= C / d + X / (d + F)){
			s += C / d;
			d += F;
		}
		s += X / d;
		cout.precision(7);
		cout << fixed << s;
		cout << "\n";
	}
}