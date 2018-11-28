#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
 
using namespace std;
 
int main()
{
    ifstream fin("C-small-attempt2.in");
    ofstream fout("C-small-attempt2.out");
    int T;
    fin >> T;

    int mult[4][4];
    int neg[4][4];
    mult[0][0] = 0;
    mult[0][1] = 1;
    mult[0][2] = 2;
    mult[0][3] = 3;
    mult[1][0] = 1;
    mult[1][1] = 0;
    mult[1][2] = 3;
    mult[1][3] = 2;
    mult[2][0] = 2;
    mult[2][1] = 3;
    mult[2][2] = 0;
    mult[2][3] = 1;
    mult[3][0] = 3;
    mult[3][1] = 2;
    mult[3][2] = 1;
    mult[3][3] = 0; 

    neg[0][0] = 1;
    neg[0][1] = 1;
    neg[0][2] = 1;
    neg[0][3] = 1;
    neg[1][0] = 1;
    neg[1][1] = -1;
    neg[1][2] = 1;
    neg[1][3] = -1;
    neg[2][0] = 1;
    neg[2][1] = -1;
    neg[2][2] = -1;
    neg[2][3] = 1;
    neg[3][0] = 1;
    neg[3][1] = 1;
    neg[3][2] = -1;
    neg[3][3] = -1;
    
    int L, X;
    string ori_s;
    for (int t = 1 ; t <= T; t++)
    {  
	string s = "";

	fin >> L >> X >> ori_s;
	for (int i = 0 ; i < X ; i++)
		s = s + ori_s;
	int total = 0;
	int neg_total = 1;
	for (int i = 0 ; i < s.size() ; i++) {
		int c = 0;
		if (s[i] == 'i') c = 1;
		if (s[i] == 'j') c = 2;
		if (s[i] == 'k') c = 3;
		neg_total *= neg[total][c];
		total = mult[total][c];
		
	}
	if (total != 0 || neg_total != -1) {
       		fout << "Case #" << t << ": " << "NO" << endl;
		continue;
	}
	
	bool canDo = false;
	int total_i = 0;
	int neg_i = 1;
	int c = 0;
	for (int i = 0 ; i < s.size() ; i++) {
		if (s[i] == 'i') c = 1;
		if (s[i] == 'j') c = 2;
		if (s[i] == 'k') c = 3;

		neg_i *= neg[total_i][c];
		total_i = mult[total_i][c];
		//cout << s[i] << " ... " << total_i << " ... " << neg_i << endl;
		if (total_i == 1 && neg_i == 1) {
			int total_j = 0;
			int neg_j = 1;
			for (int j = i+1 ; j < s.size() ; j++) {
				if (s[j] == 'i') c = 1;
				if (s[j] == 'j') c = 2;
				if (s[j] == 'k') c = 3;

				neg_j *= neg[total_j][c];
				total_j = mult[total_j][c];
//cout << "!!! " << s[j] << " ... " << total_j << " ... " << neg_j << endl;
				if (total_j == 2 && neg_j == 1) {
					canDo = true;
					break;
				}	
			}
			if (canDo) break;
		}
	}
	if (canDo)
	fout << "Case #" << t << ": " << "YES" << endl;
	else
	fout << "Case #" << t << ": " << "NO" << endl;
    }
}
