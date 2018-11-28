#include<iostream>
#include<fstream>
#include<string>

using namespace std;

ifstream fin ("B-large.in");
ofstream fout ("pancake.out");

string flip(string pancakes, int length) {
    for (int i = 0; i < length; i++) {
        if (pancakes[i] == '+') pancakes[i] = '-';
        else if (pancakes[i] == '-') pancakes[i] = '+';
    }
    return pancakes;
}

bool check(string pancakes, int length) {
    for (int i = 0; i < length; i++)
        if (pancakes[i] == '-') return false;
    return true;
}

int work (string pancakes) {
    int length = pancakes.length();
    if (check(pancakes, length) == true) return 0;
    int numFlips = 0;
    for (int i = length - 1; i >= 0; i--) {
        if (pancakes[i] == '-') {
	    pancakes = flip(pancakes, i + 1);
	    numFlips++;
	}
        if (check(pancakes, length) == true) return numFlips; 
    }
}

int main() {
    int T;
    fin >> T;
    for (int i = 1; i <= T; i++) {
        fout << "Case #" << i << ": ";
        string pancakes;
        fin >> pancakes;
        int num = work(pancakes);
        fout << num << endl;
    }
}
