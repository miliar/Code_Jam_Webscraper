#include<iostream>
#include<string>
#include<vector>
#include<fstream>
using namespace std;

int main()
{


	int t = 0,smax=0;
	char *s=new char[6];
	ifstream fin;
	ofstream fout;
	fout.open("solution.out");
	int persons = 0;
	int present = 0;
	fin.open("1.in");
	int ca = 0;
	fin >> t;
	while (t--)
	{
		fin >> smax;
		fin >> s;
		ca++;
	
		persons = 0;
		present = 0;
		for (int k = 0; k < smax; k++)
		{

			if (smax == 0)
				break;
			
			present = (s[k]-'0') + present;

			if (s[k] == '0'&&s[k + 1]!='0')
			{  
				if (present <= k){
					persons = abs((k + 1) - present)+persons;
					present = present + persons;
				}
			}

		}
		fout <<"Case #"<<ca<<": "<< persons << endl;
	}

	
	return 0;
}