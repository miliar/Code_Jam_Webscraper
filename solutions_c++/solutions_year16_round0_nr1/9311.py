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
ofstream fs("SalidaA.txt");
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    long long t;
    long long n;
    long long i,a,sol,d,m,g;
    cin>>t;
    for(long long cs=0;cs<t;cs++)
	{
	    cin>>n;
	    if(n==0)
		{
		    fs<<"Case #"<<cs+1<<": INSOMNIA\n";
		    continue;
		}
	    i=1;
	    sol=0;
	    while(true)
		{
		    a=n*i;
		    g=a;
		    i++;
		    //cout<<"a: "<<a<<"\n";
		    while(true)
			{
			    s.insert(a%10);
			    a/=10;
			    if(a==0)break;
			}
		    //cout<<s.size()<<"\n";
		    sol++;
		    if(s.size()==10)
			{
			    break;
			}
		}
	    fs<<"Case #"<<cs+1<<": "<<g<<"\n";
	    s.clear();
	}
}
