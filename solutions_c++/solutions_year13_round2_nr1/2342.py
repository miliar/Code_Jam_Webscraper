#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <math.h>
#include <fstream>

using namespace std;

void quickSort(int* arr, int left, int right) {
    int i = left, j = right, tmp;
    int pivot = arr[(left + right) / 2];

    while (i <= j) {
        while (arr[i] < pivot)
        i++;
        while (arr[j] > pivot)
        j--;
        if (i <= j) {
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
    };

    if (left < j)
    quickSort(arr, left, j);
    if (i < right)
    quickSort(arr, i, right);
}

int main(int argc, char* argv[])
{
    ifstream sourceFile("./A-small-attempt2.in");
    ofstream output("./output.txt");

    int T;
    sourceFile >> T;

	for(int i = 0; i < T; i++) {
		int A, N;
		sourceFile >> A >> N;
        int* sizes = new int[N];

        for(int j = 0; j < N; j++) {
            sourceFile >> sizes[j];
        }

        quickSort(sizes, 0, N - 1);
        int moves = 0;

		int* delta = new int[N - 1];
		int easypass = 0;
		
		for(int j = 0; j < N - 1; j++) {
			delta[j] = sizes[j] + sizes[j] + 1 - sizes[j + 1];
			if(delta[j] > 0) {
				easypass++;
			}
		}

        for(int j = 0; j < N; j++) {
            if(A > sizes[j]) {
                A += sizes[j];
            }
            else {
				int tempA = A;
				int k = 0;
				for(; k < N; k++) {
					if(tempA > sizes[j]) {
						break;
					}
					tempA += (tempA - 1);
				}

				if(k <= easypass) {
					moves += k;
					A = tempA + sizes[j];
				}
				else {
					moves++;
				}
			}

        }

		output << "Case #" << i + 1 << ": " << moves << endl;
		//cout << "Case #" << i + 1 << ": " << moves << endl;
	}

    return 0;
}