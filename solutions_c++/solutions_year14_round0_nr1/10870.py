#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;

string Bad = "Bad magician!";
string Cheat = "Volunteer cheated!";
vector<int> FirstCards;
vector<int> SecondCards;
vector<int> V;

vector<int> ReadCards(int num)
{
	vector<int> V;
	int count = 1, n;
	char line[10];
	while(count != 5)
	{
		if(count != num)
			for(int i=0; i<4; i++)
				cin>>n;
		else
		{
			for(int i=0; i<4; i++)
			{
				cin>>n;
				V.push_back(n);
			}
		}
		count ++;
	}
	return V;
}

int Compare()
{
	V.clear();
	vector<int>::iterator it;
	for(int i=0; i<4; i++)
	{
		it = find(SecondCards.begin(), SecondCards.end(), FirstCards.at(i));
		if(it != SecondCards.end())
			V.push_back(FirstCards.at(i));
	}
	return V.size();
}
int main()
{
	int T, First, Second, n;
	string garbage;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("Ouput.txt", "w", stdout);
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cin>>First;		
		FirstCards = ReadCards(First);

		cin>>Second;
		SecondCards = ReadCards(Second);

		printf("Case #%d: ", i);
		n = Compare();
		if(n == 0)
			printf("%s",Cheat.c_str());
		else
			if(n == 1)
				printf("%d", V.at(0));
			else
				printf("%s", Bad.c_str());
		printf("\n");
	}
	return 0;
}