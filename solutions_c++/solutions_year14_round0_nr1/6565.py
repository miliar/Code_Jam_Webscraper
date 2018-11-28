#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


int main(){
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	int c1,c2,buf;
	vector<int>v1(4),v2(4);
	for(int t=0; t<T; ++t){
		cin >> c1;
		for(int i=0; i<4; ++i){
			for(int j=0; j<4; ++j){
				if(i!=c1-1){
					scanf("%d", &buf);
				}
				else{
					scanf("%d", &v1[j]);
				}
			}
		}
		cin >> c2;
		for(int i=0; i<4; ++i){
			for(int j=0; j<4; ++j){
				if(i!=c2-1){
					scanf("%d", &buf);
				}
				else{
					scanf("%d", &v2[j]);
				}
			}
		}
		int reps=0;
		int ans;
		for(int i=0; i<4; ++i){
			for(int j=0; j<4; ++j){
				if(v1[i]==v2[j]){
					ans = v1[i];
					reps++;
				}
			}
		}
		cout << "Case #" << t+1 << ": ";
		if(reps==1){
			cout << ans << endl;
		}
		if(reps>=2){
			cout << "Bad magician!" << endl;
		}
		if(reps==0){
			cout << "Volunteer cheated!" << endl;
		}
	}

		

	return 0;
}