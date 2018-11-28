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
	int t;cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		int x,r,c;cin>>x>>r>>c;
		string ret="RICHARD";
		switch(x)
		{
			case 1: ret="GABRIEL";break;
			case 2: if(c%2==0 || r%2==0) ret="GABRIEL";break;
			case 3: if(r*c%3==0 && r*c!=3)  ret="GABRIEL";break;
			case 4: if(r*c==12 || r*c==16) ret="GABRIEL";break;
		}
		printf("Case #%d: %s\n",tc,ret.c_str());
	}
	return 0;
}