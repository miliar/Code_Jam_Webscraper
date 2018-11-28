#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

ifstream fin("A-large.in.txt");
ofstream fout("A-large.out.txt");

int T, S;
string s;

int main()
{
    fin >> T;
    for(int c = 1; c <= T; c++)
    {
	fin >> S >> s;
	if(S == 0)
	{
	    fout << "Case #" << c << ": " << 0 << endl;
	    continue;
	}
	std::vector<int> dp(S+1);
	dp[0]= 0;
	for(int i = 1; i <= S; i++)
	{
	    dp[i] = dp[i-1] + (int)(s[i-1] - '0');
	}
	int ret = 0;
	for(int i = 0; i <= S; i++)
	{
	    ret = std::max<int>(ret, i-dp[i]);
	}
	fout << "Case #" << c << ": " << ret << endl;
    }
	
    return 0;
}
