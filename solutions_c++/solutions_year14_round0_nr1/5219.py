#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

int main()
{
	ifstream myfile;
	ofstream myfileOut;
    myfileOut.open("output.txt");
	myfile.open("A-small-attempt0.in");
	int t,ans,ans1,result,temp,i=1;
	int cards[4][4];
	int cards1[4][4];
	myfile>>t;
	while(t--)
	{
		temp=result =0;
		myfile>>ans;
		ans--;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				myfile>>cards[i][j];
			}
		}
		myfile>>ans1;
		ans1--;
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				myfile>>cards1[i][j];
			}
		}

		for (int i = 0; i < 4;i++)
		{
			for(int j= 0;j<4;j++)
			{
				if(cards[ans][i]==cards1[ans1][j])
				{
					result=cards[ans][i];
					temp++;
				}
			}
		}
		if(temp==1)
			myfileOut<<"Case #"<<i<<": "<<result<<"\n";
		else if(temp>1)
			myfileOut<<"Case #"<<i<<": Bad magician!\n";
		else
			myfileOut<<"Case #"<<i<<": Volunteer cheated!\n";

		i++;
	}
	myfile.close();
	myfileOut.close();
	return 0;
}
