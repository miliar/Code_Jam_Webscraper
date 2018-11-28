#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int  SolveCase(int num)
{
	int digitBitSet = 0;
	int curNum = num;
	
	while(1)
	{
		int tmpNum = curNum;
		while(tmpNum) {
			digitBitSet |= (1<<(tmpNum%10));
			tmpNum /= 10;
		}
		
		if(digitBitSet == (1<<10)-1)
		{
			return curNum;
		}
		
		curNum += num;
	}	
	
	return -1;
}

int main() 
{
	FILE *fin = freopen("A-small.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-small.out", "w", stdout);
	
	int testCases;
	cin >> testCases;
	for(int t = 1; t <= testCases; t++)
	{		
		int num;
		cin >> num;
		
		cout << "Case #" << t << ": ";
		
		if (num == 0) cout << "INSOMNIA";
		else          cout << SolveCase(num);
		
		cout << endl;
	}
	
	exit(0);
}
