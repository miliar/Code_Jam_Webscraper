#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <assert.h>
#include <fstream>
#include <cmath>
#include <cstring>

using namespace std;

void convertstringtobasearr(long int* &base, string numberholder);
long int findfirstdivisible(long int base);
string DecToBin(int number);
int main()
{
	fstream output;
	output.open("output.txt",ios::out);
	int t, n, j;
	int count_permutations = -2;
	cin >> t;
	bool print = false;
	assert(t == 1);
	cin >> n >>j;
	long int* basearr = new long int[9]; // holds the decimal representations of the base string
	string * finalresult = new string[j];
	string numberholder = "";
	long int* checkholder = new long int[9]; // holds the  divisors
	long int check;
	long int tobeconverted;

	int count = 0;
	while (count != j)
	{
		count_permutations += 2;
		cout << " # " << (count_permutations +1 / 2)  << endl;
		if (print) {	
			count++;
			output << " " << numberholder << " ";
			for (int i = 0; i < 9;i++)
			{
				output << checkholder[i] << " ";
			}
			output << endl;
			print = false;
		}
		tobeconverted = 1 + pow(2, n - 1) + count_permutations;
		numberholder = DecToBin(tobeconverted);
		convertstringtobasearr(basearr, numberholder);
		for (int i = 0; i < 9;i++)
		{
			check = findfirstdivisible(basearr[i]);
			if (check == -1) 
			{
				break;
			}
			else
			{
				checkholder[i] = check;
			}
			if (i == 8)
			{
				print = true;
			}
		}
	}

	//testing 




}
void convertstringtobasearr(long int* &base, string numberholder)
{
	char* temp = new char[numberholder.size() + 1];
	memcpy(temp, numberholder.c_str(), numberholder.size() + 1);
	for (int i = 0;i < 9; i++)
	{
		base[i] = strtol(temp, NULL, i + 2);
	}
}
long int findfirstdivisible(long int base)
{
	long int temp;
	for (int i = 2;i < base/2;i++)
	{
		temp = base % i;
		if (temp == 0)
			return i;
	}
	return -1;
}

string DecToBin(int number)
{
	if (number == 0) return "0";
	if (number == 1) return "1";

	if (number % 2 == 0)
		return DecToBin(number / 2) + "0";
	else
		return DecToBin(number / 2) + "1";
}




