//
//  main.cpp
//  round1_3
//
//  Created by wonhee jang on 13. 4. 14..
//  Copyright (c) 2013년 vanillabreeze. All rights reserved.
//

#include <iostream>
#include <sstream>
#include <math.h>
#include "BigIntegerLibrary.hh"


BigUnsigned makeface(BigUnsigned face) {
	std::string sf = bigUnsignedToString(face);
	const char* sfc = sf.c_str();
	size_t len = sf.length();
	std::stringstream _stream;
	while (len > 0) {
		len--;
		_stream << sfc[len];
	}
	_stream << sf;
	return stringToBigUnsigned(_stream.str());
}

bool isface(BigUnsigned face) {
	std::string sf = bigUnsignedToString(face);
	const char* sfc = sf.c_str();
	size_t len = sf.length();
	std::stringstream _stream;
	while (len > 0) {
		len--;
		_stream << sfc[len];
	}
	if(sf == _stream.str())
		return true;
	return false;
}

BigUnsigned numofface(BigUnsigned small, int len_small, BigUnsigned big, int len_big) {
	BigUnsigned i = 0;
	for(;small <= big; small++) {
		if(isface(small)) {
			float num = sqrtf(atof(bigUnsignedToString(small).c_str()));
			if(num - floorf(num) == 0) {
				std::stringstream stream;
				stream << (int)num;
				if(isface(stringToBigUnsigned(stream.str())))
					i++;
			}
		}
	};
	return i;
	/*
	//검사할 자릿수
	int bit = (len_big - len_small) / 2;
	std::stringstream _stream;
	for(int i = 0; i < bit; i++)
		_stream << '9';
	BigUnsigned count = stringToBigUnsigned(_stream.str().c_str());
	std::cout << count;
	//for(BigUnsigned i = 0; i < count; i++) {
		
	//}
	return 0;
	 */
}

int main(int argc, const char * argv[])
{
	FILE* f = fopen(argv[1], "r");
	int len = 1;
	fscanf(f, "%d", &len);
	fseek(f, SEEK_CUR, 1);
	int i = 0;
	while (i < len) {
		char buf[2][101] = {NULL,};
		fscanf(f, "%s %s", buf[0], buf[1]);
		
		BigUnsigned small = stringToBigUnsigned(std::string(buf[0]));
		BigUnsigned big = stringToBigUnsigned(std::string(buf[1]));
		
		std::cout << "Case #" << (i+1) << ": "  << numofface(small, (int)strlen(buf[0]), big, (int)strlen(buf[1])) << "\n";
		
		fseek(f, SEEK_CUR, 1);
		i++;
	}
	fclose(f);
    return 0;
}

