#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <map>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <climits>
#include <set>
using namespace std;


int main()
{
	int t;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		int s;cin>>s;
		int needed=0;
		int prev=0;
		char ch;cin>>ch;
		prev=ch-'0';
		for(int i=1;i<=s;i++)
		{
			cin>>ch;
			ch-='0';
			if(ch!=0 && prev<i)
			{
				needed+=(i-prev);prev=i+ch;
			}
			else if(ch!=0)
				prev+=ch;
		}
		printf("Case #%d: %d\n",tc,needed );

	}
	return 0;
}