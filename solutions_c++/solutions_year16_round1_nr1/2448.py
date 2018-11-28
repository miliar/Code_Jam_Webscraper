#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<utility>
#define PB push_back
#define pii pair<int,int>
#define MP make_pair
#define sz size()
#define fi first
#define se second
using namespace std;
typedef long long ll;
string s,r;
int a[2000];
int t1,t2;
void fun(int e,char c)
{
	int i,j,k;
	for(i=e,k=e;i>=0;i--)
	{
		if(s[i]==c)
		{
			r[t1]=c;
			t1++;
			for(j=k;j>i;j--,t2--)r[t2]=s[j];
			k=i-1;
		}
	}
	if(c!='A')fun(k,c-1);
}
int main()
{
	int t,i,j,k,cs,css;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cin>>s;
		r=s;
		t1=0,t2=s.sz-1;
		fun(s.sz-1,'Z');
		cout<<"Case #"<<cs<<": "<<r<<endl;
	}
	return 0;
}
