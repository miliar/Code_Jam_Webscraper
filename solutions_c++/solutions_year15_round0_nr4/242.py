#ifndef __OMINOUS_OMINO_H__
#define __OMINOUS_OMINO_H__

#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

void ominous_omino(){
	FILE* fp_read = fopen("D-large.in", "r");
	FILE* fp_write = fopen("D-large.out", "w");

	int round = 0;
	fscanf(fp_read, "%d", &round);
	//cout << "round " << round << endl;

	for (int i = 0; i < round; i++) {
		int x = 0;
		fscanf(fp_read, "%d", &x);
		//cout << "value " << x << endl;
		int r = 0;
		fscanf(fp_read, "%d", &r);
		//cout << "value " << r << endl;
		int c = 0;
		fscanf(fp_read, "%d", &c);
		//cout << "value " << c << endl;

		int max = 0;
		int min = 0;
		if (r > c) {
			max = r;
			min = c;
		}
		else {
			max = c;
			min = r;
		}

		bool condition = (x<7) && ((r*c)%x==0) && (min>=((x+1)/2)) && (max>=x);
		if (!condition)
			fprintf(fp_write, "Case #%d: RICHARD\n", i + 1);
		else {
			if (x==1 || x==2 ||x==3)
				fprintf(fp_write, "Case #%d: GABRIEL\n", i + 1);
			else {
				if (x==4 && max%2==0 && max >=4 && min==2)
					fprintf(fp_write, "Case #%d: RICHARD\n", i + 1);
				else if (x==5 && max==5 && min==3)
					fprintf(fp_write, "Case #%d: RICHARD\n", i + 1);
				else if (x==6 && max%2==0 && max>=6 && min==3)
					fprintf(fp_write, "Case #%d: RICHARD\n", i + 1);
				else
					fprintf(fp_write, "Case #%d: GABRIEL\n", i + 1);
			}
		}
	}

	fclose(fp_read);
	fclose(fp_write);
}

#endif