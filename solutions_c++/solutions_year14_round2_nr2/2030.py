#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

int mp[100][100];
char seq[100];

int main(){
	int T,ti,N,i,ni,j,k,sum,flag,le,A,B,K;
	int mid,temp;
	char str[128];
	double po;
	FILE * fin, * fout;
	fin = fopen("B-small-attempt0.in","r");
	fout = fopen("B-small-attempt0.out","w");
	fscanf(fin,"%d",&T);
	flag=0;
	for (ti=0;ti<T;ti++){
		fscanf(fin,"%d%d%d",&A,&B,&K);
		sum=0;
		for (i=0;i<A;i++)
			for (j=0;j<B;j++){
				if ((j&i)<K) sum++;
			}
		fprintf(fout,"Case #%d: %d\n",ti+1,sum);
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
