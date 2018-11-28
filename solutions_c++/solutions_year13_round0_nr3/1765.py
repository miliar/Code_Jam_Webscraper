#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <math.h>

using namespace std;
typedef unsigned long long llu;


string LLuToStr(llu a)
{
	std::stringstream ss;
    ss<<a;
    std::string str;
    ss>>str;
	return str;
}

bool IsP(llu a)
{
	string s = LLuToStr(a);
	for (int i = 0; i < s.length()/2; ++i)
	{
		if (s[i] != s[s.length() - i - 1])
			return false;
	}
	return true;
}


int main()
{

	int maxim = 10000001;
	vector<llu> arr(maxim);
	for (llu i = 1; i < maxim; ++i)
	{
		arr[i] = arr[i-1];
		if (IsP(i))
		{
			if (IsP(i * i))
			{
				++arr[i];
			}
		}
		if (i % 1000000 == 0)
			cout<<i<<endl;
	}
	int T;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>T;
	for (int i = 0; i < T; ++i)
	{
		llu a, b;
		cin>>a>>b;
		a = ceil(sqrt((double)a));
		b = sqrt((double)b);
		cout<<"Case #"<< i + 1<<": "<<(arr[b] - arr[a-1])<<endl;


		
	}



	return 0;
}