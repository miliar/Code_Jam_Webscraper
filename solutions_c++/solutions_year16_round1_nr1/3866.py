#include<iostream>
#include<vector>
#include<stdio.h>
#include<algorithm>
#include<set>
#include<math.h>
#include<string.h>
#include<map>
#include<deque>
#define all(c) c.begin(), c.end()
#define tr(container, it) for(typeof(container.begin())it=container.begin();it!=container.end();it++)
#define sz(a) int((a).size()) 
#define pb push_back
#define present(c,x) ((c).find(x)!=(c).end()) 
#define cpresent(c,x) (find(all(c),x)!=(c).end())
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef set<int> si;
typedef long long int lli;

int main()
{
	int t,n,m,i,j,k,flag=0,cnt=0;
	char str[1001];
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		cin>>str;
		deque<char> d;
		int l=strlen(str);
		int max=int(str[0]);
		d.pb(str[0]);
		for(i=1;i<l;i++)
		{
			if(int(str[i])>=max)
			{
				d.push_front(str[i]);
				max=str[i];
			}
			else
				d.pb(str[i]);
		}
		cout<<"CASE #"<<j<<": ";
		tr(d,it)
			cout<<*it;
		cout<<endl;
	}
}

