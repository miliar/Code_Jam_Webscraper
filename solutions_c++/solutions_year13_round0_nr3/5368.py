#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <windows.h>
using namespace std;

void GetAB(string line, int &A, int &B)
{
	int i, j;
	i = 0;
	j = i + 1;
	char temp[1001];
	size_t len;
	while (line[j++] != ' ')
		continue;
	len = line.copy(temp, j - i - 1, i);
	temp[len] = '\0';
	A = atoi(temp);
	i = j;
	j = i+1;
	while (j++ < line.length())
		continue;
	len = line.copy(temp, j - i, i);
	temp[len] = '\0';
	B = atoi(temp);
}

bool isPint(int num) //for large input sets, it's not enough
{
	char temp[4];
	int i = 0, j;
	itoa(num, temp, 10);
	j = strlen(temp) - 1;
	while (temp[i] == temp[j] && i <= j) {
		i++;
		j--;
		continue;
	}
	if (i > j)
		return true;
	else
		return false;
}

int main()
{
	ifstream myfile;
	ofstream outputfile;
	string line;
	int T, count;
	int A = 0, B = 0;//for large input sets, it's not enough
	int sqrtA, sqrtB;
	int countPint = 0;
	myfile.open("C-small-attempt0.in");
	outputfile.open("output.out");
	if (myfile.is_open()) {
		getline (myfile, line);
		T = atoi(line.c_str());
		count = T;
		while (count-- >= 1) {
			if (T -count != 1) {
				//getline(myfile, line);
				outputfile<<endl;
			}
			outputfile << "Case #" << T - count << ": ";
			getline(myfile, line);
			GetAB(line, A, B);
			sqrtA = (int)sqrt((double)A);
			sqrtB = (int)sqrt((double)B);
			if (sqrtA * sqrtA < A)
				sqrtA += 1;
			for (;sqrtA <= sqrtB;sqrtA++) {
				if (isPint(sqrtA) && isPint(sqrtA * sqrtA))
					countPint++;
			}
			outputfile<< countPint;
			countPint = 0;
		}
	}
	myfile.close();
	outputfile.close();
	system("pause");
	return 0;
}