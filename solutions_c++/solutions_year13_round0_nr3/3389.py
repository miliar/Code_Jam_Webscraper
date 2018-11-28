#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>

#define N 10000000

using namespace std;

vector<unsigned long long> fsTable;	

string convertNum(unsigned long long number)
{
		stringstream ss;
		ss << number;
		return ss.str();
}

bool isFair(unsigned long long num)
{
		string numStr = convertNum(num);
		int end = numStr.size()-1;
		int mid = end/2 + 1;
		for (int i = 0; i < mid; i++)
				if (numStr[i] != numStr[end-i])
						return false;
		return true;			
}

void buildTable()
{	
		unsigned long long square;
		for (int i = 1; i < N; i++)
		{
				if (isFair(i)) {
						square = i*i;
						if (isFair(square))
								fsTable.push_back(square);
				}
		}
}

int main(int argc, char* argv[])
{
		buildTable();
		/*
		for (int i = 0; i < fsTable.size(); i++)
				printf("%llu ", fsTable[i]);
		printf("\n");
		*/
		
		int T;
		unsigned long long A, B;

		scanf("%d", &T);
		for (int t = 0; t < T; t++)
		{
				scanf("%llu %llu", &A, &B);
				int count = 0;
				for (int i = 0; i < fsTable.size(); i++)
						if (A <= fsTable[i] && fsTable[i] <= B)
								count++;
				printf("Case #%d: %d\n", t+1, count);
		}

		return 0;
}
