#include <iostream>
#include <fstream>
using namespace std;

int calcsize(char a[]);
void flip(char a[], int size);
bool happy(char a[], int size);
int main()
{

	fstream input;
	input.open("B-large.in");
	ofstream codejam;
	codejam.open("B-large.out");

	char arr[1000];
	input.getline(arr, 1000);
	int T = atoi(arr);
	int count = 0;
	while (count != T)
	{
		input.getline(arr, 1000);
		int size = calcsize(arr);
		int count2 = 0;
		bool check = false;
		while (happy(arr, size) == false)
		{
			flip(arr, size);

			count2++;
		}
		if (count + 1 == 1)
		{
			codejam << "Case #" << count + 1 << ": " << count2;
		}
		else
		{
			codejam << endl << "Case #" << count + 1 << ": " << count2;
		}
		count++;
	}

	return 0;
}
int calcsize(char a[])
{
	int index = 0;
	while (a[index] != '\0')
	{
		index++;
	}
	return index;
}
void flip(char a[], int size)
{
	char first = a[0]; //either + or -

	int flip_index = 0;
	while (flip_index < size && a[flip_index] == first)
	{
		flip_index++;
	}
	if (flip_index == size && first == '+')
	{
		return;
	}
	for (int i = 0; i<flip_index; i++)
	{
		if (a[i] == '+')
		{
			a[i] = '-';
		}
		else
		{
			a[i] = '+';
		}
	}
}
bool happy(char a[], int size)
{
	for (int i = 0; i<size; i++)
	{
		if (a[i] == '-')
		{
			return false;
		}
	}
	return true;
}
