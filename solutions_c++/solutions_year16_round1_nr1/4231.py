/* 
 * File:   main.cpp
 * Author: henryw
 *
 * Created on April 4, 2016, 5:58 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <memory.h>
#include <cassert>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <cmath>

typedef unsigned long long ull;

std::string wordC(std::string s, char c)
{
	if (s.at(0) <= c) return std::string(1, c) + s;
	else return s + std::string(1, c);
}
int main(int argc, char* argv[])
{
	using namespace std;
	int nCases;
	
	freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );
	
	scanf( "%d\n", &nCases );
	
	for (int iCase = 1; iCase <= nCases; ++iCase)
	{
		char str[1000];
		char result[1000];
		scanf("%s", str);
		
		std::string word(1, str[0]);
		for (int i = 1; str[i] != '\0'; ++i)
		{
			word = wordC(word, str[i]);
		}
		
		printf("Case #%d: %s\n", iCase, word.c_str()); // Case number
			
	}
	
	return 0;
}

