		/*masterwayne*/
#include<bits/stdc++.h>
using namespace std;
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf(x) printf("%d",x)
#define pf2(x,y) printf("%d %d",x,y)
#define pf3(x,y,z) printf("%d %d %d",x,y,z)
#define fr(i,x,n) for(int i=x;i<n;i++)
#define fre(i,x,n) for(int i=x;i<=n;i++)
#define fb(i,x,n) for(int i=n-1;i>=x;i--)
#define fbe(i,x,n) for(int i=n;i>=x;i--)
#define pfn() printf("\n")
#define pfs() printf(" ")
#define pb push_back
int main()
{
	freopen("inpA2.in","r",stdin);
	freopen("outA2.txt","w",stdout);
	int t;
	sc(t);
	for(int i=1;i<=t;i++)
	{
		string s;
		cin>>s;
		//string s1;
		char curr=s[0];
		list<char> l;
		l.push_front(s[0]);
		for(int i=1;s[i]!='\0';i++)
		{
			int x=curr-65;
			int y=s[i]-65;
			if(y<x)
				l.push_back(s[i]);
			else
			{
				l.push_front(s[i]);
				curr=s[i];
			}
		}
		cout<<"Case #"<<i<<": ";
		list<char>::iterator it;
		for(it=l.begin();it!=l.end();it++)
			cout<< *it;
		cout<<endl;
	}
	return 0;
}