//#include <iostream>
#include <algorithm>
#include <fstream>

#define MAX 1001

using namespace std;

ifstream cin;
ofstream cout;

typedef struct{
	int length;
	double Naomi[MAX];
	double Ken[MAX];
}blocks;

blocks War;

int WarOptimally(const blocks &War)
{
	int iNaomi = 0;
	int iKen = 0;
	while(iKen < War.length)
	{
		if(War.Naomi[iNaomi] < War.Ken[iKen])
		{
			iNaomi++;
		}
		iKen++;
	}
	return War.length-iNaomi;
}

int  DeceitfulWarOptimally(const blocks &War)
{
	int iNaomi = 0;
	int iKen = 0;
	while(iNaomi < War.length)
	{
		if(War.Ken[iKen] < War.Naomi[iNaomi])
		{
			iKen++;
		}
		iNaomi++;
	}
	return iKen;
}

int main()
{
	cin.open("D-large.in");
	cout.open("D-large.out");
	int t;
	cin>>t;
	for(int i=0; i<t; ++i)
	{
		cin>>War.length;
		for(int j=0; j<War.length; ++j)
		{
			cin>>War.Naomi[j];
		}
		for(int j=0; j<War.length; ++j)
		{
			cin>>War.Ken[j];
		}
		sort(War.Naomi, War.Naomi+War.length);
		sort(War.Ken, War.Ken+War.length);
		int resWar = WarOptimally(War);
		int resDeceitfulWar = DeceitfulWarOptimally(War);
		cout<<"Case #"<<i+1<<": "<<resDeceitfulWar<<" "<<resWar<<endl;
	}
	return 0;
}