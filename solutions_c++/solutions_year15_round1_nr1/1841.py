#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm> 

using namespace std;

int main() {

	freopen("A-large.in", "r", stdin);
	
	long long cantTestCases;
	cin >> cantTestCases;
	for(long long nCase = 1; nCase <= cantTestCases; nCase++) {
		long long cantVector;
		cin >> cantVector;
		vector<long long> cosas;
		for(long long i = 0; i < cantVector; i++) {
			long long num;
			cin >> num;
			cosas.push_back(num);
		}
		long long anterior = cosas[0];
		long long difMaxima = 0;
		long long comidos = 0;
		for(long long i = 1; i < cantVector; i++) {
			long long actual = cosas[i];
			if(anterior - actual > difMaxima) {
				difMaxima = anterior - actual;
			}
			if  (actual < anterior) {
				comidos += anterior - actual;
			}
			anterior = actual;
		}
		long long losDeltiempo = 0;
		for(long long i = 0; i < cantVector-1; i++) {
			losDeltiempo += min(cosas[i], difMaxima);
		}
		cout << "Case #" << nCase << ": " << comidos << " " << losDeltiempo << endl;
	}
	return 0;
}