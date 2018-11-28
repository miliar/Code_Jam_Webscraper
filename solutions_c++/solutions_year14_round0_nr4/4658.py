#include<set>
#include<climits>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<iostream>
#include <sstream>
#include <fstream>
using namespace std;

int main()
{
	int test, testcase;
	freopen("D:\\codejam\\D-large.in","r", stdin);
	freopen("D:\\codejam\\outlarge.txt", "w", stdout);
	cin >> testcase;
	int n;
	double k;
	vector<double> first, second;
	for(test=1;test<=testcase;test++)
	{
		cout << "Case #" << test << ": ";

		cin >> n;
		int p = n;
		while(p--)
		{
			cin >> k;
			first.push_back(k);
		}
		
		while(n--)
		{
			cin >> k;
			second.push_back(k);
		}
		int X = first.size();
		sort(first.begin(), first.end());
		sort(second.begin(), second.end());

		int ans1=0, ans2 = 0;

		for(int i=X-1, j=X-1; i>=0 && j>=0; j--)
		{
			if(first[i] > second[j]){ans1++; i--;}
		}

		for(int i=X-1, j=X-1; i>=0 && j>=0; i--)
		{
			if(first[i] < second[j]){ans2++; j--;}
		}
		ans2 = X-ans2;
		cout << ans1 << " " << ans2 << endl;
		first.clear();
		second.clear();
	}
	return 0;
}