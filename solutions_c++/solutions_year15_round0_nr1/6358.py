#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin;
	fin.open("in.txt");
	ofstream out;
	out.open("output.txt");
	int num;
	fin>>num;
	int i=0;
	int max;
	string s;
	for(int j=0;j<num;j++)
	{
		int counter=0;
		fin>>max;
		fin>>s;
		int standing=0;
		int i=0;

		while(i<=max)
		{
			standing = standing + s[i]-'0';
			while(standing-1<i)
			{
				counter++;
				standing++;
			}
			i++;
		}
		out<<"Case #"<<j+1<<": "<<counter;
		out<<endl;

	}
	return 0;
}