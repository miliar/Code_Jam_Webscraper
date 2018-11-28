#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

int T;

int main()
{
	fin >> T;
	for(int i = 1; i <= T; i++){
		int maxS, answer = 0, people = 0;
		string audience;
		fin >> maxS >> audience;
		for(int j = 0; j < audience.length(); j++){
			if(audience[j] - '0' != 0){
				answer += max(0, j - people);
				people += max(0, j - people);
			}
			people += audience[j] - '0';
		}
		fout << "Case #" << i << ": ";
		fout << answer << "\n";
	}
	return 0;
}