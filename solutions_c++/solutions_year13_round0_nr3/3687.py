#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <sstream>

using namespace std;

bool check(int d){
	stringstream ss;
	ss<<d;
	string a = ss.str();
	
	for (int i = 0; i < a.size()/2 + 2; ++i)
	{
		if (a[i] != a[a.size()-i-1])
		{
			return false;
		}
	}
	return true;
}

int main(int argc, char const *argv[])
{
	int T;
	cin>>T;

	for (int t = 0; t < T; ++t)
	{
		int A,B;
		cin>>A>>B;

		int count = 0;
		for (int i = 0; i < 10; ++i)
		{
			int d = i * i;
			if(d >= A && d <=B)
			{
				if(check(d))
					count++;
			}

			if(i != 0)
			{
				int di = i * 10 + i;
				int dd = di * di;
				if(dd >= A && dd <=B)
				{
					if(check(dd))
						count++;
				}
			}
			
		}

		cout<<"Case #"<<t+1<<": "<<count<<endl;
	}
	return 0;
}