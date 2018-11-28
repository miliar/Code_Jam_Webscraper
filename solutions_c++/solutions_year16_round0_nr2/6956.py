#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <set>
#include <utility>
#include <stack>
#include <cmath>
#include <cassert>
using namespace std;

int t;
char str[111];

int main(int argc, char const *argv[])
{
	cin>>t;
	for (int tt = 0; tt < t; ++tt)
	{
		cin>>str;
		int l = strlen(str);
		int ans = (str[l-1]=='+')?0:1;
		for (int i = l-2; i >= 0; i--)
		{
			if(str[i]!=str[i+1])
			{
				ans++;
			}
		}
		cout<<"Case #"<<tt+1<<": "<<ans<<"\n";
	}
}
