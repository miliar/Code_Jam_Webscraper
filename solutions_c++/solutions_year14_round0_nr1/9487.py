#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

const char CDfv[] = "A-small-attempt0.in";
const char CRfv[] = "Output1.out";
const int CMax = 100;
const char Nr = 4;

void read(const char fv[], int A[CMax][Nr], int B[CMax][Nr], int & n);
int analyse(int A[], int B[], const int nr);
int which(int A[], int B[], const int nr);

int main()
{
	int A[CMax][Nr];
	int B[CMax][Nr];
	int n;
	read(CDfv, A, B, n);
	ofstream out(CRfv);
	for (int i = 0; i < n; i++)
	{
		int a;
		a = analyse(A[i], B[i], Nr);
		out << "Case #" << i+1 << ": ";
		if (a == 0) 
		{
			out << which(A[i], B[i], Nr);
		}
		else if (a == 1)
		{
			out << "Bad magician!";
		}
		else if (a == 2)
		{
			out << "Volunteer cheated!";
		}
		out << endl;
	}
	out.close();
}

void read(const char fv[], int A[CMax][Nr], int B[CMax][Nr], int & n)
{
	ifstream fd(fv);
	fd >> n;
	int a;
	int sk;
	int b;
	for (int i = 0; i < n; i++)
	{
		fd >> a;
		sk = 0;
		for (int h = 0; h < Nr; h++)
		{
			sk += 1;
			for (int j = 0; j < Nr; j++)
			{
				if (sk == a)
				fd >> A[i][j];
				else fd >> b;
			}
		}
		fd >> a;
		sk = 0;
		for (int h = 0; h < Nr; h++)
		{
			sk += 1;
			for (int j = 0; j < Nr; j++)
			{
				if (sk == a)
				fd >> B[i][j];
				else fd >> b;
			}
		}
	}
	fd.close();
}

int analyse(int A[], int B[], const int nr)
{
	int h = 0;
	for (int i = 0; i < nr; i++)
	{
		for (int j = 0; j < nr; j++)
		{
			if (A[i] == B[j]) 
			{
				h += 1;
			}
		}
	}
	if (h == 1) return 0;
	else if (h == 0) return 2;
	else return 1;
}

int which(int A[], int B[], const int nr)
{
	int who;
	for (int i = 0; i < nr; i++)
	{
		for (int j = 0; j < nr; j++)
		{
			if (A[i] == B[j]) 
				who = A[i];
		}
	}
	return who;
}