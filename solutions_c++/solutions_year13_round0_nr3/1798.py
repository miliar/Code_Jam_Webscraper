#include<iostream>
#include<queue>
#include<map>
#include<cstring>
#include<utility>
#include<vector>
#include<climits>
#include<iomanip>
#include<set>
#include<algorithm>
#include<string>
#include<cmath>
#include<math.h>
#include<cstdlib>
#include<stack>
#include<cstdio>
#include<stdio.h>
using namespace std;

bool isPalindrome(string num)
{
	if(num.size() == 1)
		return true;

	for(int i = 0; i <= num.size() / 2; i++)
		if(num[i] != num[num.size() - i - 1])
			return false;
	
	return true;
}

string intToString(long long num)
{
	string res = "";
	string addition = "0";
	if(num == 0)
		return "0";

	while(num > 0)
	{
		addition[0] += num % 10;
		res.insert(0, addition);
		addition = "0";
		num /= 10;
	}
	
	return res;
}


int main()
{
	vector<long long>fair;
	for(long long i = 0; i * i <= 100000000000000; i++)
	{
		if(isPalindrome(intToString(i)) && isPalindrome(intToString(i * i)) )
			fair.push_back(i * i);
	}
	freopen("output.txt", "w", stdout);
	freopen("C-large-1.in", "r", stdin);
	long long start, end;
	int t, res;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		res = 0;
		cin >> start >> end;
		res = (upper_bound(fair.begin(), fair.end(), end) - fair.begin()) - (lower_bound(fair.begin(), fair.end(), start) - fair.begin());
		cout << "Case #" << i <<": " << res << endl;
				
	}

	
	
	return 0;
		
}	