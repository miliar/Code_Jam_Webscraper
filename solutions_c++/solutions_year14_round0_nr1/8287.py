#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>

#define MAX 4

using namespace std;

int first[MAX+1][MAX+1], second[MAX+1][MAX+1];
int t, a1, a2;

int main(){
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin >> a1;
		for(int j = 1; j <= MAX; j++){
			for(int k = 1; k <= MAX; k++)
				cin >> first[j][k];
		}
		cin >> a2;
		for(int j = 1; j <= MAX; j++){
			for(int k = 1; k <= MAX; k++)
				cin >> second[j][k];
		}
		int equal, equals = 0;
		for(int j = 1; j <= MAX; j++){
			for(int k = 1; k <= MAX; k++){
				if(first[a1][j] == second[a2][k]){
					equal = first[a1][j];
					equals++;
				}
			}
		}
		cout << "Case #" << i << ": ";
		if(equals == 1)
			cout << equal << endl;
		else if(equals == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}
