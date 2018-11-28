#include <string>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string answers[] = {"Volunteer cheated!","Bad magician!",""};
string case_text = "Case #";

int conf1 [5][5];
int conf2 [5][5];
int row1 = 0, row2 = 0;
int answer = -1;

int Solve(){
	int acum [20];
	fill(acum, acum + 20 , 0);
	for(int c = 0; c < 4 ; c++){
		acum[ conf1[row1 - 1][c] ] ++;
		acum[ conf2[row2 - 1][c] ] ++;
	}
	int num_intersections = 0;
	for(int i = 1; i <= 16 ; i++){
		if( acum[i] > 1 ){
			num_intersections ++;
			answer = i;
		}
	}
	return num_intersections;
}

int main (){
	int T;
	cin >> T;
	for ( int test_id = 1; test_id <= T; test_id ++ ) {
		cin >> row1;
		for ( int i = 0 ; i < 4 ; i++ )	for ( int j = 0; j < 4 ; j++ ) 	cin >> conf1[i][j] ;
		cin >> row2;
		for ( int i = 0 ; i < 4 ; i++ )	for ( int j = 0; j < 4 ; j++ ) 	cin >> conf2[i][j] ;
		int num_intersections = Solve();
		cout << case_text  << test_id << ": ";
		if (num_intersections == 0) cout << answers[0];
		else if (num_intersections > 1) cout << answers[1];
		else cout << answer;
		cout << endl;
	}
}
