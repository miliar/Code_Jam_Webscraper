/*
 * main.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: omar
 */
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
using namespace std;
set<int> foundSoFar;
void addToSet(long long num)
{
	while(num)
	{
		int temp;
		temp = num%10;
		if(foundSoFar.count(temp)==0) foundSoFar.insert(temp);
		num/=10;
	}
}

bool isDone()
{
	return foundSoFar.size()==10;
}

void setClear()
{
	foundSoFar.clear();
}

int main()
{
	int caseCounter = 1;
	int testCases; cin>>testCases;
	bool done = false;
	while(testCases--)
	{
		setClear();
		done = false;
		int N; cin>>N; long long tempN=N;
		addToSet(tempN);
		done = isDone();
		for(unsigned int i=2;!done && i<10000;i++)
		{
			tempN = N*i;
			addToSet(tempN);
			done = isDone();
		}
		cout<<"Case #"<<caseCounter++<<": ";
		if(done) cout<<tempN<<"\n";
		else cout<<"INSOMNIA"<<"\n";
	}
	return 0;
}
