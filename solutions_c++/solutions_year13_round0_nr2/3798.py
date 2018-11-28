#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	int numCase;

	cin >> numCase;

	for (int currentCase = 1; currentCase <= numCase; currentCase++) {
		int desire[100][100];
		bool real[100][100];
		int height, width;
		
		cin >> height >> width;
		int remaining = height * width;

		memset(real, false, sizeof(real));

		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				cin >> desire[i][j];
			}
		}

		bool flag;
		do {
			flag = false;
			for (int i = 0; i < height; i++) {
				int max = 0;
				for (int j = 0; j < width; j++) {
					if (max < desire[i][j]) {
						max = desire[i][j];
					}
				}

				for (int j = 0; j < width; j++) {
					if (desire[i][j] == max && real[i][j] == false) {
						real[i][j] = true;
						//if (remaining == 0) {throw 1;}
						remaining--;
						flag = true;
					}
				}
			}

			for (int i = 0; i < width; i++) {
				int max = 0;
				for (int j = 0; j < height; j++) {
					if (max < desire[j][i]) {
						max = desire[j][i];
					}
				}

				for (int j = 0; j < height; j++) {
					if (desire[j][i] == max && real[j][i] == false) {
						real[j][i] = true;
						//if (remaining == 0) {throw 1;}
						remaining--;
						flag = true;
					}
				}
			}
		} while (flag);

		cout << "Case #" << currentCase << ((remaining) ? ": NO" : ": YES") << endl;
	}
}
