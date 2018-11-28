#include <fstream>
#include <iostream>
#include <array>

using namespace std;

FILE *fin, *fout;

bool isFull(std::array<bool,10> ar)
{
	for (int i = 0; i < 10; i++) {
		if (!ar[i]) {
			return false;
		}
	}

	return true;
}



int main()
{
	fopen_s(&fin, "input.txt", "r");
	fopen_s(&fout, "output.txt", "w");

	int t;
	fscanf_s(fin, "%d", &t);

	for (int i = 1; i <= t; i++) {
		int n;
		fscanf_s(fin, "%d", &n);
		if (n == 0){
			fprintf_s(fout, "Case #%d: INSOMNIA\n", i);
			continue;
		}

		int temp = 0;
		std::array<bool, 10> fDig;
		fDig.fill(false);

		while (!isFull(fDig)) {
			temp += n;
			int a = temp;
			while (a != 0) {
				fDig[a % 10] = true;
				a = a / 10;
			}
		}
		fprintf_s(fout, "Case #%d: %d\n", i, temp);
	}

}