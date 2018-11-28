#include<iostream>
#include<string>
#include<fstream>
using namespace std;

ofstream myout;
void myfunc(string str, int c);
int main()
{
	int total = 0, count = 1;
	string str;
	std::string::size_type sz;
	ifstream fin;
	fin.open("B-large.in");
	getline(fin, str, '\n');
	total = std::stoi(str, &sz);
	myout.open("output.txt");
	while (count <= total)
	{
		string s;
		getline(fin, s, '\n');
		myfunc(s, count);
		count++;
	}
	myout.close();
}

void myfunc(string str, int c)
{
	int flipping = 0;
	bool happy = false;
	for (int i = 0; str[i] != '\0'; i++)
	{
		if (str[i] == '+')
		{
			while (str[i + 1] != '-' && str[i + 1] != '\0')i++;
			if (str[i + 1] == '\0')happy = true;
			else
			{
				for (int j = 0; j <= i; j++)str[j] = '-';
				flipping++;
			}
		}
		else
		{
			while (str[i + 1] != '+' && str[i + 1] != '\0')i++;
			if (str[i + 1] == '\0')happy = true;
			for (int j = 0; j <= i; j++)
			{
				str[j] = '+';
				if (j == 0)flipping++;
			}
		}
	}
	myout << "Case #" << c << ": " << flipping << '\n';
}