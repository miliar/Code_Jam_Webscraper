/** ========================================================================
 * Name        : main.cpp
 * Author      : Iuro Nascimento
 * Version     :
 * Copyright   :
 * Description : 
==========================================================================*/
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <thread>
#include <chrono>

int countSheep(unsigned long n);
bool isComplete(int &digits);
void checkDigits(unsigned long n, int &digits);

int main(int argc, char *argv[])
{
	std::chrono::high_resolution_clock::time_point to = std::chrono::
		high_resolution_clock::now();
	if (argc < 2) {
		printf("usage: %s filename\n",argv[0]);
		exit(1);
	}
	char *infname;
	if (argc > 2)
		infname = argv[2];
	else
		infname = (char*)"test.out";

	unsigned int nthreads = std::thread::hardware_concurrency();
	std::string infilename(argv[1]);
	std::string line;
	std::ifstream infile (infilename);

	if (!infile.is_open()) {
		printf("Unable to open file");
		exit(1);
	}

	std::ofstream outfile(infname);

	unsigned long T, i;
	unsigned long n;
	infile >> T;
	T++;
	for (i = 1; i < T; i++) {
		infile >> n;
		unsigned long ans = countSheep(n);
		outfile << "Case #" << i << ": ";
		if (!ans)
			outfile << "INSOMNIA\n";
		else
			outfile << ans << "\n";
	}
	infile.close();
	outfile.close();
	std::chrono::high_resolution_clock::time_point tf = std::chrono::
		high_resolution_clock::now();
	std::chrono::duration<double,std::ratio<1l,1000l>> delta_t = 
		std::chrono::duration_cast<std::chrono::duration<double,std::ratio<1l,1000l>>>(tf - to);

	std::cout << "Elapsed: " << delta_t.count() << " ms.\n";

	return 0;
}

int countSheep(unsigned long n)
{
	int digits = 0;/* compiled with gcc 5.3 */
	if (!n)
		return 0;

	unsigned long num = 0;
	while(!isComplete(digits)) {
		num += n;
		checkDigits(num, digits);
	}
	return num;
}

inline bool isComplete(int &digits)
{
	return digits == 1023;
}

void checkDigits(unsigned long n, int &digits)
{
	int digit;
	while (n) {
		digit = n % 10;
		digits |= 1 << digit;
		n /= 10;
	}
}

