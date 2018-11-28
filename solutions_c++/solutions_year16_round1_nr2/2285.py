#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<char> vc;
typedef vector<vc> vvc;

int main(){
	int T, N, i, j, k, temp;
	cin >> T;
	for(i = 0; i < T; i++){
		cin >> N;
		vvi lists(2*N - 1);
		vi answer;
		int max = 0;
		vi occurances(2500, 0);
		for(j = 0; j < (2*N - 1); j++){
			for(k = 0; k < N; k++){
				cin >> temp;
				lists[j].push_back(temp);
				occurances[temp]++;
				max = max > temp? max : temp;
			}
		}
		for(j = 0; j <= max; j++){
			if(occurances[j]%2){
				answer.push_back(j);
			}
		}
		sort(answer.begin(), answer.end());
		cout << "Case #" << i + 1 << ": ";
		for(j = 0; j < answer.size(); j++){
			cout << answer[j] << " ";
		}
		cout << endl;
	}
}