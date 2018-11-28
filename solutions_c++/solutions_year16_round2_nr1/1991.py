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
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out1.txt", "w", stdout);
	int t,tt;
	cin>>t;
	tt=t;
	while(tt--)
	{
	    string s;
        int ar[26]={0};
        cin>>s;
        vector<int>ret;
        for(int q=0;s[q]<='Z' && s[q]>='A'; q++)
            ar[s[q]-'A']++;
        while(ar['Z'-'A'])
        {
            ret.push_back(0);
            ar['Z'-'A']--;ar['E'-'A']--;ar['R'-'A']--;ar['O'-'A']--;
        }
        while(ar['G'-'A'])
        {
            ret.push_back(8);
            ar['E'-'A']--;ar['I'-'A']--;ar['G'-'A']--;ar['H'-'A']--;ar['T'-'A']--;
        }
        while(ar['W'-'A'])
        {
            ret.push_back(2);
            ar['T'-'A']--;ar['W'-'A']--;ar['O'-'A']--;
        }
        while(ar['X'-'A'])
        {
            ret.push_back(6);
            ar['S'-'A']--;ar['I'-'A']--;ar['X'-'A']--;
        }
        while(ar['S'-'A'])
        {
            ret.push_back(7);
            ar['S'-'A']--;ar['E'-'A']--;ar['V'-'A']--;ar['E'-'A']--;ar['N'-'A']--;
        }
        while(ar['V'-'A'])
        {
            ret.push_back(5);
            ar['F'-'A']--;ar['I'-'A']--;ar['V'-'A']--;ar['E'-'A']--;
        }
        while(ar['F'-'A'])
        {
            ret.push_back(4);
            ar['F'-'A']--;ar['O'-'A']--;ar['U'-'A']--;ar['R'-'A']--;
        }
        while(ar['O'-'A'])
        {
            ret.push_back(1);
            ar['O'-'A']--;ar['N'-'A']--;ar['E'-'A']--;
        }
        while(ar['N'-'A'])
        {
            ret.push_back(9);
            ar['N'-'A']--;ar['I'-'A']--;ar['N'-'A']--;ar['E'-'A']--;
        }
        while(ar['H'-'A'])
        {
            ret.push_back(3);
            ar['T'-'A']--;ar['H'-'A']--;ar['E'-'A']--;ar['R'-'A']--;ar['E'-'A']--;
        }
        sort(ret.begin(),ret.end());
		cout<<"Case #"<<t-tt<<": ";//<<ret<<endl;
		for(int qq=0;qq<ret.size();qq++)
            cout<<ret[qq];
        cout<<endl;
	}
	return 0;
}
