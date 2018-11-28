#include <iostream>
#include<fstream>
#include <string>
#include <stdlib.h>
#include <math.h>
using namespace std;
void main()
{
	int T,Smax;
	string k,answer="";
	ifstream infile;
	infile.open("A-large.in");
	infile >> T;
	cout << T << endl;;
	int invite = 0;
	for (int init = 0; init <T; init++)
	{
		
		infile >> Smax>>k;
		cout << Smax << " " << k << endl;
		int Stand = 0;
		invite = 0;
		Stand += (k.at(0)-'0');
		if (Smax != 0)
		{
			int tmpin;
			for (int CountStr = 1; CountStr < k.length(); CountStr++)
			{
				tmpin = 0;
				if (Stand >= CountStr)
				{
					Stand += (k.at(CountStr) - '0');
				}
				else
				{
					tmpin+=abs(CountStr-Stand);
					Stand += tmpin;
					Stand += (k.at(CountStr) - '0');
				}
				invite += tmpin;
			}
		}
	else
					{
						
						int t = k.at(0) - '0';
						if (t < 1)
							invite = 1;
						else
							invite = 0;
					}
		answer += "Case #" + to_string(init + 1) + ": " + to_string(invite)+"\n";
		
	}
	infile.close();
	ofstream myfile;
	myfile.open("output.out");
	myfile << answer;
	myfile.close();
	cout << answer;
	system("PAUSE");
}