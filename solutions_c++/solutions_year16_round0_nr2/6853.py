#include<bits/stdc++.h>
#define mod 1000000007
#define ll long long int
#define v1 vector<int>
#define s1 set<int>
#define l1 list<int>
#define m1 map<int,int>
#define p1 pair<int,int>
#define mem(a) memset(a,0,sizeof a)
using namespace std;
ll arr[10000000];
int main()
{
	string s;
	int t,i,j,k=1,l,a,c,ss,rr;
	//freopen("2.txt","r",stdin);
	//freopen("out2.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		cin>>s;
		a=0;
		l=s.length();
		if(l==1)
		{
			if(s[0]=='-')
			cout<<"Case #"<<k++<<": "<<1<<endl;
			else
			cout<<"Case #"<<k++<<": "<<0<<endl;
			continue;
		}
		i=0;
		if(s[i]=='+')
		{
			while(i<l && s[i++]=='+');
			if(i==l && s[i-1]=='+')
			{
				cout<<"Case #"<<k++<<": "<<0<<endl;
				continue;
			}
			else
			{
				a++;
				i--;
			}
		}
		ss=0;rr=0;
		for(i;i<l;i++)
		{
			if(s[i]=='+')
			{
				if(ss==0)
				a++;
				ss=1;
			}
			else
			{
				
				if(rr==1)
				{
					if(ss==1)
					a++;
					ss=0;
				}
				if(rr==0)
				{
					rr=1;
				}
			}
		}
		if(s[i-1]=='-')
		a++;
		cout<<"Case #"<<k++<<": "<<a<<endl;
	}
 	return 0;
}

