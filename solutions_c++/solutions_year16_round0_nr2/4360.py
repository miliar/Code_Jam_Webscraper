#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T,count,flag;
	string a;
	vector <int > vec;
	ifstream in;
	in.open("in.in");
	ofstream out;
	out.open("out.expect");
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> a;
		count = 0;
		vec.clear();
		for (int j = 1; j < a.length(); j++)
		{
			if (a[j] == 45 && a[j - 1] == 43)
			{
				count++;
			}
			else if (a[j] == 43 && a[j - 1] == 45)
			{
				count++;
			}
		}
		if (a[a.length() - 1] == 45)
		{
			count++;
		}
		cout << "Case #" << i + 1 << ": " << count <<  endl;
		out << "Case #" << i + 1 << ": " <<  count << endl;
			
		
	}
	return 0;
}