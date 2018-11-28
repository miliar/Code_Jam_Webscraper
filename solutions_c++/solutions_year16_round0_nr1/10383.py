#include <stdio.h>
#include <cstdio>

const int mask = 1023;

int main() {

	int  	    input_count;
	long 	    input_value;
	long     	output;
	errno_t     error;
	FILE	   *in_file;
	FILE       *out_file;

	error = fopen_s(&in_file, "W:\\A-large.in", "r"); // read only 
	if (error != 0) {
		printf("Failed to open input file. Err code:");
		return 0;
	}
	error = fopen_s(&out_file, "W:\\A-large.out", "w"); // write only
	if (error != 0) {
		printf("Failed to open output file.");
		return 0;
	} 

	fscanf_s(in_file, "%d\n", &input_count);

	for (int iter = 1; iter <= input_count; iter++) {

		int check_num=0;

		fscanf_s(in_file, "%d\n", &input_value);
		
		if (input_value == 0) {
			fprintf_s(out_file, "CASE #%d: INSOMNIA\n", iter);
			continue;
		}

		output = 0;
		
		do {
			output += input_value;
			long x = output;
			while (x) {
				check_num |= 1 << (x % 10);
				x = x / 10;
			}
		} while (mask != check_num);

		fprintf_s(out_file, "CASE #%d: %d\n", iter, output);
	}

	fclose(in_file);
	fclose(out_file);

	return 0;
}