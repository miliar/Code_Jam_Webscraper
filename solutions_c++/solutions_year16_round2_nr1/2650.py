#include<bits/stdc++.h>
#include<conio.h>
using namespace std;
list<char> li;
int find(char ch)
{
	for(list<char>::iterator i=li.begin();i!=li.end();i++) if(*i==ch) return true;
	return false;
}
void display()
{
	for(list<char>::iterator i=li.begin();i!=li.end();i++) cout<<*i;
	cout<<endl;
}
void finderase(char ch)
{
	list<char>::iterator i;
	for(i=li.begin();i!=li.end();i++) if(*i==ch) break;
	li.erase(i);
}
int main()
{
	ifstream file1("A-large.in");
	ofstream file2("file2.txt");
	int t;
	file1>>t;
	for(int j=0;j<t;j++)
	{
		string str;
		file1>>str;
		list<int> li1;
		int l=str.length();
		for(int i=0;i<l;i++) li.push_back(str[i]);
		while(!li.empty())
		{
			while(find('Z')) {li1.push_back(0);finderase('Z');finderase('E');finderase('R');finderase('O');}
			while(find('X')) {li1.push_back(6);finderase('S');finderase('I');finderase('X');}
			while(find('G')) {li1.push_back(8);finderase('E');finderase('I');finderase('G');finderase('T');finderase('H');}
			while(find('W')) {li1.push_back(2);finderase('T');finderase('W');finderase('O');}
			while(find('U')) {li1.push_back(4);finderase('F');finderase('O');finderase('U');finderase('R');}
			while(find('O')) {li1.push_back(1);finderase('O');finderase('N');finderase('E');}
			while(find('T')) {li1.push_back(3);finderase('T');finderase('H');finderase('R');finderase('E');finderase('E');}
			while(find('F')) {li1.push_back(5);finderase('F');finderase('I');finderase('V');finderase('E');}
			while(find('V')) {li1.push_back(7);finderase('S');finderase('E');finderase('V');finderase('E');finderase('N');}
			while(find('I')) {li1.push_back(9);finderase('N');finderase('I');finderase('N');finderase('E');}
		}
		li1.sort();
		file2<<"Case #"<<j+1<<": ";
		for(list<int>::iterator i=li1.begin();i!=li1.end();i++) file2<<*i;
		file2<<endl;
	}
}
