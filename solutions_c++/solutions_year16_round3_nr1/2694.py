#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
vector< pair<int,int> >v;
bool cmp(const pair<int,int>a,const pair<int,int>b)
{
	return a.first>b.first;
}
string mc(int a)
{
	char temp=(char)(a+'A');
     string h="";
     h+=temp;
     return h;
}
int main() {
int n;
int t;
//freopen("input.txt","r",stdin);
cin>>t;
for(int q=1;q<=t;q++)
{
	cin>>n;
	v.clear();
	int a[n+1];
	for(int i=0;i<n;i++)
			{
				cin>>a[i];
			v.pb(mp(a[i],i));
			}
			sort(v.begin(),v.end(),cmp);
			int final=1;
           cout<<"Case #"<<q<<": ";
	while(final<n)
		{   while(v[final-1].first!=v[final].first)
			{
				for(int i=0;i<final;i++)
				{
		        cout<<mc(v[i].second)<<" ";
		        v[i].first--;
				}
			}
			final++;
		}
		for(int i=0;i<n-2;i++)
		while(v[i].first--)
		cout<<mc(v[i].second)<<" ";
		while(v[n-1].first--)
		cout<<mc(v[n-2].second)<<mc(v[n-1].second)<<" ";
		cout<<endl;
	}
}