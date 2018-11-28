#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;


int T;
int arr1[4][4];
int arr2[4][4];

int* cand1;
int* cand2;

int CA;
int nCA;

int ans1, ans2;

void getArr(int (*arr)[4] ){
	
	for (int r = 0; r < 4; r++){
		for (int c = 0; c < 4; c++){
			scanf("%d", &arr[r][c]);
		}
	}
}



int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output0.txt", "w", stdout);
		
	scanf("%d", &T);

	int nCase = 1;
	while (T-- > 0){

		scanf("%d", &ans1);
		getArr(arr1);

		scanf("%d", &ans2);
		getArr(arr2);

		cand1 = arr1[ans1 - 1];
		cand2 = arr2[ans2 - 1];
		
		nCA = 0;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (cand1[i] == cand2[j]){
					CA = cand1[i];
					nCA++;
				}
			}
		}
		if (nCA == 0){
			printf("Case #%d: %s\n", nCase, "Volunteer cheated!");
		}
		else if (nCA == 1){
			printf("Case #%d: %d\n", nCase, CA);
		}
		else if (nCA >= 2){
			printf("Case #%d: %s\n", nCase, "Bad magician!");
		}
		nCase++;
	}

	return 0;
}