#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>

using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)

int main()
{
	ifstream in("C-large-1.in");
	ofstream out("output.txt");
	ul t,a,b;
	in>>t;
	ul k = 0;
	ul ans[50];
	ans[1] = 1;
	ans[2] = 2;
	ans[3] = 3;
	ans[4] = 11;
	ans[5] = 22;
	ans[6] = 101;
	ans[7] = 111;
	ans[8] = 121;
	ans[9] = 202;
	ans[10] = 212;
	ans[11] = 1001;
	ans[12] = 1111;
	ans[13] = 2002;
	ans[14] = 10001;
	ans[15] = 10101;
	ans[16] = 10201;
	ans[17] = 11011;
	ans[18] = 11111;
	ans[19] = 11211;
	ans[20] = 20002;
	ans[21] = 20102;
	ans[22] = 100001;
	ans[23] = 101101;
	ans[24] = 110011;
	ans[25] = 111111;
	ans[26] = 200002;
	ans[27] = 1000001;
	ans[28] = 1001001;
	ans[29] = 1002001;
	ans[30] = 1010101;
	ans[31] = 1011101;
	ans[32] = 1012101;
	ans[33] = 1100011;
	ans[34] = 1101011;
	ans[35] = 1102011;
	ans[36] = 1110111;
	ans[37] = 1111111;
	ans[38] = 2000002;
	ans[39] = 2001002;
	ans[40] = 10000001;
	ans[41] = 10011001;
	ans[42] = 10100101;
	ans[43] = 10111101;
	ans[44] = 11000011;
	ans[45] = 11011011;
	ans[46] = 11100111;
	ans[47] = 11111111;
	ans[48] = 20000002;
	REP(q, t)
	{
		in>>a>>b;
		k = 0;
		ul rez = 0;
		for (int i = 1; i<= 48; i++)
		{
			if ((ans[i]*ans[i] >= a) && (rez == 0)) rez = i;
			if (ans[i]*ans[i] > b)
			{
				k = i - rez;
				i = 50;
				break;
			}
		}
		/*for (ul i = 1; i < b; i++)
		{
			if (i*i < a) continue;
			if (i*i > b) 
			{
				i = b+1;
				continue;
			}
			stringstream ss;
			ss<<i;
			string s = ss.str();
			bool ok = true;
			for (int j = 0; j < s.size()/2; j++)
				if (s[j] != s[s.size()-1-j])
				{
					ok = false;
					break;
				}
			if (!ok) continue;
			else 
			{
				ok = true;
				stringstream ss1;
				ss1<<i*i;
				s.clear();
				s = ss1.str();
				bool ok = true;
				for (int j = 0; j < s.size()/2; j++)
					if (s[j] != s[s.size()-1-j])
					{
						ok = false;
						break;
					}
				if (ok) 
				{
					k++;
					out<<"ans["<<k<<"] = "<<i<<";\n";
				}
			}
		}
		out<<'\n';*/
		
		out<<"Case #"<<q+1<<": "<<k<<'\n';
	}
	in.close();
	out.close();
	system("pause");
	return 0;
}