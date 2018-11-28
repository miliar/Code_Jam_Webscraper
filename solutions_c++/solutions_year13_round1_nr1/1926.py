#include <cstdio>
#include <stdio.h>
#include <string>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;

long calc(long double r,long double t){
	long count=0;
	while(t>0){
		t-=(2*r+1);
		if(t>=0)
			count ++;
		r+=2;
	}
	return count;
}

int main() {
	int total2, total;
	FILE * fl = fopen("A-small-attempt0.in", "r");
	FILE* fo = fopen("outB", "w");
	fscanf(fl, "%d", &total2);
	total = total2;

	for (int i = 0; i < total; i++) {
		long double r;
		long double t;
		fscanf(fl, "%Lf %Lf", &r, &t);
		long num=calc((long double)r,(long double)t);
		fprintf(fo, "Case #%d: %lu\n", i + 1,num);
	}
	return 0;
}

