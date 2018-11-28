#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main() {
	ifstream fin("in");
	ofstream fout("out");
	int T = 0;
	fin >> T;
	string l;
	string ans;
	for (int TT = 0; TT < T; TT++) {
		int n;
		fin >> n;
		int dsum = 0;
		int sum2 = 0;
		int dl = 0;
		int arr[1200];
		fin >> arr[0];
		for (int i = 1; i < n; i++) {
			fin >> arr[i];
			if (arr[i] < arr[i-1]) dsum+=arr[i-1]-arr[i];
			if (arr[i-1]-arr[i] > dl) dl = arr[i-1]-arr[i];
		}
		for (int i = 0; i < n-1; i++) {
			sum2 += dl > arr[i] ? arr[i] : dl;
		}
		fout << "Case #" << TT+1 << ": " << dsum << " " << sum2 << endl;
	}
	return 0;
}
