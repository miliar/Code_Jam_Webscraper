#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <math.h> 


using namespace std;

#define ll long long
#define ui unsigned int
#define debug(a) cout << #a << ": " << a << endl;
#define debugVector(a) cout << #a << ": "; for(ui i; i < a.size(); i++) {cout << a[i] << " ";} cout << endl;
#define pb(a) push_back(a)
#define init(); ofstream fOut; fOut.open ("result.txt");
#define case(i) fOut << "Case #" << (i) << ": "; cout << "Case #" << (i) << endl;

int main()
{
    init();
    ui tests; cin >> tests;

    for (ui i = 1; i <= tests; i++) {
    	int feglaWon = 0;
		int N; cin >> N;
		vector< pair <int, char > > words[100];

		string tmp;
		for (int k = 0; k < N; k++) {
			cin >> tmp;
			char cur = tmp[0];
			int count = 1;
			for (int l = 1; l < tmp.length(); l++) {
				if (tmp[l] == cur) {
					count++;
				} else {
					words[k].pb(make_pair (count, cur));
					cur = tmp[l];
					count = 1;
				}
			}
			words[k].pb(make_pair (count, cur));
		}

		//same size
		int size = words[0].size();
		for ( int k = 1; k < N; k++) {
			if (size != words[k].size()) {
				feglaWon = 1;
			}
		}

		debug(size); debug(feglaWon);

		vector<int> averages;
		for (int k = 0; (k < size) && !feglaWon ; k++) { //letters
			double avg = 0;
			char cur = words[0][k].second;
			for (int l = 0; l < N; l++) { //words
				if (cur == words[l][k].second) {
					avg += words[l][k].first;
				} else {
					feglaWon = 1;
				}
			}
			avg /= N;
			debug(avg);
			int average = lrint(avg);
			averages.pb(average);
		}
		
		cout << "averages: ";
		for ( int x = 0; x < averages.size(); x++) {
			cout << averages[x] << " ";
		} cout << endl;

		int moves = 0;
		for (int k = 0; (k < size) && !feglaWon ; k++) { //letters
			for (int l = 0; l < N; l++) { //words
				moves += abs(averages[k] - words[l][k].first);
			}
		}



		case(i);

		if (feglaWon) {
			fOut << "Fegla Won" << endl;
			cout << "fegla" << endl;
		} else {
			fOut << moves << endl;
			cout << moves << endl;
		}
    }

}
