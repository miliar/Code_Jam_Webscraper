#include<queue>
#include<fstream>
#include<iostream>
#include<queue>
#include<cmath>
using namespace std;

long long moteSize;
int totalMotes;
int minimum=0;
priority_queue <long long, vector <long long>, greater<long long> > sorted;
double minAdd(long long toConsider)
{
	double required=floor((double)(toConsider/moteSize));
	required=floor(pow(required,0.1)/(pow(2,0.1)))+1;
	long long value=pow(2,(required))*moteSize-(2*(required-1)+1);
	while (value<=toConsider)
	{
		required++;
		value+=(value-1);
	}
	moteSize=value;
	return required;
}
int main()
{
	int testCases;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testCases);
	for (int a=0; a<testCases; a++)
	{
		vector <long long> temps(0);
		minimum=-1;
		sorted=priority_queue <long long, vector <long long>, greater<long long> > (temps.begin(), temps.end());
		scanf("%d %d", &moteSize, &totalMotes);
		for (int ab=0; ab<totalMotes; ab++)
		{
			int temp;
			scanf("%d", &temp);
			sorted.push(temp);
		}
		if (moteSize!=1)
		{
			minimum=sorted.size();
			int lastRequired=0;
			while (sorted.size()!=0)
			{
				long long current=sorted.top();
				sorted.pop();
				if (current<moteSize)
				{
					moteSize+=current;
					if (minimum==-1||lastRequired+sorted.size()<minimum) minimum=lastRequired+sorted.size();
				}
				else
				{
					double toTest=minAdd(current);
					/*
					long long tempMote=(2*toTest*moteSize)-(2*(toTest-1)+1);
					while (sorted.top()<tempMote)
					{
						temps.push_back(sorted.top());
						tempMote+=sorted.top();
						sorted.pop();
					}
					if (temps.size()<toTest)
					*/
					if (minimum==-1||lastRequired+toTest+sorted.size()<minimum) minimum=lastRequired+toTest+sorted.size();
					
							lastRequired+=toTest;
							moteSize+=current;
					

				}
			}
			if (minimum==-1) minimum=0;
			printf("Case #%d: %d\n", a+1, minimum);
		}
		else printf("Case #%d: %d\n", a+1, totalMotes);

	}


}