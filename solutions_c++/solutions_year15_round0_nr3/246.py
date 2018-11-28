#ifndef __DIJKSTRA_H__
#define __DIJKSTRA_H__

#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

int simple_times(int first, int second) {
	if (first < 0)
		return -1 * simple_times(-1 * first, second);
	if (second < 0)
		return -1 * simple_times(first, -1 * second);

	if (first == 1)
		return second;
	else if (first == 2) {
		if (second == 1) return 2;
		else if (second == 2) return -1;
		else if (second == 3) return 4;
		else if (second == 4) return -3;
	}
	else if (first == 3) {
		if (second == 1) return 3;
		else if (second == 2) return -4;
		else if (second == 3) return -1;
		else if (second == 4) return 2;
	}
	else if (first == 4) {
		if (second == 1) return 4;
		else if (second == 2) return 3;
		else if (second == 3) return -2;
		else if (second == 4) return -1;
	}
}

int mapping(char c) {
	if (c == 'i') return 2;
	else if (c == 'j') return 3;
	else if (c == 'k') return 4;
}

int complex_times(string str) {
	int product = 1;
	for (int i  = 0; i < str.length(); i++)
		product = simple_times(product, mapping(str.at(i)));
	return product;
}

void dijkstra(){
	FILE* fp_read = fopen("C-small-attempt0.in", "r");
	FILE* fp_write = fopen("C-small-attempt0.out", "w");

	int round = 0;
	fscanf(fp_read, "%d\n", &round);
	//cout << "round " << round << endl;

	for (int i = 0; i < round; i++) {
		int l = 0;
		fscanf(fp_read, "%d", &l);
		//cout << "value " << l << endl;
		int x = 0;
		fscanf(fp_read, "%d\n", &x);
		//cout << "value " << x << endl;

		char* line = new char[l + 1];
		fgets(line, l + 1, fp_read);
		string pattern = line;
		//cout << complex_times(pattern) << endl;

		int product = 1;
		for (int j = 0; j < x; j++)
			product = simple_times(product, complex_times(pattern));;

		if (product != -1)
			fprintf(fp_write, "Case #%d: NO\n", i + 1);
		else {
			int product_i = 1;
			int length_i = 1;
			while (length_i < l * x){
				product_i = simple_times(product_i, mapping(pattern.at((length_i - 1) % l)));
				if (product_i == 2) {
					break;
				}
				length_i++;
			}
			int product_j = 1;
			int length_j = 1;
			while (length_j < l * x){
				product_j = simple_times(mapping(pattern.at((l-1)-((length_j - 1) % l))), product_j);
				if (product_j == 4) {
					break;
				}
				length_j++;
			}

			if (length_i != 0 && length_j != 0 && length_i + length_j < l * x)
				fprintf(fp_write, "Case #%d: YES\n", i + 1);
			else
				fprintf(fp_write, "Case #%d: NO\n", i + 1);
		}
	}

	fclose(fp_read);
	fclose(fp_write);
}

#endif