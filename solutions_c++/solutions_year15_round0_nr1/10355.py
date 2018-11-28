#include <iostream>
#include <vector>
#include <iterator>
#include <cstdio>
#include <fstream>
using namespace std;

int main()	{
	int testcases = 0, currentcase = 1;
	int count = 0, friends = 0, i = 0;
	int Smax, sdata;
	ofstream file("tmp.txt");
	cin >> testcases;
	while(currentcase <= testcases)	{
		count = friends = 0;
		cin >> Smax >> sdata;
		vector<int> Sarr;
		for(int j = 0; j <= Smax; j++)	{
			Sarr.push_back(sdata%10);
			sdata/=10;
		}
		i = 0;
		for(vector<int>::reverse_iterator it = Sarr.rbegin(); it != Sarr.rend(); ++it, i++)	{
			if(*it)	{
				if(count < i)	{
					friends += i - count;
					count+=(friends + *it);
				}
				else
					count+=(*it);
			}
		}
		file<<"Case #" << currentcase << ": " << friends <<"\n";
		currentcase++;
	}
	file.close();
}
