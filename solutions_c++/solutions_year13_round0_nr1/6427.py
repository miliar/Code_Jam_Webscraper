#include <iostream>
#include <fstream>
#include <string>
#include <windows.h>
#define N 4
using namespace std;

bool RowColumnDiagResult(string line, char symbol)
{
	char *p = &line[0];
	int i = 0;
	while (i++ < N) {
		if (*p == symbol || *p == 'T') {
			p++;
			continue;
		}
		else
			return false;
	}
	return true;
}

int MatrixResult(string m[])
{
	int i = 0;
	while (i < N) {
		if (RowColumnDiagResult(m[i], 'X'))
			return 0;
		if (RowColumnDiagResult(m[i], 'O'))
			return 1;
		i++;
	}
	return -1;
}

void MatrixTranspose(string m[])
{
	int i = 0, j;
	char temp;
	while (i < N -1) {
		for (j = i + 1;j < N;j++) {
			temp = m[i][j];
			m[i][j] = m[j][i];
			m[j][i] = temp;
		}
		i++;
	}
}

bool findempty(string line)
{
	int i = 0;
	while (i < N) {
		if (line[i] == '.')
			return true;
		i++;
		continue;
	}
	return false;
}

int GetResult(string m[])
{
	int i = 0;
	char diagline[N];
	if (MatrixResult(m) == 0)
		return 0;
	else if (MatrixResult(m) == 1)
		return 1;

	i = 0;
	MatrixTranspose(m);
	if (MatrixResult(m) == 0)
		return 0;
	else if (MatrixResult(m) == 1)
		return 1;

	i = 0;
	while (i < N) {
		diagline[i] = m[i][i];
		i++;
	}
	string dline(diagline);
	if (RowColumnDiagResult(dline, 'X'))
			return 0;
	if (RowColumnDiagResult(dline, 'O'))
			return 1;

	i = 0;
	while (i < N) {
		diagline[i] = m[N - 1 - i][i];
		i++;
	}
	if (RowColumnDiagResult(diagline, 'X'))
			return 0;
	if (RowColumnDiagResult(diagline, 'O'))
			return 1;
	
	i = 0;
	while (i < N) {
		if (findempty(m[i]))
			return 3;
		i++;
	}
	MatrixTranspose(m);
	return 2;	 
}

int main()
{
	ifstream myfile;
	ofstream outputfile;
	string line;
	string matrix[N];
	int T;
	int count;
	int l;
	myfile.open("A-large.in");
	outputfile.open("output.out");
	if (myfile.is_open()) {
		getline (myfile, line);
		T = atoi(line.c_str());
		count = T;
		while (count-- >= 1) {
			if (T -count != 1) {
				getline(myfile, line);
				outputfile<<endl;
			}
			outputfile << "Case #" << T - count << ": ";
			for (l = 0;l < N;l++)				
				getline(myfile, matrix[l]);
			if (GetResult(matrix) == 0)
				outputfile<<"X won";
			else if (GetResult(matrix) == 1)
				outputfile<<"O won";
			else if (GetResult(matrix) == 2)
				outputfile<<"Draw";
			else
				outputfile<<"Game has not completed";
		}
	}
	myfile.close();
	outputfile.close();
	system("pause");
	return 0;
}