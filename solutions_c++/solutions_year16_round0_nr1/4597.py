#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
using namespace std;

int check = 2047;

void setN(int i){
	int t = 2047 - (1 << i);
	check &= t;
}


void gCSheep(int N, int r){
	if (N == 0){
		printf("Case #%d: INSOMNIA\n", r);
		return;
	}


	int test = 0;
	int tp;
	int tp2;

	while (check != 1024){
		test += N;
		tp = test;

		while (tp != 0){
			tp2 = tp % 10;
			setN(tp2);
			tp /= 10;
			if (check == 1024)
				break;
		}
	}
	printf("Case #%d: %d\n", r, test);
	

}



int main(void){

	int Test_Case;
	int num;
	//freopen("input.txt", "r", stdin);
	scanf("%d", &Test_Case);
	for (int i = 1; i <= Test_Case; ++i){
		check = 2047;
		scanf("%d", &num);
		gCSheep(num, i);
	}
	
	return 0;
}