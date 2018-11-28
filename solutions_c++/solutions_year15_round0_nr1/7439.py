#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<string>
#include<fstream>
#include<map>

#define MAX 7
#define identity 0
#define ll long long
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define DBUG(x) cout<<x<<endl;
#define pcc pair<char,char>
#define pii pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define mp(a,b) make_pair(a,b)

using namespace std;

int main()
{
	fstream datafile1,datafile2;
	datafile1.open("a.txt",ios::in);
	datafile2.open("final.txt",ios::out);
	
	int t;
	datafile1>>t;
	for(int j=1;j<=t;j++)
	{
		int s;
		datafile1>>s;
		
		string x;
		datafile1>>x;
		
		ll curr=x[0]-48,rq=0,a;
		
		for(int i=1;i<=s;i++)
		{
			a=0;
			
			if(curr<i) a=i-curr;
			
			curr+=a+x[i]-48;
			rq+=a;
		}
		
		datafile2<<"Case #"<<j<<": "<<rq<<endl;
	}
}
