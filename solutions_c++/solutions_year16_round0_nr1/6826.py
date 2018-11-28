#include<stdio.h>
#include<vector>
#include<iostream>
#include<fstream>

using namespace std;

int tc;
int N;
vector<bool> check;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input_a.txt");
	fout.open("output_a.txt");
	fin >> tc;
	for(int t = 1; t <= tc; t++)
	{
		check = vector<bool>(10, false);
		int cnt = 0;
		fin >> N;
		
		if(N == 0)
		{
			fout << "Case #" << t << ": INSOMNIA" << endl;
			continue;
		}
		
		int mul = 1;
		while(cnt < 10)
		{
			int tmp = N * mul;
			while(tmp != 0)
			{
				if(!check[tmp % 10])
				{
					cnt++;
					check[tmp % 10] = true;
				}
				tmp /= 10;
			}
			mul++;
		}
		
		fout << "Case #" << t << ": " << N * (mul - 1) << endl;
	}
}
