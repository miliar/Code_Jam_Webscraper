#include<iostream>
#include<string>
// #include<math.h>
#include<vector>
#include<algorithm>
// #include<map>
// #include<utility>
// #include<sstream>
// #include<ctype.h>
// #include<queue>
// #include<stack>

using namespace std;

int main(){
	int T, N;
	string s;
	char c1, c2;
	int cmpt = 1;

	cin >> T;
	for (int i = 0; i < T; i++) {
		int b = 0;
//cout << "debug #0\n";
		//acquisition des données
		cin >> N;
		vector<string> chaines;
		for (int j = 0; j < N; j++) {
			cin >> s;
			chaines.push_back(s);
		}
/*
for (int j = 0; j < N; j++) {
        for (unsigned int k = 0; k < chaines[j].size(); k++) {
                cout << chaines[j][k];
        }
        cout << "\n";
}
*/
//cout << "debug #1\n";
		//transformation des données
		vector<vector<int>> nombres;
		vector<int> temp0;
		vector<char> caracteres;
		c1 = chaines[0][0];
		int cmpt_car = 1;
		for (unsigned int k = 1; k < chaines[0].size(); k++) {
//cout << "debug #1.1 : k = ";
//cout << k << "\n";
			c2 = chaines[0][k];
//cout << "debug #1.2\n";
			if (c2 == c1) {
				cmpt_car ++;
			} else {
				caracteres.push_back(c1);
				temp0.push_back(cmpt_car);
				c1 = c2;
				cmpt_car = 1;
			}
		}
                caracteres.push_back(c1);
                temp0.push_back(cmpt_car);
		nombres.push_back(temp0);
//cout << "debug #2\n";
//                caracteres.push_back(c1);
//                nombres[0].push_back(cmpt_car);
		for (int j = 1; j < N; j++) {
	                vector<int> temp;
			c1 = chaines[j][0];
			cmpt_car = 1;
               	 	int numcar = 0;
			if (c1 != caracteres[numcar]) { /*cout << "bouh`n";*/ b = -1; }
			for (unsigned int k = 1; k < chaines[j].size(); k++) {
//cout << "coucou`n";
				c2 = chaines[j][k];
				if (c2 == c1) {
					cmpt_car ++;
				} else {
					numcar ++;
					temp.push_back(cmpt_car);
					c1 = c2;
					if (c1 != caracteres[numcar]) { b = -1; }
					cmpt_car = 1;
				}
			}
		if (c1 != caracteres[numcar]) { b = -1; }
		temp.push_back(cmpt_car);
//cout << "nbr.s before : " << nombres.size() << "\n";
		nombres.push_back(temp);
//cout << "nbr.s after : " << nombres.size() << "\n";
		}
//cout << "debug #3\n";
/*
cout << "Case #" << cmpt << ":\n";
for (unsigned int k = 0; k < caracteres.size(); k++) {
	cout << caracteres[k] << " ";
}
cout << "\n";
//cout << nombres.size() << "\n";
for (int j = 0; j < N; j++) {
//cout << "hey\n";
	for (unsigned int k = 0; k < nombres[j].size(); k++) {
		cout << nombres[j][k];
	}
	cout << "\n";
}
cout << "b = " << b << "\n";
*/
		//algo (small)
if (nombres[0].size() != nombres[1].size()) { b = -1; }
		int res = 0;
		if (b == 0) {
			for (unsigned int p = 0; p < caracteres.size(); p++) {
				int incr = nombres[0][p] - nombres[1][p];
				if (incr < 0) { res = res - incr; }
				else { res = res + incr; }
			}
		}
		//sortie
		if (b == 0) {
			cout << "Case #" << cmpt << ": " << res << "\n";
		} else {
                        cout << "Case #" << cmpt << ": Fegla Won\n";
		}
		cmpt++;
	}
}
