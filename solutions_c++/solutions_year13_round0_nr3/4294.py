//
//  main.cpp
//
//  Created by Prateek Sachdev 
//  Copyright (c) 2013 Prateek Sachdev. All rights reserved.
//
#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <cstring>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <iostream>

using namespace std;

typedef vector<int > vd;
#define ll long long
#define sd(n) scanf("%d",&n)
#define sc(n) scanf("%c",&n)
#define sf(n) scanf("%f",&n)
#define ss(n) scanf("%s",n)
#define pd(n) printf("%d\n",n)
#define pb push_back

#define SIEVE(a) ({int b=ceil(sqrt(a));vd d(a,0);vd e;int f=2;e.pb(2);e.pb(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.pb(c);}}e;})
template<class T> inline vector<pair<T,int> > FACTORISE(T n){vector<pair<T,int> >R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline T TOTIENT(T n) {vector<pair<T,int> > R=FACTORISE(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}

vector<ll > final_list;

string int_tostr(ll num)
{
	string temp,strval="";
	while( num!=0 ){
		temp = num%10 + '0';
		strval = temp + strval;
		num /= 10;
	}
	return strval;
}

bool checkpall(string s)
{
	ll i;
	ll len;
	len=s.size();
	for(i=0;i<=len-i-1;i++)
	{
		if(s[i]!=s[len-i-1])
			return false;
	}
	return true;
}

void make_list()
{
	
	ll i;
	final_list.clear();
	for( i=1;i*i<=1e14;i++ ){
		if( checkpall(int_tostr(i)) && checkpall(int_tostr(i*i)) )
			final_list.push_back(i*i);
	}
	return ;

}
ll findall( ll num)
{
	ll i;
	for(i=0;i<final_list.size();i++)
	{
		if(final_list[i]>=num)
			break;
	}
	return i;
}
int main()
{
	

	make_list();
	
	ll n1,n2;
	long long int t;
	scanf("%lld",&t);
	long long int count=0;
	ll ans;
	while(t--)
	{
		count++;
	scanf("%lld%lld",&n1,&n2);
	ans=findall(n2+1)-findall(n1);
	printf("Case #%lld: %lld\n",count,ans );
}

	return 0;
}



