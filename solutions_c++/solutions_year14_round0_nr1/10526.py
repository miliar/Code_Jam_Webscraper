#include <iostream>
#include <cstdio>
using namespace std;

int a[4][4], b[4][4];

int checkMagic(int a[4][4], int b[4][4], int first, int second) {

	int count = 0;
	int answer;

	for(int i = 0; i < 4; i++) {
		if(count > 1) break;
		for(int j = 0; j < 4; j++) {
			if(count > 1) break;
			if(a[first-1][i] == b[second-1][j]) {
				count++;
				if(count > 1) {
					break;
				}
				answer = b[second-1][j];
			}
		}
	}

	if(count == 0) return 0;
	else if(count == 1) return answer;
	else return -1;
	
}

int main() {

	int numTest, first_ans, second_ans;
	int fin;

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	
	cin>>numTest;
	for(int test=1; test <= numTest; test++) {
		// Get first Answer
		cin>>first_ans;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin>>a[i][j];
			}
		}
		// Get second Answer
		cin>>second_ans;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin>>b[i][j];
			}
		}
		
		fin = checkMagic(a, b, first_ans, second_ans);
		if(fin == -1) 
			printf("Case #%d: Bad magician!\n", test);
		else if(fin == 0) 
			printf("Case #%d: Volunteer cheated!\n", test);
		else
			printf("Case #%d: %d\n", test, fin);
	}

	return 0;
}