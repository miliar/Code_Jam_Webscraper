#if 1
#pragma comment(linker, "/STACK:66777216")
#include <math.h>
#include <iostream>
#include <deque>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <string>
#include <ctime>
#include <vector>
#include <iomanip>
using namespace std;
typedef long double LD; 
typedef long long LL; 

#define PROBLEM "D-large"
void solve()
{
	int n,sc1=0,sc2=0;
	double w;
	deque<double> a,b;
	scanf("%d",&n);
	for(int i=0; i<n; i++)
	{
		cin>>w;
		a.push_back(w);
	}
	for(int i=0; i<n; i++)
	{
		cin>>w;
		b.push_back(w);
	}
	sort(a.begin(),a.end());
	sort(b.begin(),b.end());
	deque<double> c(a),d(b);

	while(a.size())
	{
		if(a.back()>b.back())
		{
			sc1++;
			a.pop_back();
		}
		else
			a.pop_front();
		b.pop_back();
	}
	while(c.size())
	{
		if(c.back()>d.back())
		{	
			sc2++;
			d.pop_front();
		}
		else
			d.pop_back();
		c.pop_back();
	}
	cout<<sc1<<" "<<sc2<<endl;
}
int main()
{
    freopen(PROBLEM ".in","r",stdin); freopen(PROBLEM ".out","w",stdout);
    //freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
    time_t START = clock(); 
    
	int t;
	cin>>t;
	cout<<fixed<<setprecision(10);
	cout.sync_with_stdio();
	for(int i=1; i<=t; i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
	}

    time_t FINISH = clock(); 
    cerr << "Time = " << double(FINISH - START) / CLOCKS_PER_SEC << endl;
    return 0;
}
#endif