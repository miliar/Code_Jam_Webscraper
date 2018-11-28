#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;


int main()
{
	ifstream in("A-large.in");
	ofstream out("1.txt");
	unsigned int T;
	unsigned int i, j;
	in >> T;
	string s;
	for (i = 0; i < T; i++)
	{
		vector<int> sol;
		map<char, int> temp;
		map<char, int>::iterator it;
		temp.clear();
		sol.clear();
		in >> s;
		for (j = 0; j < s.length(); j++)
			temp[s[j]]++;
		it=temp.find('Z');
		while(it!=temp.end()&&temp['Z']>0)
		{
			sol.push_back(0);
			temp['Z']--;
			temp['E']--;
			temp['R']--;
			temp['O']--;
		}
		it=temp.find('U');
		while(it!=temp.end()&&temp['U']>0)
		{
			sol.push_back(4);
			temp['F']--;
			temp['O']--;
			temp['U']--;
			temp['R']--;
		}
		it=temp.find('G');
		while(it!=temp.end()&&temp['G']>0)
		{
			sol.push_back(8);
			temp['E']--;
			temp['I']--;
			temp['G']--;
			temp['H']--;
			temp['T']--;
		}
		it=temp.find('W');
		while(it!=temp.end()&&temp['W']>0)
		{
			sol.push_back(2);
			temp['T']--;
			temp['W']--;
			temp['O']--;
		}
		it=temp.find('X');
		while(it!=temp.end()&&temp['X']>0)
		{
			sol.push_back(6);
			temp['S']--;
			temp['I']--;
			temp['X']--;
		}
		it=temp.find('S');
		while(it!=temp.end()&&temp['S']>0)
		{
			sol.push_back(7);
			temp['S']--;
			temp['E']--;
			temp['V']--;
			temp['E']--;
			temp['N']--;
		}
		it=temp.find('T');
		while(it!=temp.end()&&temp['T']>0)
		{
			sol.push_back(3);
			temp['T']--;
			temp['H']--;
			temp['R']--;
			temp['E']--;
			temp['E']--;
		}
		it=temp.find('V');
		while(it!=temp.end()&&temp['V']>0)
		{
			sol.push_back(5);
			temp['F']--;
			temp['I']--;
			temp['V']--;
			temp['E']--;
		}
		it=temp.find('O');
		while(it!=temp.end()&&temp['O']>0)
		{
			sol.push_back(1);
			temp['O']--;
			temp['N']--;
			temp['E']--;
		}
		it=temp.find('I');
		while(it!=temp.end()&&temp['I']>0)
		{
			sol.push_back(9);
			temp['N']--;
			temp['I']--;
			temp['N']--;
			temp['E']--;
		}
		sort(sol.begin(), sol.end());
		out << "Case #"<< i + 1 <<": ";
		for (j = 0; j <sol.size()-1; j++)
			out << sol[j];
		out<<sol[j];
		out<<endl;
	}
}
