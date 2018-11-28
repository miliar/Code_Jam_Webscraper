//============================================================================
// Name        : CodeJam1C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
#include <limits>
#include <algorithm>
#include <set>

using namespace std;

typedef long long ll;

class A
{
public:
	void solve();
private:
	ll calc(string str, int n);
};

void A::solve()
{
	ifstream ifs("input");
	ofstream ofs("output");

	if(!ifs.is_open())
		cout<<"error while opening";

	int T;
	ifs>>T;
	for(int t=0; t<T; ++t)
	{
		string inStr;
		ifs>>inStr;
		int n;
		ifs>>n;
		ll res=calc(inStr, n);
		ofs<<"Case #"<<t+1<<": "<<res<<endl;
	}
}

ll A::calc(string str, int n)
{
	char v[5]={'a', 'e', 'i', 'o', 'u'};
	ll res=0;

	for(int i=n; i<=str.size(); ++i)
	{
		//set<string> mSet;
		for(int cur=0; cur<=str.size()-i; ++cur)
		{
			string subS=str.substr(cur, i);
			bool isOk=false;
			int conSize=0;
			for(int j=0; j<i; ++j)
			{
				if(subS[j]!=v[0] && subS[j]!=v[1] && subS[j]!=v[2] && subS[j]!=v[3] && subS[j]!=v[4])
					conSize++;
				else
					conSize=0;

				if(conSize==n)
				{
					isOk=true;
					break;
				}
			}
			if(isOk)
				res++;
		}
		//res+=mSet.size();
	}

	return res;
}

int main() {
	A a;
	a.solve();
	cout << "done" << endl;
	return 0;
}
