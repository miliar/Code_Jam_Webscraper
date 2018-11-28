#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool Palindrom(int No);
int FairNSquare(int a, int b);

int main()
{
	ifstream fi;
	ofstream fo;
	string strTmp,strNo;
	char out[255];
	int T,A,B,i,j;

	//fi.open ("test.in");
	//fo.open("test.out");

	fi.open ("C-small-attempt0.in");
	fo.open("C-small-attempt0.out");

	// Get number of cases, N
	getline(fi,strTmp);
	T = atoi(strTmp.c_str());

	for (i = 0; i<T ; i++)
	{
		// Get N & M
		getline(fi,strTmp);
		j = strTmp.find(' ');
		strNo = strTmp.substr(0,j);
		A = atoi(strNo.c_str());
		strNo = strTmp.substr(j,strTmp.length()-j);
		B = atoi(strNo.c_str());

		// Write result to file
		sprintf_s(out,"Case #%d: %d\n",i+1,FairNSquare(A,B));
		fo.write(out,strlen(out));
	}

	fi.close();
	fo.close();
	return 0;
}

int FairNSquare(int a, int b)
{
	int count = 0;
	for (int i=ceil(sqrt(a));i<=floor(sqrt(b));i++)
	{
		if (Palindrom(i) && Palindrom(i*i))
		{
			count++;
		}
	}
	return count;
}

bool Palindrom(int intNo)
{
	int tmp = intNo, pal = 0;
	while (tmp>0)
	{
		pal = pal*10 + tmp%10;
		tmp = tmp/10;
	}
	return (intNo == pal);
}