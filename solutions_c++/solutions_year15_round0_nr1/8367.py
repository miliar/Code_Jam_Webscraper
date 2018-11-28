/*
 * =====================================================================================
 *
 *       Filename:  standing_ovation.cc
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/11/2015 08:02:09 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:   (Qi Liu), liuqi.edward@gmail.com
 *   Organization:  antq.com
 *
 * =====================================================================================
 */

#include<stdio.h>

void StandingOvation(const char* input_file_name, const char* output_file_name){
	int i, j, count, level, sum, ans, tmp;
	char people[1002];
	FILE* file = fopen(input_file_name, "r");
	FILE* output_file = fopen(output_file_name, "a");
	count  = 0;
	fscanf(file, "%d", &count);
	for(i = 0; i != count; ++i){
		level = 0;
		fscanf(file, "%d", &level);
		fscanf(file, "%s", people);
		sum = people[0] - '0';
		ans = 0;
		level += 1;
		for(j = 1; j != level; ++j){
			if(j > sum){
				tmp = j - sum;
				ans += tmp;
				sum += tmp;
			}
			sum += people[j] - '0';
		}
		fprintf(output_file, "Case #%d: %d\n", i+1, ans);
	}
	fclose(file);
	fclose(output_file);
}

int main(){
	const char* input_file_name = "A-large.in";
	const char* output_file_name = "output.txt";
	StandingOvation(input_file_name, output_file_name);
	return 0;
}
