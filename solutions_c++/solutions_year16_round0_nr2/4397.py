#include <bits/stdc++.h>
using namespace std;

#define FOR(i,j,n) for(i=j;i<n;i++)
#define si(i) scanf("%d",&i)
#define sli(i) scanf("%ld",&i)
#define slli(i) scanf("%lld",&i)
#define sc(i) scanf("%c",&i)
#define ss(i) scanf("%s",i);

#define pi(i) printf("%d\n",i)
#define pli(i) printf("%ld\n",i)
#define plli(i) printf("%lld\n",i)
#define pc(i) printf("%c\n",i)
#define ps(i) printf("%s\n",i);

typedef long long int lli;
int find_p(string s, int i)
{
	for(int j=i-1;j>=0;j--)
	{
		if(s[j]=='+')
		{
			return j;
		}
	}
}

void do_it(string& s, int i)
{
	string s1(s,0,i+1);
	int len=s.size();
	string s2(s,i+1,len-i-1);
	reverse(s1.begin(),s1.end());
	int l1=s1.size(),kk;
	FOR(kk,0,l1)
	{
		if(s1[kk]=='+')
		{
			s1[kk]='-';
		}
		else
		{
			s1[kk]='+';
		}
	}
	s1=s1+s2;
	s=s1;
}
void solve()
{
	//print the answer and nothing less or more. 
	string s;
	cin>>s;
	string s2=s;
	int len=s.size();
	int i=len-1,ans=0;
	while(i>=0)
	{
		if(s[i]=='-')
		{
			if(s[0]=='-')
			{
				do_it(s,i);
				ans++;
			}
			else
			{
				int j=find_p(s,i);
				do_it(s,j);
				ans++;
				do_it(s,i);
				ans++;
			}
		}
		i--;
	}

	printf("%d",ans);
		
}

int main()
{
	lli i,t;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl; 	
	}
	   
    return 0;
}