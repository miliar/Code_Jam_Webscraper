#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits.h>
#include <string.h>
 
#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)
#define pb push_back
#define full(v)  v.begin(),v.end()
#define np next_permutation
#define VI vector<int>
#define VS vector<string>
#define VC vector<char>
#define VD vector<double>
#define VF vector<float>
#define SI set<int>
#define SC set<char>
#define SS set<string>
#define MII map<int,int>
#define MSI map<string,int>
#define MIS map<int,string>
#define MIC map<int,char>
#define MCI map<char,int>
#define LL long long
using namespace std;
 
int main()
{
	int test;
	cin>>test;
	repx(testcase,1,test+1)
	{
		int n;
		cin>>n;
		int ret = 0;
		int tot = 0;
		string s;
		cin>>s;
		rep(i,n+1)
		{
			int tmp;
			tmp =  (int)(s[i]-'0');
			if(i==0)
			{
				tot+=tmp;
			}
			else
			{
				if(tot>=i)
				{
					tot+=tmp;
				}
				else
				{
					ret += (i-tot);
					tot = i + tmp; 
				}
			}
		}
		cout <<"Case #"<<testcase<<": "<<ret<<"\n";
	}
	return 0;
}