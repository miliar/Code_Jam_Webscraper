/* Dan Mitton

*/
#define _CRT_SECURE_NO_DEPRECATE
#define toDigit(c) (c-'0')
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <fstream>

using namespace std;
typedef long long ll;
typedef long double ld;


int cases; char s[128];
int main()
{
	//freopen("testA.txt", "rt", stdin);

	//freopen("out1.txt", "wt", stdout);
	//cin >> n;
	//cout << n;
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp = fopen(infile, "r"); //*ofp = freopen(outfile, "wt", stdout);
	ofstream outFile;
	ifstream inFile;
	inFile.open(infile);
	outFile.open(outfile);
	//	cout << infile;
	fscanf(fp, "%d", &cases);

	for (int i = 0; i < cases; i++) {
		cout << "hi\n";
		fscanf(fp, "%s", s);
		
		string word(s);
		cout << word;
		string lastWord = "";
		for (int j = 0; j < word.size(); j++) {

			if (lastWord == "") {
				lastWord += word.at(j);
			}
			else if (word.at(j) < lastWord.at(0)) {
				lastWord = lastWord + word.at(j);
			}
			else {
				lastWord = word.at(j) + lastWord;
				
			}
		}

		outFile << ("Case #" + to_string(i + 1) + ": " + lastWord + "\n");

	}



	//	std::cout << n;
	//	std::cout << "hi";

	//	std::cout << "Press ENTER to continue...";
	//std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	//	system("pause");

	return 0;
}
