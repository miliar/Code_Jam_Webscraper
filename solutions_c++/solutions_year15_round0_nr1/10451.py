#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include<iostream>
#include <string>
#include <vector>
#include <cstdio>
#include<cstring>

using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int ii = 0; ii < T; ii++)
	{
		int s;
		cin >> s;
		string str;
		cin >> str;
		int sum = 0;
		sum = str[0] - '0';
		int newPeople = 0;
		for (int i = 1; i <= s; i++)
		{
			int temp = str[i] - '0';
			if (sum < i)
			{
				newPeople = newPeople + (i - sum);
				sum = i;

			}
			sum = sum + temp;
		}
		cout <<"Case #"<<ii+1<<": "<<newPeople << endl;
	}
}