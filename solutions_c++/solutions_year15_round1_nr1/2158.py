#include <iostream>
#include <vector>
using namespace std;

long long int method1(vector<int> vec)
{
	int ret = 0;
	for(int i=1;i<vec.size();i++)
	{
		if(vec[i] < vec[i-1])
		{
			ret += vec[i-1] - vec[i];
		}
	}
	return ret;
}

long long int method2(vector<int> vec)
{
	int ret=0,max=0;
	for(int i=1;i<vec.size(); i++)
	{
		if(max<(vec[i-1]-vec[i]))
            max=(vec[i-1]-vec[i]);
	}
	for(int i=0;i<vec.size()-1;i++)
	{
		if(max > vec[i])
		{
			ret += vec[i];
		}
		else
		{
			ret += max;
		}
	}
	return ret;
}

int main()
{
	int test;
	cin >> test;
	for(int x = 1; x<=test;x++)
	{
		int n;
		long long int z, y;
		vector<int> vec;
		cin >> n;
		for(int j=0;j<n;j++)
		{
			cin >> z;
			vec.push_back(z);
		}
		y = method1(vec);
		z = method2(vec);
		cout << "Case #" << x << ": " << y << " " << z << endl;
	}
	return 0;
}