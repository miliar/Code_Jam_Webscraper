#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int max(string s, int n)
{
	int max = 0;
	for (int i = 0; i < n; i++)
		max += (s[i] - '0');
	return max;
}

int main() {
	ifstream in("A - small - practice.in");
	ofstream out("A - small - practice.out");
	int t, smax;  string s; int count = 0; int friends = 0;
	in >> t; 

	for (int i = 0; i < t; i++)
	{
		in >> smax; 
		
		in >> s; 
		for (int i1 = 1; i1 < s.length() ; i1++)
		{
			count += s[i1 - 1] - '0'; 
			if (i1 > max(s,i1))
			{

				friends += (i1 - max(s, i1));
				s[i1 - 1] += (i1 - max(s, i1));
			}
			
		}
			out << "Case #"<<(i + 1) << 
			": " << friends << endl;
			friends = 0;

		count = 0;
	}

	cin >> smax;
}