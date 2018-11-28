#include <stdlib.h>
#include <stdio.h>

int solve(int ctry){
	int cards1[16], cards2[16], a1, a2;
	char* rez = NULL;
	char out_rez[16];
	scanf("%d", &a1);
	for (int i = 0; i < 16; i++) scanf("%d", cards1 + i);
	scanf("%d", &a2);
	for (int i = 0; i < 16; i++) scanf("%d", cards2 + i);
	a1--; a1 *= 4; 
	a2--; a2 *= 4;
	
	// 1: is magician ok? all 4 nubmers on the "a1" row should be on different rows of second attepmt
	// that means that on each row should be something from 
	bool magician_ok = true;
	int answer = 0;	// default error
	int answer_cnt = 0;	// if more than 1: cheat!
	for (int i = 0; i < 4; i++) {	// rows of the second try that are being checked
		bool found_card = false;
		for (int j = 0; j < 4; j++)	// elements from try 1
			for (int k = 0; k < 4; k++)	// elements from try 2
				if (cards1[a1 + j] == cards2[i*4 + k]){
					found_card = true;
					if (i*4 == a2) {
						answer = cards1[a1 + j];
						answer_cnt++;
					};
				};
		if (!found_card)	// there is a row in the second try that does not contain any cards from the choosen one from try1!
			magician_ok = false;
	};	

	if (answer) {
		sprintf(out_rez, "%d", answer);
		rez = out_rez;
	};
	if (answer_cnt > 1) 
		rez = "Bad magician!";
	if (!answer)
		rez = "Volunteer cheated!";
			
	printf("Case #%d: %s\n", ctry, rez);
};


int main(){

	if (freopen("test.in", "rt", stdin)){
//		freopen("A-large-practice.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-small-attempt1.in", "rt", stdin)){
		freopen("A-small-attempt1.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-large-practice.in", "rt", stdin)){
		freopen("A-large-practice.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};