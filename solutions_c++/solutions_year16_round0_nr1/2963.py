#include <iostream>
#include <fstream>
using namespace std;
bool AllDone(int Counter[]) {
	int i;
	for (i = 0; i < 10; i++)
		if (Counter[i] == 0)
			break;
	if (i == 10)
		return false;
	return true;
}
void SetCounter(int N, int Counter[]) {
	do {
		int R = N % 10;
		Counter[R] = 1;
		N /= 10;
	} while (N != 0);
}
int main() {
	ifstream fin("A-large.in", ios::in);
	ofstream fout("A-large.out", ios::out);
	int T;
	unsigned long Bleatix, TempBleatix;
	fin >> T;
	for (int j = 0; j < T; j++) {
		int Counter[10] = { 0 };
		fin >> Bleatix;
		int i = 0;
		fout << "Case #" << j + 1 << ": ";
		if (Bleatix == 0)
			fout << "INSOMNIA\n";
		else {
			for (; AllDone(Counter);) {
				TempBleatix = Bleatix * ++i;
				SetCounter(TempBleatix, Counter);
			}
			fout << TempBleatix<<endl;
		}
	}
}
