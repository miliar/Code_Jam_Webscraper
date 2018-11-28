//
//  main.cpp
//  GoogleCodejam
//
//  Created by JungMyun Girl on 2015. 4. 11..
//  Copyright (c) 2015³â ChoboSu_Jung. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>



void func(FILE *fi, FILE *fo, int idx){
	int x, r, c;
	fscanf(fi, "%d %d %d", &x, &r, &c);
	if (x == 1) fprintf(fo, "Case #%d: GABRIEL\n", idx);
	else if (x == 2){
		if (r % 2 == 0 || c % 2 == 0)
			fprintf(fo, "Case #%d: GABRIEL\n", idx);
		else
			fprintf(fo, "Case #%d: RICHARD\n", idx);
	}
	else if (x == 3){
		if ((r*c) % x == 0){
			if (r == 1 || c == 1)
				fprintf(fo, "Case #%d: RICHARD\n", idx);
			else
				fprintf(fo, "Case #%d: GABRIEL\n", idx);
		}
		else{
			fprintf(fo, "Case #%d: RICHARD\n", idx);
		}
	}
	else if (x == 4){
		if (r == 4 && c == 3)
			fprintf(fo, "Case #%d: GABRIEL\n", idx);
		else if (r == 3 && c == 4)
			fprintf(fo, "Case #%d: GABRIEL\n", idx);
		else if (r == 4 && c == 4)
			fprintf(fo, "Case #%d: GABRIEL\n", idx);
		else
			fprintf(fo, "Case #%d: RICHARD\n", idx);
	}
}

int main(void) {
	FILE *fi, *fo;

	fi = fopen("D-small-attempt2.in", "r");
	fo = fopen("D.out", "w");

	int T;
	fscanf(fi, "%d", &T);

	for (int i = 0; i<T; i++){
		func(fi, fo, i + 1);
	}
}