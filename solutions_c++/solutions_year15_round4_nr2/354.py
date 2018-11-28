/*

*/
 
//#pragma comment(linker, "/STACK:16777216")
#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>
#include <memory.h>
#include <ctime> 
 
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
 
#define eps 1e-9
//#define M_PI 3.141592653589793
#define bs 1000000007
#define bsize 256

using namespace std;

int get(double val)
{
	val*=10000;
	val+=0.5;
	return val;
}

int tests,ts,n,rate[1<<10],temp[1<<20];
int needV,needT;

int main(){
//freopen("newlines.in","r",stdin);
//freopen("newlines.out","w",stdout);
freopen("F:/B-small-attempt1.in","r",stdin);
freopen("F:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);
//cin.tie(0);

cin>>tests;
for (;tests;--tests)
{
	++ts;
	cin>>n;
	double val;
	cin>>val;
	needV=get(val);
	cin>>val;
	needT=get(val);
	
	for (int i=1;i<=n;i++)
	{
		double val;
		cin>>val;
		rate[i]=get(val);
		cin>>val;
		temp[i]=get(val);
	}
	
	if (n==2)
	 swap(temp[1],temp[2]),
	 swap(rate[1],rate[2]);
	 
	cout<<"Case #"<<ts<<": ";
	
	if (n==2&&temp[1]==temp[2])
	{
		int memo=rate[1];
		rate[1]+=rate[2];
		rate[2]+=memo;
	}
	
	if (n==2&&needT==temp[2])
	{
		swap(temp[2],temp[1]);
		swap(rate[2],rate[1]);
	}
	
	if (n==1||n==2&&needT==temp[1])
	{
		cout.precision(10);
		if (needT!=temp[1])
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else cout<<fixed<<needV*1.0/rate[1]<<endl;
	}
	else
	{
		cout.precision(10);
		if (needT<min(temp[1],temp[2])||needT>max(temp[1],temp[2]))
		cout<<"IMPOSSIBLE"<<endl;
		else
		{
			double dist1=fabs(needT-temp[1]);
			double dist2=fabs(needT-temp[2]);
			double val1=needV/(dist1+dist2)*dist2;
			double val2=needV/(dist1+dist2)*dist1;
			double res=max(val1/rate[1],val2/rate[2]);
			cout<<fixed<<res<<endl;
		}
	}
}

//cin.get();cin.get();
return 0;}
