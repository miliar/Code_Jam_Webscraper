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
#include <chrono>
#include <thread>

std::string flip(std::string seq, int until);
int count_flip_points(std::string seq);
int process_sequence(int i, std::string seq);

int main(int argc, char *argv[])
{
	std::chrono::high_resolution_clock::time_point to = std::chrono::
		high_resolution_clock::now();
	if (argc < 2) {
		printf("usage: %s infile [outfile]\n",argv[0]);
		exit(1);
	}
	char *outfname;
	if (argc > 2)
		outfname = argv[2];
	else
		outfname = (char*)"test.out";

	unsigned int nthreads = std::thread::hardware_concurrency();
	std::string infilename(argv[1]);
	std::ifstream infile (infilename);
	std::ofstream outfile (outfname);

	if (!infile.is_open()) {
		printf("Unable to open file");
		exit(1);
	}

	unsigned long T, i;
	unsigned long aux;
	infile >> T;
	std::string seq;
	int digits[10] = {0};/* compiled with gcc 5.3 */
	for (i = 0; i < T; i++) {
		infile >> seq;
		int k = process_sequence(i,seq);
		outfile << "Case #" << i+1 << ": " << k << "\n";
	}
	infile.close();
	outfile.close();

	std::chrono::high_resolution_clock::time_point tf = std::chrono::
		high_resolution_clock::now();
	std::chrono::duration<double,std::ratio<1l,1000000l>> delta_t = 
		std::chrono::duration_cast<std::chrono::duration<double,std::ratio<1l,1000000l>>>(tf - to);

	std::cout << "Elapsed: " << delta_t.count() << " us.\n";

	return 0;
}

int process_sequence(int i, std::string seq)
{
	int k = count_flip_points(seq);
	int n = seq.length() - 1;
	if (seq[n] == '-') k++;

	return k;
}

int count_flip_points(std::string seq)
{
	int k = 0;
	int n = seq.length();
	char old = seq[0];
	for(int i = 1; i < n; i++) {
		char ch = seq[i];
		if (ch != old)
			k++;
		old = ch;
	}
	return k;
}

std::string flip(std::string seq, int until)
{
	int ch = seq[0];		
	if (ch == '+') ch = '-';
	if (ch == '-') ch = '+';
	for(int i = 0; i <= until; i++)
		seq[i] = ch;
	return seq;
}

