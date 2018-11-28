#include<iostream>
#include<cmath>
#include<map>
#include<string>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<set>
#include<iomanip>
#include<algorithm>
using namespace std;
typedef unsigned long long int ULL;
int main()
{
	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	int test;
	cin >> test;
	for(int t = 1; t <= test; ++t)
	{
		int firstRow, secondRow;
		int count = 0;
		int temp, value = 0;
		set<int> first;
		cin >> firstRow;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				cin >> temp;
				if(i == firstRow - 1) first.insert(temp);
			}
		}
		cin >> secondRow;
		for(int i = 0; i < 4; ++i)
		{
			for(int j = 0; j < 4; ++j)
			{
				cin >> temp;
				if( (i == secondRow - 1) && (count <= 1) )
				{
					set<int>::iterator it = first.find(temp);
					if(it != first.end()) { ++count; value = temp; }
				}
			}
		}
		cout << "Case #" << t << ": ";
		if(count == 1)		cout << value;
		else if (count > 1)		cout << "Bad magician!";
		else		cout << "Volunteer cheated!";
		cout <<  endl;
	}
	return 0;
}