#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
void fun(vector<int>& v,long long int a)
{
	int b,i;
	while (a != 0)
	{
		b = a % 10;
		for (i = 0; i < v.size(); i++)
		{
			if (v[i] == b)
				v.erase(v.begin() + i);
		}
		a = a / 10;
	}
	
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("int.in");
	fout.open("out.txt");
	int i, t,j,z=1;
	long long int num, num2;
	fin >> t;
	while (t--)
	{

		vector<int> v(10);
		fin >> num;
		if (num == 0)
			fout << "Case #" << z << ": INSOMNIA" << endl;
		else {
			for (i = 0; i < 10; i++)
				v[i] = i;
			j = 1;
			while (v.size() != 0)
			{
				num2 = j*num;
				fun(v, num2);
				j++;
			}
			fout <<"Case #"<<z<<": "<< num2 << endl;
		}
		z++;
	}
	fin.close();
	fout.close();
}