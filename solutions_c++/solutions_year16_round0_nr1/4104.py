/*
 * Counter.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: phinjirp
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool ready(bool check[10]){
	return (check[0]&&check[1]&&check[2]&&check[3]&&check[4]&&check[5]&&check[6]&&check[7]&&check[8]&&check[9]);
}

long long int count(long long int n , bool zero){
	bool check[10];
	memset(check, 0 , sizeof(check));
	if(zero)check[0] = true;
	if(n==0)return 0;
	long long int counter = 0, tmp;

	while(!ready(check)){
		counter+=n;
		tmp = counter;
		while(tmp>0){
			check[tmp%10] = true;
			tmp/=10;
		}

	}
	return counter;
}

int main(){
	int t;
	int zeros;
	long long int n,result;
	FILE *fin,*fout;

	fin = fopen("input.txt","r");
	fout = fopen("output.txt","w+");
	fscanf(fin,"%d",&t);
	for(int i = 1 ; i <= t ; ++i)
	{
		fscanf(fin,"%lld",&n);
		fprintf(fout,"Case #%d: ",i);
		if(n==0)fprintf(fout,"INSOMNIA\n");
		else {
			zeros = 0;
			while(n%10 == 0)
			{
				zeros++;
				n/=10;
			}
			result = count(n, zeros>0);
			fprintf(fout,"%lld",result);
			for(int j = 0 ; j < zeros; ++j)
				fprintf(fout,"0");
			fprintf(fout,"\n");
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}


