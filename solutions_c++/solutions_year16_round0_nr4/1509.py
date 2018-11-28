#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

const int MAXN=2147483647;

int i,j,k,c,s,tcase,xcase;


int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	cin>>tcase;
	xcase=0;
	while (xcase<tcase)
	{
		xcase++;
		cout<<"Case #"<<xcase<<":";
		cin>>k>>c>>s;
		for (i=1;i<=s;i++)
		{
			cout<<" "<<i;
		}
		cout<<endl;
	}
	return 0;
}

