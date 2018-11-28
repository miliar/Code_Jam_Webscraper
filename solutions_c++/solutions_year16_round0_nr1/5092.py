#include <iostream>
#include <string.h>

using namespace std;

int getCount(int N){
	int i, temp, j, k = 2;
	int number = N, iRetVal = N;
	int countArr[10];
	memset(countArr,0x00,10);
	do{
		while (N){
			countArr[N % 10] = 1;
			N = N / 10;
		}
		for (j = 0; j < 10; j++){
			temp = 0;
			if (countArr[j] == 1)
				temp = 1;
			else
				break;
		}
		if (temp == 1 && j == 10)
			break;
		else{
			N = number * k;
			iRetVal = N;
			k++;
		}
	} while (1);
	return iRetVal;
}

int main()
{
	int countArr[10];
	int iTCases = 0, iInput = 0;
	cin >> iTCases;
	for (int i = 1; i <= iTCases; i++){
		cin >> iInput;
		cout << "Case #" << i << ": ";
		if (iInput == 0)
			cout << "INSOMNIA" << endl;
		else
		{
			cout << getCount(iInput) << endl;;
		}
	}
	return 0;
}