#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
double EPS  = 1e-9;

int main(void){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int T;
	cin >> T;
	
	for(int t = 1; t <= T; t++){
		vector<bool> v1(17, false);
		vector<bool> v2(17, false);

		int ans1, ans2;
		cin >> ans1;

		int arr1[4][4];
		int arr2[4][4];

		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> arr1[i][j];
			}
		}

		for(int j = 0; j < 4; j++){
			v1[arr1[ans1-1][j]] = true;
		}

		cin >> ans2;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> arr2[i][j];
			}
		}

		for(int j = 0; j < 4; j++){
			v2[arr2[ans2-1][j]] = true;
		}

		vector<int> v(17, false);
		for(int i = 1; i < 17; i++){
			v[i] = v1[i] & v2[i];
		}

		int cnt = 0;
		int ans = 0;
		for(int i = 1; i < 17; i++){
			if(v[i]){
				ans = i;
				cnt++;
			}
		}

		if(cnt == 0){
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		}
		else if(cnt == 1){
			cout<<"Case #"<<t<<": "<<ans<<endl;
		}
		else{
			cout<<"Case #"<<t<<": Bad magician!"<<endl;
		}


	}

	return 0;
}