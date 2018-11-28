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
#include <string>
#include <cstring>
using namespace std;
#define MAX 10000000
#define LL long long int
int palin(LL n)
{
	int buf[50];
	LL i;
	int r,pos=0;
	while(n) {
		r=n%10;
		buf[pos++]=r;
		n/=10;
	}
	int l=pos;
	for(i=0;i<l/2;i++)
	{
		if(buf[i]!=buf[l-i-1])
		return 0;
	}
	return 1;
}
int main()
{
	LL i,a,b,x;
	int t,k;
	vector<LL> v;
	vector<LL> sv;
	vector<LL>::iterator low,up;
	
	
	
	for(i=1;i<=MAX;i++)
	{
		if(palin(i))
		v.push_back(i);
	}
	
	for(i=0;i<v.size();i++)
	{
		x=v[i]*v[i];
		if(palin(x))
		sv.push_back(x);
	}
	sort(sv.begin(),sv.end());
	
	cin>>t;
	for(k=1;k<=t;k++)
	{
		x=0;
		cin>>a>>b;
		low=lower_bound (sv.begin(), sv.end(),a);
		up =lower_bound (sv.begin(), sv.end(),b);
		if(*low==a && *up==b)
		x=1;
		if(*low!=a && *up==b)
		x=1;
		
		cout<<"Case #"<<k<<": "<<(up - sv.begin())-(low- sv.begin())+x<<endl;
	}
	return 0;
}
