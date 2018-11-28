#include <iostream>
#include <fstream>
#include <iomanip> 
#include <algorithm>
#include <vector>
using namespace std;
class node{
public:
	node(double m, int b):mass(m), bel(b){
	}
	double mass;
	int bel;
};

int main() {
	ifstream fin("D-large.in");
	ofstream fout("out.txt");
	int n, t;
	double nom[1000], ken[1000];
	double tmp;
	int y, z;
	fin >> t;
	for (int k = 0; k < t; k++){
		y = 0;
		z = 0;
		
		fin >> n;
		for (int i = 0; i < n; i++){
			fin >> nom[i];
		}
		for (int i = 0; i < n; i++){
			fin >> ken[i];
		}
		vector<double> nomv(nom, nom + n);
		vector<double> kenv(ken, ken + n);
		sort(nomv.begin(), nomv.end());
		sort(kenv.begin(), kenv.end());
		int headnom = 0, headken = 0, tailken = n - 1, tailnom = n - 1;
		while (true){
			if (nomv[headnom] > kenv[headken]){
				y++;
				headken++;
				headnom++;
			}
			else{
				headnom++;
				tailken--;
			}
			if (headnom == n)
				break;
		}

		vector<double> nomv1(nom, nom + n);
		vector<double> kenv1(ken, ken + n);
		sort(nomv1.begin(), nomv1.end());
		sort(kenv1.begin(), kenv1.end());
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				if (nomv1[i] < kenv1[j]){
					kenv1[j] = -1;
					break;
				}
			}
		}
		for (int i = 0; i < n; i++){
			if (kenv1[i] != -1)
				z++;
		}

		
		
		fout << "Case #" << k + 1 << ": ";
		fout << y << " " << z << endl;
	}
	fin.close();
	fout.close();
	return 0;
}