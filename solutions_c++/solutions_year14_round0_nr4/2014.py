#include<conio.h>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<functional>
#include<iterator>

using namespace std;

ifstream in("test.txt");
ofstream out("result.txt");

class Dwar{
	int nob;//no of blocks
	double naomi[1000], ken[1000];
	int fairWin, unfairWin;
public:
	void getData();
	void check(int &noc);
};

int main()
{
	const int T = 50;
	Dwar caseArr[T];
	int noc;
	in >> noc;
	int i;
	for (i = 0; i < noc; i++)
	{
		caseArr[i].getData();
	}
	for (i = 0; i < noc; i++)
	{
		caseArr[i].check(i);
	}


//	_getch();
	return 0;
}

void Dwar::getData()
{
	in >> nob;
	
	for (int  i = 0; i < nob; i++)
	{
		in >> naomi[i];
	}
	
	for (int i = 0; i < nob; i++)
	{
		in >> ken[i];
	}
	sort(begin(naomi),end(naomi),greater <double>());
	sort(begin(ken), end(ken), greater <double>());

/*	for (int i = 0; i < nob; i++)
	{
		cout<< naomi[i] << " ";
	}
	cout << endl;
	for (int i = 0; i < nob; i++)
	{
		cout << ken[i] << " ";
	}
*/
}

void Dwar::check(int &caseNo)
{
	
	fairWin = 0; unfairWin = nob;
	int nhead = 0;int khead = 0;
	int ntail = nob - 1; int ktail = nob - 1;
	for (int i = 0; i < nob; i++)
	{
		if (naomi[nhead] > ken[khead])
		{
			fairWin++;
			ktail--;
			nhead++;
		}
		else
		{
			nhead++;
			khead++;
		}
	}

	nhead = khead = 0;
	ntail = ktail = nob - 1;

	for (int i = 0; i < nob; i++)
	{	
		if (naomi[ntail] < ken[ktail])
		{
			khead++;
			ntail--;
			unfairWin--;
		}
		else
		{
			ktail--;
			ntail--;
		}
	}
	
	out << "Case #" << caseNo+1 << ": " << unfairWin << " " << fairWin << endl;
}