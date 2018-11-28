#include <fstream>
#include <string>
#include <list>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.out");

int main ()
{
	int N;
	fin >> N;
	for (int t = 1; t <= N; t++)
	{
		string str;
		fin >> str;
		list <char> ans;
		ans.push_back (str[0]);
		for (int i = 1; i < str.size (); i++)
			if (str[i] >= ans.front ())
				ans.push_front (str[i]);
			else
				ans.push_back (str[i]);
		fout << "Case #" << t << ": ";
		for (list <char>::iterator it = ans.begin (); it != ans.end (); it++)
			fout << *it;
		fout << endl;
	}
}

