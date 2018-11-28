#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void showvector(vector<char> v)
{
	for (auto elem : v)
	{
		cout << elem << " ";
	}
	cout << endl;
}
string calc (string & s)
{
	vector<char> ch;
	ch.push_back(s[0]);
	for (int i = 1; i < s.size(); ++i )
	{
		if (s[i] >= ch[0]) 
			ch.insert(ch.begin(), s[i]);
		else ch.push_back(s[i]);
	}
	string rez = "";
	for (auto letter : ch)
	{
		rez += letter;
	}
	return rez;
}
vector<string> readFromFile()
{
	vector<string> input;
	ifstream fin ("input.txt");
	int count;
	fin >> count;
	string s;
	getline(fin, s);	
	for (int i = 0; i < count; ++i)
	{
		getline(fin, s);
		string news = calc(s);
		input.push_back(news);
	}
	return input;

}
void writeResult(vector<string> & result)
{
	ofstream fout("output.txt");
	for (int i = 0; i < result.size(); ++i)
	{
		 fout << "Case #" << i + 1 <<": " << result[i] << endl;
	}
}



int main()
{
	auto tests = readFromFile();
	writeResult(tests);
	return 0;
}