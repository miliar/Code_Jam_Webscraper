#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

string Lawnmower(int Lawn[101][101], int N, int M);

int main()
{
	ifstream fi;
	ofstream fo;
	string res,strTmp,strNo;
	char out[255];
	int T,N,M,i,j,k,l,m;
	int Lawn[101][101];

	fi.open ("B-large.in");
	fo.open("B-large.out");

	// Get number of cases, N
	getline(fi,strTmp);
	T = atoi(strTmp.c_str());

	for (i = 0; i<T ; i++)
	{
		// Get N & M
		getline(fi,strTmp);
		j = strTmp.find(' ');
		strNo = strTmp.substr(0,j);
		N = atoi(strNo.c_str());
		strNo = strTmp.substr(j,strTmp.length()-j);
		M = atoi(strNo.c_str());

		// Get lawn pattern
		memset( &Lawn[0][0], 0, sizeof(Lawn) );

		for (j=0;j<N;j++)
		{
			getline(fi,strTmp);
			strTmp = strTmp + " ";
			k=0;
			m=0;
			while(k<strTmp.length())
			{
				l = strTmp.find(' ',k);
				strNo = strTmp.substr(k,l-k);
				Lawn[j][m] = atoi(strNo.c_str());
				// Update maximum value of current row
				if (Lawn[j][M]<Lawn[j][m]) Lawn[j][M]=Lawn[j][m];
				// Update maximum value of current column
				if (Lawn[N][m]<Lawn[j][m]) Lawn[N][m]=Lawn[j][m];

				m++;
				k=l+1;
			}
		}

		// Write result to file
		res = Lawnmower(Lawn,N,M);
		sprintf_s(out,"Case #%d: %s\n",i+1,res.c_str());
		fo.write(out,strlen(out));
	}

	fi.close();
	fo.close();
	return 0;
}

string Lawnmower(int Lawn[101][101], int N, int M)
{
	int i,j;

	// Check for rows
	for (i=0;i<N;i++)
	{
		for (j=0;j<M;j++)
		{
			if (Lawn[i][j] != Lawn[N][j] && Lawn[i][j] != Lawn[i][M])
			{
				return "NO";
			}
		}
	}
	return "YES";
}
