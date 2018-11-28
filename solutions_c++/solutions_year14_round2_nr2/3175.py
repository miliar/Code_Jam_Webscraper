#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define rep(i,n) for(int i=0;i<(n);i++)
//#define ull unsigned long long
//#define lint long long
#define MX 10000001
int main()
{
	int i,j,k,l,n,m,t,a,b;
	cin>>t;
	int c=1;
	while(t--)
	{
	    cin>>a>>b>>k;
	    int ct=0;
	    for(int i=0;i<a;i++)
	    {
	        for(int j=0;j<b;j++)
	        {
	            if((i&j)<k)
	            ct++;
            }
        }
        cout<<"Case #"<<c<<": "<<ct<<endl;
        c++;
	}
	return 0;
}


















