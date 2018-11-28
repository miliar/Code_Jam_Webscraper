#include <vector>
#include <list>
#include <map>
#include <set>
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
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out3.txt", "w", stdout);
	int t,tt;
	string s,ret="";
	cin>>t;
	tt=t;
	char c='A';
	while(tt--)
	{
        cin>>s;
        ret="";
		for(int q=0;s[q]!='\0';q++)
		{
			if(s[q]>c)
				c=s[q];
		}
		ret+=s[0];
		for(int q=1;s[q]!='\0';q++)
		{
			if(s[q]>=ret[0])
				ret=s[q]+ret;
			else
				ret=ret+s[q];
		}
		cout<<"Case #"<<t-tt<<": "<<ret<<endl;
	}
	return 0;
}
