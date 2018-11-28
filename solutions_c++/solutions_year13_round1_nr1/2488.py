//
//  main.cpp
//  round_2_A
//
//  Created by wonhee jang on 13. 4. 27..
//  Copyright (c) 2013년 vanillabreeze. All rights reserved.
//

#include <iostream>
#include <math.h>
//
//long double excute2(long double start, long double *avail) {
//	long double count = 0;
//	bool sub = true;
//	long double amount = *avail;
//	while (amount >= start + 4) {
//		if(sub) {
//			amount -= amount - 4;
//		} else {
//			amount += amount - 4;
//		}
//		sub = !sub;
//		count++;
//	}
//	*avail -= amount;
//	return count;
//}

bool draw(long double start, long double* avail) {
	long double sr = start;
	long double r = start + 1;
	
	long double f = (r*r - sr*sr);
//	std::cout << floor(*avail) << "," << floor(f) << "\n";
	if(*avail >= f) {
		*avail -= f;
		return true;
	}
	
	return false;
}

double excute(char _buf1[20], char _buf2[20]) {
	long double start = atoll(_buf1);
	long double amount = atoll(_buf2);
	
//	long double test_count = 0;
//	while (amount > start) {
//		test_count += excute2(start, &amount);
//	}
//	std::cout <<"count:"<< test_count << "\n";
//	
//	amount = atoll(_buf2);
	
	long double avail = amount;
	long double count = 0;
	
	while (draw(start, &avail)) {
		start+=2;
		count++;
	}
	
	return count;
}

int main(int argc, const char * argv[])
{
	FILE* f = fopen(argv[1], "r");
	int len = 1;
	fscanf(f, "%d", &len);
	fseek(f, SEEK_CUR, 1);
	int i = 0;
	while (i < len) {
		char buf[2][20] = {NULL,};
		fscanf(f, "%s %s", buf[0], buf[1]);
		
		double count = excute(buf[0], buf[1]);
		
		std::cout << "Case #"<<i+1<<": " << (unsigned long long)count << "\n";
		
		fseek(f, SEEK_CUR, 1);
		i++;
	}
	fclose(f);
    return 0;
}