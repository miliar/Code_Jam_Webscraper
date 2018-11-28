#include<fstream>
#include<string>
#include<set>

using namespace std;

	fstream fin("e:/1.in");
	fstream fout("e:/1.out");

string calc()
{
	string result;
	int tmp;
	set<int> a,b;
	a.clear();
	b.clear();
	int r;	
	fin >> r;
	for (int i=0; i<4; i++)
	{
		for (int j=0; j< 4; j++)
		{
			fin >> tmp;
			if (i == r-1)
			{
				a.insert(tmp);
			}
		}
	}
	fin >> r;
	for (int i=0; i<4; i++)
	{
		for (int j=0; j< 4; j++)
		{
			fin >> tmp;
			if (i == r-1)
			{
				if (a.find(tmp) != a.end())
					b.insert(tmp);
			}
		}
	}
	
	if (b.size() == 1)
	{
		int ar = *b.begin();
		char buffer[20];		
		_itoa( ar, buffer, 10 );
		string s(buffer);		
		result = s;
	}
	if (b.size() > 1)
		result = "Bad magician!";
	if (b.size() < 1)
		result = "Volunteer cheated!";
	return result;
}

int main()
{

	int t;
	fin >> t;	
	for (int i=0; i<t; i++)
	{		
		string result;
		result = calc();
		fout <<"Case #"<<i+1<<": "<<result<<endl;
	}
	fin.close();
	fout.close();
}