#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

ifstream fin("C-small-attempt1.in");
ofstream fout("C-small-attempt1.out");

int palindromes(int n, int s);

int flag[10000] = {0,};

int T,A,B;


int palindromes(int n, int s)
{
	int i,j,len;
	char data[100];
	char s_data[100];

	itoa(n,data,10);
	itoa(s,s_data,10);

	// integer pall??
	len = strlen(data);
	for(i=0;i<len/2;i++)
	{
		if(data[i] != data[(len-1)-i])
		{
			return 0;
		}
	}

	//sqrt pall??
	len = strlen(s_data);
	for(i=0;i<len/2;i++)
	{
		if(s_data[i] != s_data[(len-1)-i])
		{
			return 0;
		}
	}

	//cout << data << " " << s_data << endl;

	return 1;

}

int main()
{
	int i,j,z;
	int cnt = 0;

	j = 1;
	flag[1] = 1;
	for(j=1,i=3;j<=1000;i+=2)
	{
		j += i;
		if (palindromes(j, sqrt((double)j)) == 1)
		{
			flag[j] = 1;
			//cout << j << " " << sqrt((double)j) << endl;
		}
	}

	fin >> T;

	//T = 1;
	for(int z=1;z<=T;z++)
	{
		fin >> A >> B;

		cnt = 0;
		for(i=A;i<=B;i++)
		{
			if(flag[i] == 1)
			{
				cnt++;
			}
		}
		fout << "Case #" <<  z <<": " << cnt << endl;
	}

	return 0;
}


