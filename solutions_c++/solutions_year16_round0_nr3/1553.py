#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>


using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int main ()
{
	ofstream output;
	output.open("out.txt");
	output << "Case #1:\n";
	int j = 0;
	int i = -1;
	while(j <500)
	{
		i = i+1;
		int k = i;
		string s;
		int p = 0;
		while(k !=0)
		{
			if (k%2 ==0)
				s = "00"+s;
			else{
				p = p+1;
				s = "11"+s;
			}
			k = k/2;
		}
		
			output << "11";
			j++;
			int len = 28-s.length();
			forn(y, len)
				output << "0";
			output<<s;
			output<<"11 ";
			output <<"3 4 5 6 7 8 9 10 11";
			output <<"\n";
		
	}
}

