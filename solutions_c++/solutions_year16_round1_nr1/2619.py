#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int main() {
	int numberOfCases, i = 0;
	string N;

	cin >> numberOfCases;
	while (cin >> N) {
		string resp = "";
		resp.push_back(N[0]);
		for (unsigned int i = 1; i < N.length(); i++) {
			if (N[i] < resp[0])
				resp += N[i];
			else
				resp = N[i] + resp;
		}
		cout << "Case #" << ++i << ": " << resp << endl;
	}
}
