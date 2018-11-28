#include<iostream>
#include<string>
#include<memory>
#include<cstring>
#include<set>
using namespace std;


int main()
{
	int t,tt;
	cin >> tt;
	set<int> ss;
	set<int> result;
	int arr[16];
	for(t = 1; t <= tt; t ++)
	{
		ss.clear();
		result.clear();
		int n,i;
		cin >> n;
		for(i = 0; i < 16; i ++)
			cin >> arr[i];
		for(i = n*4-4; i < n*4; i ++)
			ss.insert(arr[i]);
		cin >> n;
		for(i = 0; i < 16; i ++)
			cin >> arr[i];
		for(i = n*4-4; i < n*4; i ++)
		{
			if(ss.count(arr[i]) > 0)
				result.insert(arr[i]);
		}
		cout << "Case #"<< t <<": ";
		if(result.empty())
			cout << "Volunteer cheated!";
		else if(result.size() > 1)
			cout << "Bad magician!";
		else
		{
			set<int>::iterator iter = result.begin();
			for(;iter != result.end(); iter++)
				cout << *iter;
		}
		cout << endl;
	}
	return 0;
}