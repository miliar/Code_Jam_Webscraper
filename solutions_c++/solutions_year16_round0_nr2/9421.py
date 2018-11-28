#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<math.h>
#include<set>
#include<stdio.h>
#include<queue>
#include <bits/stdc++.h>
using namespace std;
vector<int> v;
set<long long> s;
ofstream fs("SalidaB.txt");
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    string s,a="";
    int ts,ta,sol;
    cin>>t;
    for(int cs=1;cs<=t;cs++)
	{
	    cin>>s;
	    sol=0;
	    ts=s.length();
	    a="";
	    a=a+s[0];
	    for(int i=1;i<ts;i++)
		{
		    if(s[i]!=s[i-1])
			{
			    a=a+s[i];
			}
		}
	    ta=a.length();
	    //cout<<a<<"\n";
	    if(a[ta-1]=='+')
		{
		    sol=ta-1;
		}
	    else
		{
		    sol=ta;
		}
	    fs<<"Case #"<<cs<<": "<<sol<<"\n";
	}
    
}
