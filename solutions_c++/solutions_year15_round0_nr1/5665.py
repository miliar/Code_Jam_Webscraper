//
//  main.cpp
//  GoogleCodejam
//
//  Created by JungMyun Girl on 2015. 4. 11..
//  Copyright (c) 2015³â ChoboSu_Jung. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>



void func(FILE *fi, FILE *fo,int idx){
	int n;
	int arr[1001];
	char arrc[2000];
	fscanf(fi, "%d", &n);
	fscanf(fi, "%s", arrc);

	for (int i = 0; i <= n; i++){
		arr[i] = arrc[i] - '0';
	}

	int curp = 0, need = 0;
	for (int i = 0; i <= n; i++){
		if (curp < i){
			int tmp = i - curp;
			need += tmp;
			curp += tmp;
		}
		curp += arr[i];
	}

	fprintf(fo, "Case #%d: %d\n", idx, need);
}

int main(void) {
	FILE *fi, *fo;

	fi = fopen("A-small-attempt0 (1).in", "r");
	fo = fopen("A.out", "w");

	int T;
	fscanf(fi, "%d", &T);

	for (int i = 0; i<T; i++){
		func(fi, fo, i);
	}
}