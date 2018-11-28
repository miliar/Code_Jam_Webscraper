#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

bool palindrome(string s)
{
	if(s.size() == 1)
		return true;
	int start = 0, end = s.size()-1;
	while(start < end)
	{
		if(s[start] != s[end])
			return false;
		start++;
		end--;
	}
	return true;
}

string intToString(int t)
{
	stringstream s;
	s << t;
	string temp;
	s >> temp;
	return temp;
}

int main(int argc, char** argv)
{
	int numCases;
	ifstream in(argv[1]);
	ofstream out("output.txt");
	stringstream stream;
	
	int start, end;
	in >> numCases;
	for(int i = 0; i < numCases; i++)
	{
		in >> start;
		in >> end;
		int num = 0;
		//for(int j = (int) sqrt(start); j <= (int) sqrt(end); j++)
		for(int j = start; j <= end; j++)
		{
			// check if j is palindrome
			if(!palindrome(intToString(j)))
				continue;
			// take square_root of j
			
			int t = (int)sqrt(j*1.0);
			if(t*t != j)
				continue;
			
			if(palindrome(intToString(t)))
				num++;
		}
		out << "Case #" << (i+1) << ": " << num << endl;
	}
}