// test3.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <math.h>
bool expand(int a, int *c) {
	while(a > 0) {
		*c = a % 10;
		c++;
		a = a / 10;
	}
	return true;
}
bool check(int *c) {
	int i, j;
	j = 99;
	while(j>0 && c[j] == 0)
		j--;
	for(i=0; j > i; j--, i++) {
		if(c[j] != c[i])
			return false;
	}
	return true;
}
bool check(int a) {
	int eA[100];
	memset(eA, 0, 100*sizeof(int));
	expand(a, eA);
	return (check(eA));
}
bool power(int *a, int *b, int *c) {
	memset(c, 0, 100*sizeof(int));
	for(int i = 0; i<50; i++) {
		for(int j = 0; j<50; j++) {
			c[i+j] += a[i] * b[j];
		}
	}
	int t;
	for(int i=0; i<100; i++) {
		t = c[i];
		while (t > 10) {
			c[i+1]++;
			t = t / 10;
		}
		c[i] = c[i] % 10;
	}
		
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int num, count;
	int from, to, sfrom, sto;
	std::cin >> num;
	for(int iCase = 1; iCase <= num; iCase++) {
		std::cin >> from >> to;
		sfrom = ceil(sqrt(double(from)));
		sto = sqrt(double(to));
		count = 0;
		for(int i = sfrom; i <= sto; i++) {
			if(check(i)&&check(i*i)) {
				count++;
				//std::cout << i << "\n";
			}
		}
		std::cout << "Case #" << iCase << ": " << count << "\n";
	}
	return 0;
}

