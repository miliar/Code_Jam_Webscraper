#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<sstream>
using namespace std;
long double divisor(long double num)
{
	//cout << num<<endl;
	for (long double i=2;i <= sqrt(num);++i)
	{
		
		if (fmod(num,i) == 0)
		{
			cout << i<<endl;
			
			return i;
		}
		
	}
	return 0;
}
int main()
{
	long double res;
	ifstream in("test.txt");
	ofstream out("result.out");
	int x;
	in >> x;
	int n, j;
	in >> n >> j;
	string inside="1000000000000111";
	out << "Case #1:" << endl;
	vector < long double > divs;
	int k=0;
	do
	{	
		for (int i=2;i <= 10;++i)
		{
			 res=0;
			for (int j=15;j >=0;--j)
			{
				if (inside[j] == '1')
					res+=pow(i, j);

			}
			long double pom=divisor(res);
			if(pom<20 && pom>0)
				divs.push_back(pom);
		}
		if ((divs.size() == 9) && (inside[inside.length()-1]=='1') && (inside[0] == '1'))
		{
			k++;
			out << inside << " ";
			for (int l=0;l < divs.size();++l)
				out << divs[l]<<" ";
			out << endl;

		}
		divs.clear();	
		if (k == 51)
			break;
	} while (std::next_permutation(inside.begin(), inside.end()));
	 inside="1000000000011111";
	k=0;
	do
	{
		for (int i=2;i <= 10;++i)
		{
			res=0;
			for (int j=15;j >= 0;--j)
			{
				if (inside[j] == '1')
					res+=pow(i, j);

			}
			long double pom=divisor(res);
			if (pom<20 && pom>0)
				divs.push_back(pom);
		}
		if ((divs.size() == 9) && (inside[inside.length() - 1] == '1') && (inside[0] == '1'))
		{
			k++;
			out << inside << " ";
			for (int l=0;l < divs.size();++l)
				out << divs[l] << " ";
			out << endl;

		}
		divs.clear();
		if (k == 1)
			break;
	} while (std::next_permutation(inside.begin(), inside.end()));
	
	cin.get();
	cin.get();
	return 0;
}

