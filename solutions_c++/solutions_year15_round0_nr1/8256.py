// ProblemAStandingOvation.cpp: определяет точку входа для консольного приложения.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-small-attempt0.out");
	int t;
	cin>>t;

	for(int r=1;r<=t;r++)
	{
		string s;
		int n=0;
		cin>>n;
		cin>>s;
		
		int i=0;
		
		int summa=0;
		int want=0;
	
		while (n+1!=i)
		{
			summa+=s[i++]-'0'-1;
			if (summa<0)
			{
				summa++;
				want++;
			}
		}
		cout<<"Case #"<<r<<": "<<want<<endl;
	}

	return 0;
}

