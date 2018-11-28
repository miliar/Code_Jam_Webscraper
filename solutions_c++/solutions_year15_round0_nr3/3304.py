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
	map<string,string>mp;
	mp["11"]="1";
	mp["1i"]="i";
	mp["1j"]="j";
	mp["1k"]="k";
	mp["i1"]="i";
	mp["ii"]="-1";
	mp["ij"]="k";
	mp["ik"]="-j";
	mp["j1"]="j";
	mp["ji"]="-k";
	mp["jj"]="-1";
	mp["jk"]="i";
	mp["k1"]="k";
	mp["ki"]="j";
	mp["kj"]="-i";
	mp["kk"]="-1";
	repx(testcase,1,test+1)
	{
		int l,x;
		cin>>l>>x;
		string s,str;
		cin>>s;
		rep(i,x)
		{
			str +=s;
		}
		string cur;
		cur += str[0];
		bool ic=false,jc=false,kc=false;
		repx(i,1,l*x)
		{
			if(ic==false && cur=="i")
			{
				ic=true;
				cur = str[i];
				continue;
			}
			else if(ic == true && jc == false && cur == "j")
			{
				jc = true;
				cur = str[i];
				continue;
			}
			else
			{
				int neg1=1,neg2=1;
				string checkstr = cur;
				if(cur[0]=='-')
				{
					neg1 = -1;
					checkstr = cur.substr(1);
				}
				checkstr = mp[checkstr+str[i]];
				if(checkstr[0]=='-')
				{
					neg2=-1;
					checkstr = checkstr.substr(1);
				}
				if(neg1 * neg2 == -1)
				{
					cur = "-"+checkstr;
				}
				else
				{
					cur = checkstr;
				}
			}

		}
		if(cur == "k" && ic && jc)
		{
		cout <<"Case #"<<testcase<<": YES\n";
		}
		else
		{
			cout <<"Case #"<<testcase<<": NO\n";
		}

	}
	return 0;
}