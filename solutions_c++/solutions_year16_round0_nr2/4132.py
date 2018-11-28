#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;


int main(int argc, char *argv[]) {
	freopen("out", "w", stdout);

	int t;
	cin>>t;
	
	for(int Case=1;Case<=t;Case++)
	{
		string s , now;
		cin>>s;
		
		for(int i=0,j;i<s.size();i=j) 
		{
			for(j=i;j<s.size() && s[j] == s[i]; j++);
			now += s[i];
		}
		
		cout<<"Case #"<<Case<<": "<<now.size() - (now[now.size()-1]=='+')<<endl;
	}
	
	
	return 0;
}
