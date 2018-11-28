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

int tests,n;
string st;
vector<int> v[25];
int ans;
int S1[1<<20],S2[1<<20];
set<string>::iterator it;
int ts;
map<string, int> mapp;
set<string> W;
int M1[1<<20],M2[1<<20];

int get_id(string st)
{
	if (W.find(st)!=W.end()) return mapp[st];
	W.insert(st);
	mapp[st]=W.size();
	return mapp[st];	
}

int main(){
//freopen("newlines.in","r",stdin);
//freopen("newlines.out","w",stdout);
freopen("F:/in.txt","r",stdin);
freopen("F:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);
//cin.tie(0);

cin>>tests;
for (;tests;--tests)
{
	cin>>n;
	++ts;
	getline(cin,st);
	
	W.clear();
	mapp.clear();
	
	for (int i=1;i<=n;i++)
	{
		getline(cin,st);
		stringstream S(st);
		v[i-1].clear();
		string s;
		while (S>>s)
		{
			v[i-1].push_back(get_id(s));
		}
	}
	/*for (int i=0;i<n;i++)
	 cout<<v[i].size()<<endl;
	 */
	 int M=W.size();
	for (int i=0;i<=M;i++)
	 M1[i]=M2[i]=0;
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<v[i].size();j++)
		{
			M1[v[i][j]]|=(1<<i);
		}
	}
	 
	ans=1e9;
	
	for (int mask=0;mask<(1<<n);mask++)
	{
		int cnt=0;
		if (mask%2==0)continue;
		if (mask/2%2==1)continue;
		int mask2=(1<<n)-mask-1;
		for (int i=1;i<=M;i++)
		{
			if (M1[i]&mask)
			 if (M1[i]&mask2)
			  ++cnt;
			if (cnt>=ans)break;
		}
		
		ans=min(ans,cnt);
	}
	
	cout<<"Case #"<<ts<<": "<<ans<<endl;
}

//cin.get();cin.get();
return 0;}
