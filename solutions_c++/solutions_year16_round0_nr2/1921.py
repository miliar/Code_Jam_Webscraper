#include <iostream>

using namespace std;

void flip (int arr[], int index);
int findPlus (int arr[], int index);
void printArr (int arr[], int size);

int main () {
	int T, size, count, i, j;
	int arr[100];
	char c;
	
	cin >> T;
	getchar();
	
	for (i=1;i<=T;i++) {
		size = 0;
		count = 0;
		
		do {
			c = getchar();
			if (c == '+') {
				arr[size] = 1;
			} else if (c == '-') {
				arr[size] = -1;
			}
			size++;
		} while (c != '\n');
		size--;
		
		for (j=size-1;j>=0;j--) {
			if (arr[j] == -1) {
				if (arr[0] == -1) {
					flip(arr, j);
					count++;
				} else {
					flip(arr, findPlus(arr, j));
					flip(arr, j);
					count += 2;
				}
				
				//cout << "count: " << count << endl;
				//printArr(arr, size);
			}
		}
		
		cout << "Case #" << i << ": " << count << endl;
	}
	
	return 0;
}

void flip (int arr[], int index) {
	int temp[index+1];
	int i;
	for (i=0;i<=index;i++) {
		temp[i] = arr[i]*(-1);
	}
	for (i=0;i<=index;i++) {
		arr[i] = temp[index-i];
	}
	return;
}

void printArr (int arr[], int size) {
	int i;
	cout << "arr: ";
	for (i=0;i<size;i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
	return;
}

int findPlus (int arr[], int index) {
	int i;
	for (i = index; i>=0; i--) {
		if (arr[i] == 1) {
			return i;
		}
	}
	
	return -1;
}
