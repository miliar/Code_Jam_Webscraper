#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <assert.h>
#include <string>

using namespace std;

int Max(vector<int> sen){
	int max = sen[0];
	int pos = 0;
	for(int i = 1; i < sen.size(); i++){
		if(max < sen[i]){
			max = sen[i];
			pos = i;
		}
	}
	return pos;
}

int Equal(vector<int> sen, int pos){
	for(int i = 0; i < sen.size(); i++){
		if(i != pos){
			if(sen[pos] == sen[i]){
				pos = i;
				return i;
			}
		}
	}
	return -1;
}

int Equal2(vector<int> sen, int max, int secondPos){
	for(int i = 0; i < sen.size(); i++){
		if(i != max){
			if(i != secondPos){
				if(sen[max] == sen[i]){
					max = i;
					return i;
				}
			}
		}
	}
	return -1;
}

bool check(vector<int> sen){
	for(int i = 0; i < sen.size(); i++){
		if(sen[i] != 0)
			return false;
	}
	return true;
}
int main() {
	
    int t;
    cin >> t;
    assert(t >= 1 && t <= 50);
    
    for( int j = 0; j < t; j++){
	
		int n;
        cin >> n;
        assert(n >= 2 && n <= 26);
		
		int sum = 0;
		vector<int> sen;
		for(int i = 0; i < n; i++){
			int p;
	        cin >> p;
			sum += p;
			sen.push_back(p);
		}
		assert(sum <= 1000);
		
		vector<string> Alph {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
		
		vector<string> ans;
		while(check(sen) != true){
			
			int max = Max(sen);
			int secondPos = Equal(sen, max);
			int thirdPos = -1;
			if(secondPos != -1){
				thirdPos = Equal2(sen, max, secondPos);
			}
			if(secondPos == -1){
				sen[max] = sen[max] - 1;
				ans.push_back(Alph[max]);
			}
			else if(secondPos != -1 && thirdPos == -1){
				sen[max] = sen[max] - 1;
				sen[secondPos] = sen[secondPos] - 1;
				ans.push_back(Alph[max] + Alph[secondPos]);
				//ans.push_back(Alph[secondPos] + Alph[max]);
			}
			else if(secondPos != -1 && thirdPos != -1){
				sen[max] = sen[max] - 1;
				ans.push_back(Alph[max]);
			}
		}
		

		cout << "Case #" << j + 1 << ": ";
		for(int i = 0; i < ans.size(); i++){
			cout << ans[i] << " ";
		}
		cout << endl;
	}
	
}