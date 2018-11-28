#include <cstdio>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream f;
	f.open("D-large.in");
	if (!f.is_open()) {
		cerr << "Could not open file.\n";
		return -1;
	}

	ofstream out;
	out.open("output_large.txt");
	if (!out.is_open()) {
		cerr << "Could not open output file.\n";
		return -1;
	}

	int t;
	f >> t;

	for (int q = 1; q <= t; ++q) {
		out << "Case #" << q << ": ";

		int n;
		f >> n;

		vector<double> naomi, ken;
		for(int i = 0; i < n; ++i) {
			double d;
			f >> d;
			naomi.push_back(d);
		}

		for(int i = 0; i < n; ++i) {
			double d;
			f >> d;
			ken.push_back(d);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		vector<double> naomi_war, ken_war;
		naomi_war = naomi;
		ken_war = ken;

		int war_result = 0;
		for (int i = 0; i < n; ++i) {
			double naomi_choice = naomi_war[i];
			auto ken_choice_it = find_if(ken_war.begin(), ken_war.end(), [&](double k) { return k > naomi_choice; });
			double ken_choice;
			if (ken_choice_it != ken_war.end())
				ken_choice = *ken_choice_it;
			else {
				ken_choice = *ken_war.begin();
				ken_choice_it = ken_war.begin();
			}
			
			ken_war.erase(ken_choice_it);

			if (naomi_choice > ken_choice)
				war_result++;
		}

		int war_result2 = 0;
		naomi_war = naomi;
		ken_war = ken;

		for(int i = 0; i < n; ++i) {
			double naomi_choice = naomi_war[i];
			double naomi_told;
			
			if (ken_war.size() > 1)
				if (naomi_choice < *ken_war.begin())
					naomi_told = (ken_war[ken_war.size()-1] + ken_war[ken_war.size()-2]) / 2;
				else
					naomi_told = 1.0;
			else
				naomi_told = naomi_choice;

			auto ken_choice_it = find_if(ken_war.begin(), ken_war.end(), [&](double k) { return k > naomi_told; });
			double ken_choice;

			if (ken_choice_it != ken_war.end())
				ken_choice = *ken_choice_it;
			else {
				ken_choice = *ken_war.begin();
				ken_choice_it = ken_war.begin();
			}

			ken_war.erase(ken_choice_it);

			if (naomi_choice > ken_choice)
				war_result2++;
		}

		out << war_result2 << " " <<  war_result << endl;
	}

}