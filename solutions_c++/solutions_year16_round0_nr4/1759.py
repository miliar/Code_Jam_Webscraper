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
int main()
{
	int t,i,j,k,cs,css,c,s;
	ll t1,t2,t3;
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cin>>k>>c>>s;
		t1=1;
		for(i=1;i<=c-1;i++)t1*=k;
		cout<<"Case #"<<cs<<": ";
		t2=1;
		for(i=1;i<=k;i++)
		{
			cout<<t2<<" ";
			t2+=t1;
		}
		cout<<endl;
	}
	return 0;
}
