#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional>
#include <deque>
using namespace std;

int main()
{
	ifstream in("in.in");
	ofstream write;
	write.open("out.expect");
	int T;
	deque <char> de;
	string S,tmp;
	in >> T;
	for (int i = 0; i < T; i++)
	{
		in >> S;
		de.clear();
		de.push_back(S[0]);
		for (int j = 1; j < S.length(); j++)
		{
			if (de[0] <= S[j])
			{
				de.push_front(S[j]);
			}
			else {
				de.push_back(S[j]);
			}
		}
		tmp = "";
		for (int j = 0; j < S.length(); j++)
		{
			tmp += de[j];
		}
		cout << "Case #" << i+1 << ": " << tmp << endl;
		write << "Case #" << i+1 << ": " << tmp << endl;
	}


	
	return 0;
}