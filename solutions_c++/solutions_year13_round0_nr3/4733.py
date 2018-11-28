#define G2013_QUALIFICATION_C 1
#if G2013_QUALIFICATION_C == 1

#ifndef GIN
	#define GIN "C-large-1.in" 
	#define GOUT "C-large-1.out"
#endif

#ifndef GIN
	#define GIN "input.txt" 
	#define GOUT "output.txt"
#endif

#ifndef GIN
	#define GIN "C-small-attempt0.in" 
	#define GOUT "C-small-attempt0.out"
#endif






#define myfile(B) ("E:\\CodeJam\\C\\"##B)

#include <SDKDDKVer.h>
#include <stdio.h>
#include <tchar.h>
#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <queue>
using namespace std;

ifstream g_infile;
ofstream g_outfile;
#define read(x) {g_infile >> x;}
#define readline(x) {std::getline(g_infile, x);}
#define write(x) {g_outfile << x;}
#define result_head(x) {g_outfile << "Case #"; g_outfile << x;  g_outfile << ": ";}
#define result_endl() {g_outfile << std::endl;}

vector<__int64> g_all;

bool IsPalindrome(unsigned long long n) {
    bool r = true;
    char s[30];
    int l = sprintf(s, "%llu", n);

    if (l == 1 && n != 1) {
        r = true;
    } else  {
        for (int i = 0; i < l/2; i++) {
            if (s[i] != s[l-i-1]) {
                r = false;
                break;
            }
        }
    }
 
    return r;
}

__int64 mypow(int x, int y) {
	__int64 result = 1;
	for (int i = 0; i < y; ++i) 
		result *= x;
	return result;
}

void prebuild() {
	__int64 MAX = 0;
	MAX = mypow(10, 7);

	printf("%llu\r\n", MAX);
    for (__int64 i = 1; i <= MAX; ++i) {
		__int64 numbertocheck = i * i;
		if (IsPalindrome(i) && IsPalindrome(numbertocheck)) {
			printf("%lld: %lld\r\n", i, numbertocheck);
			g_all.push_back(numbertocheck);
		}
	}
}

void alg() {
	__int64 N, A, B, counter;

	read(N);
	for (__int64 i = 1; i <= N; ++i) {
		read(A); read(B);
		counter = 0;
		for(vector<__int64>::iterator iter = g_all.begin(); iter != g_all.end(); ++iter) {
		    if (*iter < A) continue;
			if (*iter > B) break;
			counter++;
		}
		result_head(i);
		write(counter);
		result_endl();
	}
}

int main(int argc, _TCHAR* argv[])
{
	g_infile.open(myfile(GIN), ifstream::in);
	g_outfile.open(myfile(GOUT), ifstream::out);

	prebuild();
	alg();

	g_outfile.close();
	g_infile.close();
	printf("over!\r\n");
	getchar();
	return 0;
}

#endif