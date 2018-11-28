#include<iostream>
#include<fstream>
using namespace std;

int C[20];

int Union(int A[5], int B[5]){
	for (int i = 1; i <= 20; i++)
		C[i] = 0;
	for (int i = 1; i <= 4; i++)
	{
		C[A[i]]++;
		C[B[i]]++;
	}
	int num = 0, index;
	for (int i = 1; i <= 16; i++)
	{
		if (C[i] == 2){
			index = i;
			num++;
		}
	}
	if (num == 1)
		return index;
	else if (num > 1)
		return -1;
	else
		return -2;
}
int main(){
	int T, A[5][5], B[5], C[5];
	cin >> T;
	for (int i = 1; i <= T; i++){
		int a, b;
		cin >> a;
		for (int x = 1; x <= 4; x++)
		for (int y = 1; y <= 4; y++)
			cin >> A[x][y];
		for (int x = 1; x <= 4; x++)
			B[x] = A[a][x];
		cin >> b;
		for (int x = 1; x <= 4; x++)
		for (int y = 1; y <= 4; y++)
			cin >> A[x][y];
		for (int x = 1; x <= 4; x++)
			C[x] = A[b][x];
		int mark = Union(B, C);
		if (mark > 0)
			cout << "Case #" << i << ": " << mark << endl;
		else if (mark == -1)
			cout << "Case #" << i << ": Bad magician!" << endl;
		else
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
	}
	return 0;
}