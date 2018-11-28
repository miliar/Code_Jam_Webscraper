#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
using namespace std;
int main()
{
	int a,b,k,tc,ans=0;
	cin>>tc;
	for(int t=0;t<tc;t++)
	{
		int count=0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				ans=i&j;
				if(ans<=k-1)
					count++;
			}
		}
		cout<<"Case #"<<(t+1)<<": "<<count<<endl;



	}
	return 0;
}

