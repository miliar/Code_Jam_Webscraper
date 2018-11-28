#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <sstream>
#include <cstdlib>
using namespace std;

// from the sample input, it's obvious that there's only these between 1 and 1000
// 1, 4, 9, 121, 484
int main()
{
	ifstream fin;
	fin.open ("input.txt");

	ofstream fout;
	fout.open ("output.txt");

	int fas[] = {1, 4, 9, 121, 484};
	int N; // num test cases
	fin >> N;
	for( int n = 0; n < N; n++ ) {
		int A;
		int B;
		fin >> A;
		fin >> B;

		int count = 0;
		for(int i = 0; i < 5; i++)
		{
			if( A <= fas[i] && B >= fas[i])
				count++;
		}

		cout << "Case #" << n+1 << ": " << count << endl;
		fout << "Case #" << n+1 << ": " << count << endl;
	}
	return 0;
}
