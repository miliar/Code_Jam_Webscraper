#include <iostream>
#include <fstream>

using namespace std;

int main(void)
{
	ios::sync_with_stdio(false);
	ifstream input("A-small-attempt0.in");
	ofstream output("out.txt");
	int T, N, temp, count, i, j;
	int digit[10];

	input >> T;

	for(i = 0; i < T; ++i){
		input >> N;
		count = 1;
		for (j = 0; j < 10; ++j) digit[j] = 0;

		while (1){
			temp = N * count;

			while (temp != 0){
				digit[temp % 10] = 1;
				temp /= 10;
			}

			if (temp == N * (count + 1)){
				output << "Case #" << i + 1 << ": INSOMNIA\n";
				break;
			}
			
			for (j = 0; j < 10; ++j){
				if (!digit[j]) break;
			}

			if (j == 10){
				output << "Case #" << i + 1 << ": " << N * count << "\n";
				break;
			}
			count++;
		}
	}

	return 0;
}