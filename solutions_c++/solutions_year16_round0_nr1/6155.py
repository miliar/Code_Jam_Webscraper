#include<fstream>
#include<iostream>

using namespace std;

ifstream fin ("A-large.in");
ofstream fout ("sheep.out");

int lastNum(int num, int caseNum) {
    int check[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; 
    fout << "Case #" << caseNum << ": ";
    for (int i = 1; i <= 100000; i++) {
        int testNum = num * i;
        int checkNum = testNum;
        while (checkNum != 0) {
            check[checkNum % 10]++;
	    checkNum /= 10;
	}
	int numNotZero = 0;
        for (int j = 0; j <= 9; j++)
	    if (check[j] > 0) numNotZero++;
        if (numNotZero == 10) {
	    fout << testNum << endl;
            return 0;
	}
    }
    fout << "INSOMNIA" << endl;
    return 0;
}

int main() {
    int N, T;
    fin >> T;
    for (int i = 1; i <= T; i++) {
	int num;
	fin >> num;
	int blank = lastNum(num, i);
    } 
}
