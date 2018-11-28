#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
 
using namespace std;
 
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T;
    fin >> T;
     
    string S;
    int Smax;
    for (int t = 1 ; t <= T; t++)
    {  
	int answer = 0;
	int total = 0;
	fin >> Smax >> S;
	for (int i = 0 ; i < S.size() ; i++) {
		int c = (int)S[i]-48;
		if (total < i) {
			answer += (i-total);
			total = i;
		}
		total += c;
	}
       fout << "Case #" << t << ": " << answer << endl;       
    }
}
