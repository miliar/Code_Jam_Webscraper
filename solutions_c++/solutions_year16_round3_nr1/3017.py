#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector <int> vi;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef vector <char> vc;

char alph [26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

bool sortFirst (ii i, ii j){ return (i.first > j.first);}

int sum(vii sth){
	int ans = 0;
	for(int j = 0; j < sth.size(); j++){
		ans += sth[j].first;
	}
	return ans;
}

int main(){
	int T, N, i;
	cin >> T;
	for(i = 0; i < T; i++){
		int j;
		cin >> N;
		vii senators(N + 2, make_pair(0, 26));
		for(j = 0; j < N; j++){
			int temp;
			cin >> temp;
			senators[j] = make_pair(temp, j);
		}
		sort(senators.begin(), senators.end(), sortFirst);
		int sNum = sum(senators);
		cout << "Case #" << i + 1 << ": ";
		while(sNum > 0){
			if(senators[0].first > senators[1].first) {
				senators[0].first -= 2;
				sNum -= 2;
				cout << alph[senators[0].second] << alph[senators[0].second] << " ";
				sort(senators.begin(), senators.end(), sortFirst);
			}
			for(j = 0; j < N && sNum > 0; j++){
				if(senators[j].first == senators[j + 1].first){
					if(senators[j + 2].first == senators[j + 1].first){
						senators[j].first--;
						senators[j + 1].first--;
						senators[j + 2].first--;
						cout << alph[senators[j].second] << " " << alph[senators[j + 1].second] << alph[senators[j + 2].second] << " ";
						sNum -= 3;
						sort(senators.begin(), senators.end(), sortFirst);
						j = (sNum > 0)? -1 : j;
					}
					else {
						senators[j].first--;
						senators[j + 1].first--;
						sNum -= 2;
						cout << alph[senators[j].second] << alph[senators[j + 1].second] << " ";
						sort(senators.begin(), senators.end(), sortFirst);
						j = (sNum > 0)? -1 : j;
					}
				}
				else {
					if(sNum > 3){
						senators[j].first -= 2;
						sNum -= 2;
						cout << alph[senators[j].second] << alph[senators[j].second] << " ";
						sort(senators.begin(), senators.end(), sortFirst);
						j = (sNum > 0)? -1 : j;
					}
					else {
						senators[j].first--;
						sNum--;
						cout << alph[senators[j].second] << " ";
						sort(senators.begin(), senators.end(), sortFirst);
						j = (sNum > 0)? -1 : j;
					}
				}
			}
		}
		cout << endl;
	}
}