#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

double kenOptimal(double value, vector<double> vec) {
	double optimalval = 1.0;
	for (int i = 0; i < vec.size(); i++) {
		if (vec[i] > value && vec[i] < optimalval) optimalval = vec[i];
	}
	if (optimalval == 1.0) {
		for (int i = 0; i < vec.size(); i++) {
			if (vec[i] < optimalval) optimalval = vec[i];
		}
	}
	return optimalval;
}

double highest(vector<double> v) {
	double optimalval = 0.0;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] > optimalval) optimalval = v[i];
	}
	return optimalval;
}

double lowest(vector<double> v) {
	double optimalval = 1.0;
	for (int i = 0; i < v.size(); i++) {
		if (v[i] < optimalval) optimalval = v[i];
	}
	return optimalval;
}

bool winnable(vector<double> n, vector<double> k) {
	for (int i = 0; i < n.size(); i++) {
		if (n[i] < k[i]) return false;
	}
	return true;
}

int main() {
	ifstream fin("D-large.in");
	ofstream fout("output.out");
	int inputs;
	fin >> inputs;
	for (int i = 0; i < inputs; i++) {
		vector<double> k, n, tempa, tempb;
		int blocks, deceitful = 0, normal = 0;
		double weight, optimal;
		n.clear();
		k.clear();

		fin >> blocks;
		for (int j = 0; j < blocks; j++) {
			fin >> weight;
			n.push_back(weight);
		}
		for (int j = 0; j < blocks; j++) {
			fin >> weight;
			k.push_back(weight);
		}
		sort(n.begin(), n.end());
		sort(k.begin(), k.end());

		tempa = n;
		tempb = k;
		while (!winnable(tempa, tempb)) {
			tempa.erase(remove(tempa.begin(), tempa.end(), lowest(tempa)), tempa.end());
			tempb.erase(remove(tempb.begin(), tempb.end(), highest(tempb)), tempb.end());
		}
		deceitful = tempa.size();

		tempa = k;
		for (int j = 0; j < blocks; j++) {
			optimal = kenOptimal(n[j],tempa);
			if (n[j] > optimal) normal++;
			tempa.erase(remove(tempa.begin(), tempa.end(), optimal), tempa.end());
		}

		fout << "Case #" << i + 1 << ": " << deceitful << " " << normal << endl;
	}
}