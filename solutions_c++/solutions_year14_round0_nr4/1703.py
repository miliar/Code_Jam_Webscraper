#include <iostream>
#include <stdio.h>
#include <algorithm>

int main() {
   int rpt = 0;
    std::cin >> rpt;
for (int w = 0; w < rpt; w++){
    int x;
    std::cin >> x;
    double array1[x];
    double array2[x];
	double array3[x];
	for (int i = 0; i < x; i++)
		std::cin >> array1[i];

	for (int i = 0; i < x; i++)
		std::cin >> array2[i];



	std::sort(array1,array1+x);
	std::sort(array2,array2+x);

    for (int i = 0; i < x; i++)
        array3[i] = array2[i];

	int wins = x;
	int prev_wins = -1;
	for (int i = 0; i < x; i++) {
		double prevVal = 1;
		int index;
		double val = array1[i];
		bool flag = false;
		for (int k = 0; k< x; k++) {
			if (array3[k] > val && array3[k] < prevVal && array3[k] != -1) {
				index = k;
				prevVal = array3[k];
				flag = true;
			}
		}
		if (flag) {
			array3[index] = -1;
			wins--;
		} else {
			for (int k = 0; k< x; k++) {
				if (array3[k] != -1){
					array3[k] = -1;
					break;
				}
			}
		}
	}
	int wars = wins;
	int c = 0;
    int d = 0;
	for (int xd = 0; xd < x; xd++) {
		if (array1[c] > array2[d]){
            c++;
            d++;
        } else {
            c++;
        }
	}


	std::cout << "Case #" << (w+1) << ": " << d << " " << wars;
	std::cout << std::endl;
}
    return 0;
}
