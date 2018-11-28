#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <queue>
#include <functional>
#include <list>
#include <set>
#include <sstream>
#define ll long long

using namespace std;

int main()
{
	ios::sync_with_stdio(false);

	//while(cin>>n)

	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		string s;
		cin>>s;
		int ans=0;
		for(int i=0;i<s.size()-1;i++)
			if(s[i]!=s[i+1])ans++;
		if(s[s.size()-1]=='-')ans++;
		cout<<"Case #"<<cas<<": "<<ans<<endl;
		//cout<<"Case "<<cas<<": ";
	}

	return 0;
}
