#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std ;

const int N = 1005;
const int INF = 1<<25;


int main(){
	int tc;
	int n;
	double she[N];
	double he[N];
	int a[2*N];
	enum {Naomi=0, Ken=1};
	ifstream cin;
	cin.open ("D-large.in");

	cin >> tc;
	for (int t = 1; t <= tc; ++t) {

		cin>>n;
		for (int i = 0; i < n; ++i)
			cin>>she[i];
		she[n] = INF;

		for (int i = 0; i < n; ++i)
			cin>>he[i];
		he[n] = INF;

		sort(she, she+n);
		sort(he, he+n);


		for (int k = 0, i = 0,j = 0; k < 2*n; ++k) {
			if (she[i]<he[j]){
				a[k] = Naomi;
				i++;
			}
			else {
				a[k] = Ken;

				j++;
			}
		}

		int optimal_score = 0; //ken optimal score;
		int cheat_score = 0; // Naomi cheating score;

		int optimal_level = 0;
		int cheat_level = 0;

		for (int i = 0; i < 2*n; ++i) {
			if (a[i] == Naomi){
				// assuming optimal play
				optimal_level++;

				// assuming cheating play
				if (cheat_level>0){
					cheat_level--;
					cheat_score++;
				}

			}else {
				// assuming optimal play
				if (optimal_level>0){
					optimal_level--;
					optimal_score++;
				}

				// assuming cheating play
				cheat_level++;
			}
		}
		cout<<"Case #"<<t<<": "<<cheat_score<<" "<<n-optimal_score<<endl;
	}

	return 0;
}
