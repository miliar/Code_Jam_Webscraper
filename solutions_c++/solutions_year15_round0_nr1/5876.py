#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

#define OO (int) 1e9

using namespace std;

int gcd(int u, int v) {return (v != 0)?gcd(v, u%v):u;}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int tc;
	cin>>tc;
	for(int j=1;j<=tc;j++)
	{
		string str;
		int n;
		cin>>n>>str;
		int cur=str[0]-'0';
		int res=0;
		for(int i=1;i<=n;i++)
		{
			if(cur < i )
			{
				res+=(i-cur);
				cur+=(i-cur);
			}
			cur+=(str[i]-'0');
		}
		cout<<"Case #"<<j<<": "<<res<<endl;
	}

}

