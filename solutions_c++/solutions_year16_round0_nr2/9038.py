#include <iostream>
#include <string>
#include <set>
#include <fstream>
#include <algorithm>

using namespace std;


long long revengeofthepancakes(string str) {
	long long resultat = 0;

	if (count(str.begin(), str.end(), '+') == str.size()) return 0;
	if (count(str.begin(), str.end(), '-') == str.size()) return 1;
	if (str.size() == 1 && str[0] == '-') return 1;
	while (count(str.begin(), str.end(), '+') != str.size()) {
		//Distribution des caractere;

		int i = str.size()-1;
		while (i >= 0 && str[i] != '-') i--;
	//	cout << i << endl;
		int cptplus = 0;
		str.erase(str.begin()+i+1, str.end());
		// nettoyage des + a la fin
		if (str[0] == '+') {
			int i = 0;
			while (i < str.size() && str[i] != '-') {
				str[i] = '-'; i++;
			}
			resultat++;
		}
		else {
			reverse(str.begin(), str.end());
			for (int j(0); j < str.size();++j) {
				if (str[j] == '+')str[j] = '-';
				else str[j] = '+';
				if (str[j] == '+')cptplus++;
			}
			resultat++;
		}
		if (cptplus == str.size())break;
		 i = 0;
		int k;
		while (i < str.size() && str[i] == '-')i++;
		k = i;
		while (i < str.size() && str[i] == '+')i++;
		if (i == str.size()) {
			for (int i(0); i < k; ++i) str[i] = '+';
			resultat++;
		}
		else if (i == 0) {
			while (i < str.size() && str[i] == '+')i++;
			k = i;
			while (i < str.size() && str[i] == '-')i++;
			if (i == str.size()) {
				for (int i(0); i < str.size(); ++i)str[i] = '+';
				resultat +=2;
			}
		}
		
	//	system("pause");
	}

	return resultat;
}
int main() {


	string N;
	int T;

	ifstream input("input.txt");
	ofstream output("output.txt");
	//cin >> T;
	input >> T;
	for (int i(1); i <= T; ++i)
	{
		//cin >> N;
		input >> N;
		output << "Case #" << i << ": " << revengeofthepancakes(N) << endl;
	}
	return 0;
}