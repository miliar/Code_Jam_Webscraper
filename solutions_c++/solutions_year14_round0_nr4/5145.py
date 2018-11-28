#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <map>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	FILE *out;
	FILE *in;

	freopen_s(&in, "D-small-attempt0.in", "r", stdin);
	freopen_s(&out, "D-small-attempt0.out", "w", stdout);

	int T;
	cin >> T;

	for (int i = 1; i <= T; i++)
	{
		//double naomi[1000];
		//double ken[1000];

		deque<double> naomi1;
		deque<double> ken1;

		deque<double> naomi2;
		deque<double> ken2;

		int N;
		cin >> N;

		for (int j = 0; j < N; j++){
			double d;
			cin >> d;
			naomi1.push_back(d);
			naomi2.push_back(d);
		}

		for (int j = 0; j < N; j++){
			double d;
			cin >> d;
			ken1.push_back(d);
			ken2.push_back(d);
		}

		std::sort(naomi1.begin(), naomi1.begin()+N);
		std::sort(ken1.begin(), ken1.begin()+N);
		std::sort(naomi2.begin(), naomi2.begin() + N);
		std::sort(ken2.begin(), ken2.begin() + N);

		//War
		int war = 0;
		for (int j = 0; j < N; j++){
			double naomiNumber = naomi1.front();
			naomi1.pop_front();
			
			double kenNumber = 0.0;
			for (int k = 0; k < ken1.size(); k++){
				if (ken1[k] > naomiNumber){
					kenNumber = ken1[k];
					ken1.erase(ken1.begin() + k);
					break;
				}
			}
			
			if (kenNumber == 0.0){
				ken1.front();
				ken1.pop_front();
				war++;
			}
			

		}

		//Deceitful War
		int deceitfulWar = 0;
		for (int j = 0; j < N; j++){
			double naomiNumber = naomi2.front();
			naomi2.pop_front();

			double kenNumber = ken2.front();

			if (naomiNumber < kenNumber){
				ken2.pop_back();
			} else {
				ken2.pop_front();
				deceitfulWar++;
			}
		}
		//lower left corner

		cout << "Case #" << i << ": " << deceitfulWar << ' ' << war << endl;
	}

	//system("pause");
}