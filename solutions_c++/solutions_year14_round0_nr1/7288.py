#include <fstream>
#include <string>
#include <list>
#include <sstream>
using namespace std;

string giveAnswer(int a[4][4],int b[4][4], int rowA, int rowB)
{
	string result;
	list<int> l;
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if(a[rowA][i] == b[rowB][j])
			{
				l.push_back(a[rowA][i]);
			}
		}
	}

	if(l.size() == 0)
	{
		result = "Volunteer cheated!";
	}
	else if(l.size() == 1)
	{
		stringstream ss;
		ss << *(l.begin());
		result = ss.str();
	}
	else
	{
		result = "Bad magician!";
	}
	return result;
}
int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t;
	in >> t;
	for(int i = 0; i < t; ++i)
	{
		int a[4][4];
		int b[4][4];
		int rowA;
		int rowB;
		in >> rowA;
		for (int k = 0; k < 4; ++k)
		{
			for (int l = 0; l < 4; ++l)
			{
				in >> a[k][l];
			}
		}
		in >> rowB;
		for (int k = 0; k < 4; ++k)
		{
			for (int l = 0; l < 4; ++l)
			{
				in >> b[k][l];
			}
		}
		out << "Case #" << i+1 << ": " << giveAnswer(a, b, rowA - 1, rowB - 1) << "\n";
	}
	return 0;
}
