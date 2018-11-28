#include <stdio.h>
#include <string.h>
#include <iostream>
#include <list>
#include <vector>
#include <stdlib.h>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 1 ; i <= T ; i++){
		int trash;
		int ans1, res1[4];
		cin >> ans1;
		for (int j = 1 ; j <= 4 ; j++){
			for (int k = 0 ; k < 4 ; k++){
				if (j == ans1){
					cin >> res1[k];
				}else{
					cin >> trash;
				}
			}
		}

		int ans2, res2[4];
		cin >> ans2;
		for (int j = 1 ; j <= 4 ; j++){
			for (int k = 0 ; k < 4 ; k++){
				if (j == ans2){
					cin >> res2[k];
				}else{
					cin >> trash;
				}
			}
		}

		int count = 0, num;
		for (int j = 0 ; j < 4 ; j++){
			for (int k = 0 ; k < 4 ; k++){
				if (res1[j] == res2[k]){
					count++;
					num = res1[j];
				}
			}
		}
		cout << "Case #" << i << ": ";
		if (count > 1){
			cout << "Bad magician!" << endl;
		}
		if (count == 0){
			cout << "Volunteer cheated!" << endl;
		}
		if (count == 1){
			cout << num << endl;
		}
	}

}
