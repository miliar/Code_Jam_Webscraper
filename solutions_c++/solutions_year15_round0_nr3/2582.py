#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <math.h>

using namespace std;

string quantPow(string s1, int pow);
string resolveString(string s);
bool canSplit(string temp, int X);
int main(int argc, char *argv[])
{
	ifstream inFile;
	if (argc > 1)
		inFile.open(argv[1]);
	else
		inFile.open("in.in");
	ofstream outFile("out.txt");

	int cases;
	inFile >> cases;

	for (int c = 1; c <= cases; ++c)
	{
		cout << "case:" << c << endl;

		int L, X;
		string temp;
		inFile >> L;
		inFile >> X;
		inFile.ignore();
		getline(inFile, temp);
		if (temp.size() != L)
			cout << "ERROR" << endl;
		if (pow(L, X) < 3)
			outFile << "Case #" << c << ": " << "NO" << endl;
		else
		{
			string resolved = resolveString(temp);
			//cout << temp << endl;
			string result = quantPow(resolved, X);
			result = ((result == "-1") ? "YES" : "NO");
			if (result == "YES")
			if (!canSplit(temp, X))
				result = "NO";
			cout << resolved <<" "<<X<<" "<<result<< endl;
			outFile << "Case #" << c << ": " << result << "\n";
		}
		
	}
	inFile.close();
	outFile.close();
	system("pause");
	return 0;
}

string multHelper(string s1, string s2)
{
	if (s1 == "--")
		s1 = "";
	if (s2 == "--")
		s2 == "";
	//check for minus here
	if (s1[0] == '-' && s2[0] == '-')
	{
		s1 = s1.substr(1);
		s2 = s2.substr(1);
	}
	else if (s1[0] == '-' || s2[0] == '-')
	{
		if (s1[0] == '-')
		{
			string s = "-" + multHelper(s1.substr(1), s2);
			if (s.size() == 3)
				return s.substr(2);
			else
				return s;
		}
		else
		{
			string s = "-" + multHelper(s1, s2.substr(1));
			if (s.size() == 3)
				return s.substr(2);
			else
				return s;
		}
	}
	if (s1 == "1" && s2 != "")
		return s2;
	if (s2 == "1" && s1 != "")
		return s1;
	if (s1 == s2 && s1 != "")
	{
		return "-1";
	}
	if (s1 == "i" && s2 == "j")
		return "k";
	if (s1 == "i" && s2 == "k")
		return "-j";
	if (s1 == "j" && s2 == "i")
		return "-k";
	if (s1 == "j" && s2 == "k")
		return "i";
	if (s1 == "k" && s2 == "i")
		return "j";
	if (s1 == "k" && s2 == "j")
		return "-i";
	if (s1 == "" && s2 == "")
		return "";
	if (s1 == "" && s2 != "")
		return s2;
	if (s1 != "" && s2 == "")
		return s1;
}

string quantPow(string s1, int pow)
{
	if (pow == 0)
	{
		return "1";
	}
	if (s1 == "i" || s1 == "j" || s1 == "k")
	{
		int p = pow % 4;
		if (p == 0)
			return "1";
		if (p == 1)
			return s1;
		if (p == 2)
			return "-1";
		if (p == 3)
			return "-" + s1;
		if (p == 4)
			return "1";
	}
	if (s1 == "-i" || s1 == "-j" || s1 == "-k")
	{
		int p = pow % 4;
		if (p == 0)
			return "1";
		if (p == 1)
			return s1;
		if (p == 2)
			return "-1";
		if (p == 3)
			return s1.substr(1);
		if (p == 4)
			return "1";
	}
	if (s1 == "1")
		return "1";
	if (s1 == "-1")
	{
		if (pow % 2 == 0)
			return "1";
		else
			return "-1";
	}

}

string resolveString(string s)
{
	string s1, s2;
	while (s.size() > 1)
	{
		/*cout << "before: ";
		for (int i = 0; i < s.size(); ++i)
			cout << s[i];
		cout << endl;*/
		if (s.size() == 2 && s[0] == '-')
			return s;
		if (s[0] == '-')
		{
			s1 = s.substr(0, 2);
			s = s.erase(0, 2);
		}
		else
		{
			s1 = s.substr(0, 1);
			s = s.erase(0, 1);
		}
		if (s[0] == '-')
		{
			s2 = s.substr(0, 2);
			s = s.erase(0, 2);
		}
		else
		{
			s2 = s.substr(0, 1);
			s = s.erase(0, 1);
		}
		string toInsert = multHelper(s1, s2);
		s.insert(0, toInsert);
		/*cout << "after: ";
		for (int i = 0; i < s.size(); ++i)
			cout << s[i];
		cout << endl;*/
	}
	return s;
}

bool canSplit(string temp, int X)
{
	string newString = "";
	for (int i = 0; i < X; ++i)
		newString.append(temp);

	for (int i = 1; i <= newString.size(); ++i)
	{
		if (resolveString(newString.substr(0,i)) == "i")
		for (int j = i+1; j < newString.size(); ++j)
		{
			if (resolveString(newString.substr(i, j-i)) == "j")
			{
				if (resolveString(newString.substr(j)) == "k")
					return true;
			}
			
		}
	}
	return false;
}
