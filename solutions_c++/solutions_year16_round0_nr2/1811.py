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
	int t,i,j,k,cs,css;
	char s[200];
	cin>>css;
	for(cs=1;cs<=css;cs++)
	{
		cin>>s;
		k=1;
		for(i=1;s[i]!='\0';i++)
		{
			if(s[i]!=s[i-1])k++;
		}
		cout<<"Case #"<<cs<<": ";
		if(s[0]=='+')
		{
			if(k%2==1)k--;
			cout<<k<<endl;
		}
		else
		{
			if(k%2==0)k--;
			cout<<k<<endl;
		}
	}
	return 0;
}
