//#include <iostream>
#include <vector>
#include <fstream>
#include <iomanip>
#include <algorithm>
using namespace std;

int deceit(const vector<double>& naomi, const vector<double>& ken);
int war(const vector<double>& naomi, const vector<double>& ken);


int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	//out << setprecision(7) << std::fixed;
	for (int t=0; t < T; t++) {
		int n;
		in >> n;
		vector<double> naomi(n), ken(n);
		for (int i=0; i <n; i++)
			in >> naomi[i];
		for (int i=0; i <n; i++)
			in >> ken[i];
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		out << "Case #" << t+1 << ": ";
		out << deceit(naomi, ken) << " " << war(naomi, ken) << endl;
	}//case
}

int deceit(const vector<double>& naomi, const vector<double>& ken)
{
	int count(0), n = 0;
	for (int i = 0; i < ken.size(); i++) {
		while(n < naomi.size() && naomi[n] < ken[i])
			n++;
		if (n >= naomi.size()) break;
		count++;
		n++;
	}
	return count;
}//deceit

int war(const vector<double>& naomi, const vector<double>& ken)
{
	int count(0), k=0;
	for (int i =0; i < naomi.size(); i++) {
		while (k < ken.size() && naomi[i] > ken[k])
			k++;
		if (k >= ken.size()) { count += naomi.size() - i; break;}
		k++;
	}
	return count;
}