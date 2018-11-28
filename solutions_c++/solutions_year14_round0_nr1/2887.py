#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
using namespace std;

int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.in","w",stdout);
	int T;
	int k = 1;
	cin >> T;
	while(T--){
		vector<int> V;
		int row;
		int arr[4][4];
		cin >> row;
		for(int i = 0 ; i < 4 ; ++i){
			for(int j = 0 ; j < 4 ; ++j){
				cin >> arr[i][j];
				if(i + 1 == row){
					V.push_back(arr[i][j]);
				}
			}
		}
		cin >> row;
		for(int i = 0 ; i < 4 ; ++i){
			for(int j = 0 ; j < 4 ; ++j){
				cin >> arr[i][j];
			}
		}
		for(int i = 0 ; i < (int)V.size() ; ++i){
			bool find = 0;
			for(int j = 0 ; j < 4 ; ++j){
				if(V[i] == arr[row - 1][j]){
					find = 1;
				}
			}
			if(!find){
				V.erase(V.begin() + i);
				i--;
			}
		}
		cout << "Case #" << k << ": ";
		if(V.size() == 1){
			cout << V[0];
		}
		if(V.size() > 1){
			cout << "Bad magician!";
		}
		if(V.size() == 0){
			cout << "Volunteer cheated!";
		}
		cout << endl;
		k++;
	}
	return 0;
}
