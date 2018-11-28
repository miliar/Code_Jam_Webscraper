#include <fstream>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cstdlib>
#include <chrono>
#include <algorithm>
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
		ui sMax;
		string audience;
		ui shyness[1024];
		fin >> sMax;
		fin >> audience;

		REP(i,sMax+1) {
			shyness[i] = (ui)(audience[i] - '0');
		}

		ui friends = 0;
		ui people = 0;

		REP(i,sMax+1)
		{
			if(shyness[i] > 0)
			{
				if((people+friends) >= i)
				{
					people += shyness[i];
				}
				else
				{
					friends += i - (people+friends);
					people += shyness[i];
				}
			}
		}

		fout << "Case #" << tt+1 << ": " << friends << endl;
	}
	auto end_time = Clock::now();
	auto exec_time = end_time - start_time;
	cout << chrono::duration_cast<chrono::milliseconds>(exec_time).count() << "ms" << endl;
	return 0;
}