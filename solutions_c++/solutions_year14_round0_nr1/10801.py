/*
 * CodeJam.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: abhishek
 */
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<stdio.h>
#include <map>
using namespace std;

int main(int argc, char **argv) {
	int a[4], b[4];
	int t, ch, ca = 1, temp;
	FILE *fp;
	char line[80];
	fp = fopen("/home/abhishek/Desktop/input.txt", "r");
	if (fp == NULL)
		cout << "File Openning Error";
	//get test cases
	fgets(line, 80, fp);
	sscanf(line, "%d", &t);

	int flag;
	while (fgets(line, 80, fp) != NULL) {
		flag = 0;
		sscanf(line, "%d", &ch);
		for (int i = 0; i < ch - 1; i++) {
			fgets(line, 80, fp);
		}
		fgets(line, 80, fp);

		sscanf(line, "%d %d %d %d", &a[0], &a[1], &a[2], &a[3]);
		for (int i = ch; i < 4; i++) {
			fgets(line, 80, fp);
		}

		fgets(line, 80, fp);
		sscanf(line, "%d", &ch);
		for (int i = 0; i < ch - 1; i++) {
			fgets(line, 80, fp);
		}
		fgets(line, 80, fp);
		sscanf(line, "%d %d %d %d", &b[0], &b[1], &b[2], &b[3]);
		for (int i = ch; i < 4; i++) {
			fgets(line, 80, fp);
		}

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a[i] == b[j]) {
					if (flag == 0)
						temp = a[i];
					flag++;
				}
			}
		}
		if (flag == 1)
			cout << "Case #" << ca << ": " << temp << endl;
		if (flag > 1)
			cout << "Case #" << ca << ": Bad magician!" << endl;
		if (flag == 0)
			cout << "Case #" << ca << ": Volunteer cheated!" << endl;
		ca++;
		t--;
		if (t == 0)
			break;

	}

}
