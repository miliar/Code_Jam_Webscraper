#include <fstream>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <chrono>
#include <algorithm>
#include <unordered_map>
#include <hash_map>
using namespace std;
#define FOR(i,a,b) for (unsigned int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define MIN(a,b) a<b?a:b
typedef chrono::system_clock Clock;
typedef unsigned long long ull;
typedef unsigned int ui;


int main(int argc, char* args[])
{
	ofstream fout("output.txt");
	ifstream fin("input.txt");
	auto start_time = Clock::now();
	int T;
	fin >> T;
	REP(tt,T) {
		int N;
		int M[1000];
		fin >> N;
		REP(i,N)
			fin >> M[i];

		int y = 0;
		ui plate = M[0];
		int z = 0;

		FOR(i,1,N)
		{
			if(M[i] < M[i-1]) // mushrooms were eaten
			{
				y += M[i-1] - M[i];
			}
		}

		ui r = 0;
		
		FOR(i,1,N)
		{
			int diff = M[i-1] - M[i];
			if(diff > 0 && diff > r)
				r = diff;
		}

		FOR(i,0,N-1)
		{
			if(M[i] < r)
				z += M[i];
			else
				z += r;
		}

		fout << "Case #" << tt+1 << ": " << y << " " << z << endl;
	}
	auto end_time = Clock::now();
	auto exec_time = end_time - start_time;
	cout << chrono::duration_cast<chrono::milliseconds>(exec_time).count() << "ms" << endl;
	return 0;
}