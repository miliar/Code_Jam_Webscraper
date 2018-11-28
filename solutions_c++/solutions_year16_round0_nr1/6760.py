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
	s1 s;
	int t,i,j,k,l,n;
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	cin>>t;
	int ss=1;
	while(t--)
	{
		cin>>n;
		int c=n,x=0,r=1;
		while(x<101)
		{
			k=c*r;
			ll tt=k;
			while(k)
			{
				int p=k%10;
				s.insert(p);
				k/=10;
			}
			if(s.size()==10)
			{
				cout<<"Case #"<<ss<<": ";
				cout<<tt<<endl;
				break;
				
			}
			
			x++;
			r++;
		}
		if(x==101 && s.size()!=10)
		{
			cout<<"Case #"<<ss<<": INSOMNIA"<<endl;
		}
		s.clear();
		ss++;
	}
 	return 0;
}

