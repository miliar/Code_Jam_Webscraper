#include <vector>
#include <string>
#include <fstream>
#include <iostream>
using namespace std;
int INF = 2000000000;
int main()
{
	int t;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> t;
	for (int times = 1; times <= t; times++)
	{
		string s;
		fin >> s;
		string answer = "";
		for (int i = 0; i < s.size(); i++)
		{
			char cur = s[i];
			if (cur >= answer[0])
			{
				answer = cur + answer;
			}
			else
			{
				answer = answer + cur;
			}

		}
		fout << "Case #" << times << ": " << answer << endl;
	}
	cin.get();
	return 0;
}
//Number 1
/*string s;
fin >> s;
string answer = "";
for (int i = 0; i < s.size(); i++)
{
char cur = s[i];
if (cur >= answer[0])
{
answer = cur + answer;
}
else
{
answer = answer + cur;
}

}
fout << "Case #" << times << ": " << answer << endl;*/
/*
nt n;
fin >> n;
vector<vector<int> > lists;
for (int i = 0; i < (2 * n - 1); i++)
for (int j = 0; j < n; j++)
fin >> lists[i][j];
int min = INF;
for (int i)
cout << "Case #" << times << ": " <<  endl;
*/