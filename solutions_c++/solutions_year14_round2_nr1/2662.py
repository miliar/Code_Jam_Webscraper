#if 1
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>
using namespace std;

int getActionN(const string& a_, const string& b_)
{
	string a = a_;
	string b = b_;
	a+=" ";
	b+=" ";
	if(a[0] != b[0])
		return -1;

	int aI= 1;
	int bI= 1;
	int ret =  0;

	while(1){


		if (a[aI] != b[bI])
		{
			if(a[aI] == a[aI-1])//a가 그전거랑 같다면
			{
				ret++;
				aI++;
			}
			else if(b[bI] == b[bI-1]) //b가 그전거랑 같다면
			{
				ret++;
				bI++;
			}
			else
			{
				//아무도 이전거랑 같은게 없으면 실패
				return -1;
			}

		}
		else
		{
			aI++; bI++;
		}

		if((aI == a.size()) && (bI = b.size()))
			break;
	}

	return ret;
}

void main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int nCase;
	cin>>nCase;

	for(int caseIndex = 0 ; caseIndex < nCase ; caseIndex++)
	{
		vector<string> stringSet;
		int nStr;
		cin>>nStr;
		stringSet.resize(nStr);
		for(int i = 0 ; i < nStr ; i++)
			cin>>stringSet[i];


		int r = getActionN(stringSet[0], stringSet[1]);
		if(r == -1)
			cout <<"Case #"<<caseIndex+1<<": "<<"Fegla Won"<<endl;
		else
			cout <<"Case #"<<caseIndex+1<<": "<<r<<endl;
	}
}

#endif
