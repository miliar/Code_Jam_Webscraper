#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int T;

	cin >> T;

	for(int k = 1; k <= T; k++){
		int N;

		cin >> N;

		double naomi[1005];
		double ken[1005];
		double dat;
		int maximum = 0;
		int minimum = N;
		int count;

		vector<double> na;
		vector<double> ke;

		for(int i = 0; i < N; i++){
			cin >> dat;
			na.push_back(dat);
		}
		
		for(int i = 0; i < N; i++){
			cin >> dat;
			ke.push_back(dat);
		}

		sort(na.begin(), na.end());
		sort(ke.begin(), ke.end());

		int index = 0;

		for(vector<double>::iterator it = na.begin(); it != na.end(); ++it){
			naomi[index] = *it;
			index++;
		}

		index = 0;

		for(vector<double>::iterator it = ke.begin(); it != ke.end(); ++it){
			ken[index] = *it;
			index++;
		}

		count = 0;

		for(int j = 0; j < N; j++){
			for(int i = 0; i < N; i++){
				if(naomi[i] > ken[(i + j) % N]){
					count++;
				}
			}

			if(minimum > count){
				minimum = count;
			}
			count = 0;
		}

		count = 0;

		for(int j = 0; j < N; j++){
			for(int i = 0; i < N; i++){
				if(naomi[i] > ken[(i + j) % N]){
					count++;
				}
			}

			if(maximum < count){
				maximum = count;
			}
			count = 0;
		}

		cout << "Case #" << k << ": " << maximum << " " << minimum << endl;
	}

	return 0;
}