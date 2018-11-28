#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#include <string.h>

int ARR[10000][100];
int ARRlen;


int vs(int a, int b){
	if (a == b) return -1;
	else{
		if (a + b == 1) return 0;
		else if (a + b == 2)return 2;
		else if (a + b == 3)return 1;
	}
	return 0;
}

bool getPossible(int cas[], int len){
	if (len == 1) return true;
	else{
		int newCas[8];
		int newLen = 0;
		for (int i = 0; i < (len / 2); i++){
			int temp = vs(cas[2 * i], cas[2 * i + 1]);
			if (temp == -1){
				newCas[newLen] = cas[i];
				newLen++;
				newCas[newLen] = cas[i];
				newLen++;
			}
			else{
				newCas[newLen] = temp;
				newLen++;
			}
		}
		if (newLen != len / 2)return false;
		return getPossible(newCas, newLen);
	}
}

void swap(int arr[], int i, int j) {
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

void perm(int arr[8], int depth, int n, int k) {

	if (depth == k) { // 한번 depth 가 k로 도달하면 사이클이 돌았음. 출력함.
		if (getPossible(arr, k)){
			for (int i = 0; i < k; i++){
				ARR[ARRlen][i] = arr[i];
			}
			ARRlen++;
		}

		return;
	}

	for (int i = depth; i < n; i++) {
		swap(arr, i, depth);
		perm(arr, depth + 1, n, k);
		swap(arr, i, depth);
	}
}

void print(int a){
	if (a == 0)printf("P");
	else if (a == 1)printf("R");
	else if (a == 2)printf("S");
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("Text.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++){
		for (int j = 0; j < 10000; j++){
			for (int k = 0; k < 100; k++){
				ARR[j][k] = 0;
			}
		}
		ARRlen = 0;
		int N, P, R, S;
		scanf("%d %d %d %d", &N, &R, &P, &S);
		//P=0, R=1, S=2
		int cas[8];
		int len = 0;
		for (int j = 0; j < P; j++){
			cas[len] = 0;
			len++;
		}
		for (int j = 0; j < R; j++){
			cas[len] = 1;
			len++;
		}
		for (int j = 0; j < S; j++){
			cas[len] = 2;
			len++;
		}

		perm(cas, 0, len, len);

		int asd[10000];
		int asdlen = 0;
		int asdf = 0;
		int min[8];
		for (int j = 0; j < 10000; j++)asd[j] = 0;
		for (int j = 0; j < ARRlen; j++){
			if (getPossible(ARR[j], len)){
				if (asdlen == 0){
					for (int a = 0; a < len; a++){
						min[a] = ARR[j][a];
					}
				}
				asd[j] = 1;
				asdlen++;
				asdf = 1;
			}
		}
		if (asdf == 0)printf("Case #%d: IMPOSSIBLE\n", i + 1);
		else{
			for (int j = 0; j < asdlen; j++){
				if (asd[j] == 1){
					int q = 0;
					for (int a = 0; a < len; a++){
						if (min[a]>ARR[j][a]){
							q = 1;
							break;
						}
						else if (min[a] < ARR[j][a]){
							break;
						}
					}
					if (q == 1){
						for (int a = 0; a < len; a++){
							min[a] = ARR[j][a];
						}
					}
				}
			}
			printf("Case #%d: ", i + 1);
			for (int k = 0; k < len; k++){
				print(min[k]);
			}
			printf("\n");
		}

	}
}