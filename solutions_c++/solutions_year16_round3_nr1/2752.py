#include<bits/stdc++.h>
using namespace std;
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define INF 99999999
#define N 100005
#define ll long long
#define llu unsigned long long
#define MOD 1000000007
#define gcd __gcd
#define fill(A,v) memset(A,v,sizeof(A))
set< pair<int,char> >s;
set< pair<int,char> >::iterator it;
char str[N];
int main()
{
     freopen("inp.in", "r", stdin);
    freopen("out2.txt", "w", stdout);
	int t,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		int n,i,len=0,val,val1,a,val2;
		s.clear();
		char c,c1,c2;
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>a;
			c=(char)(i+65);
			s.insert(mp(-a,c));
		}
		while(!s.empty())
		{
           if(s.size()==2)
		   {
		   	 it=s.begin();
		   	 val1=it->ff;
		   	 c1=it->ss;
		   	 it++;
		     val2=it->ff;
		     c2=it->ss;
		     if(val1==val2)
		     {
		     	while(val1++)
		     	{
		     	 str[len++]=c1;
		     	 str[len++]=c2;
		     	 str[len++]=' ';
		     	}
		     	break;
		     }
		   }
		   it=s.begin();
		   val=it->ff;
		   c=it->ss;
		   s.erase(it);
		   str[len++]=c;
		   val++;
		   if(val!=0)
		     s.insert(mp(val,c));
		   str[len++]=' ';
		}
		cout<<"Case #"<<k<<": ";
		for(i=0;i<len;i++)
		  cout<<str[i];
		 cout<<"\n";
	}
	return 0;
}
