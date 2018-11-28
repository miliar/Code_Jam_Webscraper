#include<iostream>
using namespace std;

void setDigits(int arr[], long multiple, int* countDigits)
{
	while (multiple)
	{
		int digit = multiple % 10;
		if (arr[digit] == 0)
		{
			arr[digit] = 1;
			(*countDigits)++;
		}
		multiple /= 10;
	}
}

void countSheep(int i, int n)
{
	if (n == 0)
	{
		cout << "Case #" << i << ": INSOMNIA" << endl;
		return;
	}
	long multiple = 0;
	int arr[10] = { 0 };
	int countDigits = 0;

	int j = 1;
	while (countDigits < 10)
	{
		multiple = j * (long)n;
		setDigits(arr, multiple, &countDigits);
		j++;
	}
	cout << "Case #" << i << ": " << multiple << endl;
}

int main()
{
	int t, n;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		//int input[100] = { 0, 1, 2, 11, 1692, 412910, 20, 8, 590388, 212958, 976147, 166, 263599, 929350, 68609, 705674, 714506, 123977, 476345, 242825, 999991, 644346, 472989, 361660, 394253, 9, 416537, 969615, 576830, 717855, 34, 999993, 280545, 548702, 25, 286565, 404368, 124, 639217, 867117, 999998, 10, 50068, 601091, 579484, 1000000, 135359, 999992, 6, 999997, 999995, 778391, 324999, 677643, 999999, 38725, 792404, 207268, 999996, 145205, 564038, 148619, 585414, 246262, 565572, 805448, 250487, 451786, 40, 53424, 389730, 491918, 671813, 125, 200, 864140, 208250, 4, 629132, 784642, 887443, 65229, 3, 7, 269501, 19418, 999994, 961312, 917725, 68017, 552173, 582253, 810974, 12500, 778785, 1250, 436064, 5, 121394, 125000 };
		cin >> n;
		//countSheep(i, input[i-1]);
		countSheep(i, n);
	}
}