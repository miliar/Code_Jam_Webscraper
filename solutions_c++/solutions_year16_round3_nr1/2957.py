/*
 * Evac.cpp
 *
 *  Created on: May 8, 2016
 *      Author: phinjirp
 */
#include<stdio.h>
#include<stdlib.h>
void solve(FILE* fin, FILE* fout);
int main(){
	FILE* fin;
	FILE* fout;
	int t;

	fin = fopen("input.txt","r");
	fout = fopen("output.txt","w");

	fscanf(fin,"%d",&t);
	for(int i = 1; i <= t; ++i){
		fprintf(fout,"Case #%d: ",i);
		solve(fin,fout);
		fprintf(fout,"\n");
	}
	fclose(fin);
	fclose(fout);
}

void solve(FILE* fin, FILE* fout){
	int count[26][2];
	int p;
	int sum = 0;
	fscanf(fin,"%d",&p);
	for(int i = 0 ; i < p; ++i){
		fscanf(fin,"%d", &count[i][1]);
		sum += count[i][1];
		count[i][0] = i;
	}

	int max_ind;
	int max_val;
	int tmp;
	for(int i = 0; i < p; ++i){
		max_ind = i;
		max_val = count[i][1];
		for(int j = i+1 ; j < p ;++j){
			if(count[j][1] > max_val){
				max_val = count[j][1];
				max_ind = j;
			}
		}
		tmp = count[i][1];
		count[i][1] = max_val;
		count[max_ind][1] = tmp;

		tmp = count[i][0];
		count[i][0] = count[max_ind][0];
		count[max_ind][0] = tmp;
	}

	int ind = 0;
	while(sum > 0){
		if(p - ind == 2){
			fprintf(fout,"%c%c ",count[ind][0]+'A',count[ind+1][0]+'A');
			count[ind][1]--;
			count[ind+1][1]--;
			sum-=2;
			ind+=2;
			ind%=p;
		}else if(p - ind == 3){
			while(count[ind][1] > count[ind+1][1]){
				fprintf(fout,"%c ",count[ind][0]+'A');
				count[ind][1]--;
				sum-=1;
			}

			if(count[ind][1] == count[ind+1][1] && count[ind+1][1] == count[ind+2][1]){
				fprintf(fout,"%c %c%c ",count[ind][0]+'A',count[ind+1][0]+'A',count[ind+2][0]+'A');
				count[ind][1]--;
				count[ind+1][1]--;
				count[ind+2][1]--;
				sum-=3;
				ind+=3;
				ind%=p;
			}else{
				while(count[ind][1] == count[ind+1][1] && count[ind+1][1] > count[ind+2][1]){
					fprintf(fout,"%c%c ",count[ind][0]+'A',count[ind+1][0]+'A');
					count[ind][1]--;
					count[ind+1][1]--;
					sum-=2;
				}
			}
		}else{
			while(count[ind][1] > count[ind+1][1]){
				fprintf(fout,"%c ",count[ind][0]+'A');
				count[ind][1]--;
				sum-=1;
			}

			while(count[ind][1] == count[ind+1][1] && count[ind+1][1] > count[ind+2][1]){
				fprintf(fout,"%c%c ",count[ind][0]+'A',count[ind+1][0]+'A');
				count[ind][1]--;
				count[ind+1][1]--;
				sum-=2;
			}
			while(count[ind][1] == count[ind+1][1] && count[ind+1][1] == count[ind+2][1] && count[ind+2][1] > count[ind+3][1]){
				fprintf(fout,"%c %c%c ",count[ind][0]+'A',count[ind+1][0]+'A',count[ind+2][0]+'A');
				count[ind][1]--;
				count[ind+1][1]--;
				count[ind+2][1]--;
				sum-=3;
			}

			fprintf(fout,"%c%c ",count[ind][0]+'A',count[ind+1][0]+'A');
			count[ind][1]--;
			count[ind+1][1]--;
			ind+=2;
			ind%=p;
			sum-=2;
		}
	}



}



