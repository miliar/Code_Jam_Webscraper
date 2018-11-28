#include<iostream>
#include<stack>
#include<map>
#include<utility>
#include<stdlib.h>
#include<math.h>
#include<stdio.h>
#include<map>
#include<fstream>
#include<algorithm>
#include<bitset>
#include<vector>
#include<cstring>
using namespace std;
#define mp make_pair
#define f first
#define pb push_back
#define s second
#define ull unsigned long long
#define ll long long
#define MOD 1000000007
int x[10000002]={0};
bool check(ll a)
{
    string x="";
    while(a)
    {
	x+=(a%10+'0');
	a/=10;
    }
    for(int i=0;i<x.size()/2;i++)
    {
	if(x[i]!=x[x.size()-1-i])
	    return 0;
    }
    return 1;
}
void init()
{
    for(ll i=1;i<10000002;i++)
    {
	if(check(i) && check(i*i))
	{
	    x[i]=x[i-1]+1;
	}
	else
	    x[i]=x[i-1];
    }
}
int main()
{
    int t;
    cin>>t;
    init();
    for(int tt=1;tt<=t;tt++)
    {
	ll a,b;
	cin>>a>>b;
	cout<<"Case #"<<tt<<": "<<(x[(int)floor(sqrt(b))]-x[(int)ceil(sqrt(a))-1])<<endl;
    }
    return 0;
}
