#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <unordered_map>
#include <set>
#include <vector>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <stack>
#define NUM_PRIME 200

using namespace std;

int primes[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,
547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223 };

int res[11][32][NUM_PRIME];//res[i][j][k] means i^j mod primes[k]

long long int pow(int k,int x) {
	if (x == 0)
		return 1;
	else
		return k * pow(k,x-1);
}

void init() {
	memset(res, 0, sizeof(res));
	for (int k = 0; k < NUM_PRIME; k++) 
		for (int i = 2; i < 11; i++){
			int modula = 1;
			for (int j = 0; j < 32; j++){
				res[i][j][k] = modula;
				modula = (modula * i) % primes[k];
			}
	}				
}

//Return -1 if the tested number is a prime, otherwise return a nontrivial divisor of the number
int primalTest(bool bits[], int base, int bitlength) {
	//ignoring some edge cases 0, 1,2 because they won't show up
	//ignoring edge case the number itself is the prime: the number itself is at least 2^16, far greater than primes we have
	for (int k = 0; k < NUM_PRIME; k++) {
		int modulesum = 0;
		for (int j = 0; j < bitlength; j++)
			modulesum += bits[j] * res[base][j][k];
		if (modulesum % primes[k] == 0)
			return primes[k];
	}
	return -1;
}

int main() {
	FILE * stream1, *stream2;
	freopen_s(&stream1, "Text.txt", "r", stdin);
	freopen_s(&stream2, "OUTPUT.txt", "w", stdout);
	int T, times;
	cin >> T;
	times = 1;
	init();
	while (T--) {
		int N, J;
		cin >> N >> J;
		cout << "Case #" << times << ":" << endl;
		times++;
		for (long long int jamcoin_var = 0; jamcoin_var < pow(2,N - 2); jamcoin_var++) {
			long long int jamcoin = 2 * jamcoin_var;	//left shift one
			jamcoin += pow(2,N - 1) + 1; // Adding the first and the last digit
			bool bits[33];
			for (int j = 0; j < N; j++) //Translating jamcoin into a bitwise array
				bits[j] = ((jamcoin & pow(2,j)) != 0);
			//test primality in 9 base
			int divisors[9],result;
			for (int j = 2; j < 11; j++) {
				result = primalTest(bits, j, N);
				if (result == -1)
					break;
				divisors[j - 2] = result;
			}
			if (result != -1) {//found a jamcoin
				for (int i = N - 1; i >= 0; i--)
					cout << bits[i];
				for (int i = 0; i < 9; i++)
					cout << " " << divisors[i];
				cout << endl;
				J--;
				if (J == 0)
					break;
			}
			
		}
		
	}
	return 0;
}