#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

void initialCoin(vector<int>& coin) {
	*(coin.begin()) = 1;
	*(coin.end() - 1) = 1;
	for (int i = 1; i < coin.size() - 1;i++) {
		coin[i] = 0;
	}
	return;
}

void combine(vector<int>&a, int n, int m, vector<int>&b, const int M, vector<vector<int>>& result) {
	for (int i = n; i >= m; i--)
	{
		b[m - 1] = i - 1;
		if (m > 1)
			combine(a, i - 1, m - 1, b, M, result);
		else
		{
			vector<int> temp;
			for (int j = M - 1; j >= 0; j--)
				temp.push_back(a[b[j]]);
			result.push_back(temp);
			temp.clear();
		}
	}
}

void generateCoin(vector<int> coin, int layer, vector<vector<int>>& coinSet) {
	vector<int> a(coin.size() - 2);
	vector<vector<int>> result;
	for (int i = 0; i < a.size(); i++) {
		a[i] = i + 1;
	}
	vector<int> b(layer);
	combine(a, a.size(), layer, b, layer, result);
	for (int i = 0; i < result.size(); i++) {
		vector<int> temp = coin;
		for (int j = 0; j < result[i].size(); j++) {
			temp[result[i][j]] = 1;
		}
		coinSet.push_back(temp);
	}
	return;
}

bool primeCheck(unsigned long long num, vector<unsigned long long>& div) {
	for (unsigned long long i = 2; i <= sqrt(num); i++) {
		if (num%i == 0) {
			div.push_back(i);
			return false;
		}
	}
	return true;
}
bool checkCoin(const vector<int>& coin, ofstream& out) {
	vector<unsigned long long> div;
	for (int base = 2; base <= 10; base++) {
		unsigned long long sum = 0;
		for (int i = 0; i < coin.size(); i++) {
			sum += coin[coin.size() - 1 - i] * pow(base, i);
		}
		if (primeCheck(sum, div)) {
			div.clear();
			return false;
		}
	}
	for (int i = 0; i < coin.size();i++) {
		cout << coin[i];
		out << coin[i];
	}
	for (int i = 0; i < coin.size();i++) {
		cout << coin[i];
		out << coin[i];
	}
	cout << ' ';
	out << ' ';
	for (int i = 0; i < div.size();i++) {
		cout << div[i] << ' ';
		out << div[i] << ' ';
	}
	cout << endl;
	out << endl;
	return true;
}

int main() {
	string temp;
	ifstream file("C-large.in");
	ofstream out("C-output.out");
	int T, N, J;
	file >> temp;
	T = stoi(temp);
	file >> temp;
	N = stoi(temp);
	file >> temp;
	N = N / 2;
	J = stoi(temp);
	vector<int> coin(N);
	vector<vector<int>> coinSet;
	initialCoin(coin);
	int layer = 1, count = 0;
	cout << "Case #1:" << endl;
	out << "Case #1:" << endl;
	//check initial array
	if (checkCoin(coin, out)) count++;
	while (count < J) {
		vector<int> temp;
		generateCoin(coin, layer, coinSet);
		for (int i = 0; i < coinSet.size(); i++) {
			if (checkCoin(coinSet[i], out)) count++;
			if (count >= J) break;
		}
		coinSet.clear();
		layer++;
		if (layer >= coin.size() - 3) break;
	}

}