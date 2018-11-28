#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>

#include <fstream>

using namespace std;



bool check_plaindrome (int num)
{
    int new_num = 0;
	int x = num;
    while(num > 0)
    {
            new_num = new_num*10 + (num % 10);
            num = num/10;
    }
	if(x == new_num)
		return true;
	else
		return false;
}


int main()
{
	string line;
	int testcases;
	
	ifstream infile;
	infile.open ("Palindromein.txt");
	getline(infile,line);
	stringstream st;
	st << line;
	st >>testcases;
	
	ofstream outfile;
	outfile.open ("Palindromeout.txt");
	for(int i=0;i<testcases;i++)
	{
		char result=0;
		bool notcompleted = false;
		int a,b;
		int count =0;
		
		getline(infile,line);
		stringstream st;
		st << line;
		st >>a>>b;
		int x =0;
		for(int j =a;j<=b;j++)
		{
			if(check_plaindrome(j))
			{
				float sq = sqrt(j);
				if((int)sq== sq && check_plaindrome(sq))
					count++;
			}

		}
		outfile<<"Case #"<<i+1<<": "<<count<<endl;
	}

	return 0;
}