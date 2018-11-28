#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
using namespace std;

bool palindrome(int nb){
	string s = to_string(nb);
	string s2(s.rbegin(), s.rend());
	int nb2 = atoi(s2.c_str());
	return (nb == nb2);
}

int main(int argc, char **argv){
	int borneMax = atoi(argv[1]);
	int borneTests = sqrt(borneMax);
	ifstream in("c.in", ios::in);
	ofstream out("c_out.txt", ios::out | ios::trunc);
	if (in && out){
		vector<int> v;
		for (int i=1;i<=borneTests;++i){
			if (palindrome(i) && palindrome(i*i)){
				v.push_back(i*i);
				cout << (i*i) << endl;
			}
		}
		int nbCandidats = v.size();
		int nbTours;
		in >> nbTours;
		for (int i=0;i<nbTours;++i){
			out << "Case #" << (i+1) << ": ";
			int inf, sup;
			in >> inf;
			in >> sup;
			int j=0;
			int debut = -1;
			do {
				if (v[j] >= inf){
					debut = j;
				}
				++j;
			} while (debut == -1);
			if (v[debut] > sup){
				out << "0" << endl;
			} else {
				while(v[j] <= sup && j<nbCandidats){
					++j;
				}
				out << (j-debut) << endl;
			}
		}
		out.close();
		in.close();
	}
	return 0;
}
