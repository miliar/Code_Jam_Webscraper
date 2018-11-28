#include<iostream>
#include<vector>
#include<algorithm>
#include<string.h>
#include<cstdio>
#include<math.h>
#include<cstdlib>
#include<map>
#include<utility>
#include<stack>
#include<fstream>

using namespace std;
#define ll long long int
vector <ll> v;
vector <ll> v1;
vector <ll> v2;
const int inf=100000005;

#define cincout ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define me1(a,i) memset(a,i,sizeof(a))
#define me2(a,i,n,m) memset(a,i,n*m*sizeof(a[0][0]))
#define mp make_pair
#define pb push_back
#define sortv(v) sort(v.begin(),v.end())
#define printv(n,v) for(int i=0;i<n;i++)  {cout<<v[i]<<" ";}

int main()
	{
	cincout;
	ifstream in;
	in.open("test.txt");
	ofstream out;
	out.open("output");
	int t;
	in>>t;
	for(int j=1;j<=t;j++)
		{
		string s,t="";
		in>>s;
		t+=s[0];
		for(int i=1;i<s.length();i++)
			{
			if(s[i]==s[i-1])
				continue;
			else
				t+=s[i];
			}
		if(t[t.length()-1]=='+')
			out<<"Case #"<<j<<": "<<t.length()-1<<endl;
		else
			out<<"Case #"<<j<<": "<<t.length()<<endl;		}
  	return 0;
  	}