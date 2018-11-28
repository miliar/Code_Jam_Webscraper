#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <stdio.h>
#include <string.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin>>T;
	for (int t = 0; t < T; ++t)
	{
		string S,Out="";
		cin>>S;
		Out+=S[0];
		for (int i = 1; i < S.size(); ++i)
		{
			if(S[i]>=Out[0])
				Out=string(1,S[i])+Out;
			else
				Out+=S[i];
		}
		cout<<"Case #"<<t+1<<": "<<Out<<endl;

	}
	return 0;
}