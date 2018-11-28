#include <bits/stdc++.h>
using namespace std;
int n,r,p,s;
char seq[50110];
void solve(int l,int r,char c)
{
	if(l==r)
	{seq[l]=c; return;}
	char bt;
	if(c=='R') bt='S';
	else if(c=='S') bt='P';
	else if(c=='P') bt='R';
	else throw;
	int mid=(l+r)/2;
	if(c<bt)
	{
		solve(l,mid,c);
		solve(mid+1,r,bt);
	}
	else
	{
		solve(mid+1,r,bt);
		solve(l,mid,c);
	}
}
string output(int l,int r)
{
	if(l==r) return string(1,seq[l]);
	int mid=(l+r)/2;
	string a=output(l,mid);
	string b=output(mid+1,r);
	if(a<b) return a+b;
	else return b+a;
}
bool check()
{
	int a=0,b=0,c=0;
	for(int i=0;i<n;i++)
		if(seq[i]=='R') a++;
		else if(seq[i]=='P') b++;
		else if(seq[i]=='S') c++;
	if(a!=r || b!=p || c!=s)
		return false;
	cout<<output(0,n-1)<<'\n';
	return true;
}
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T,no=0;
	cin>>T;
	while(T--)
	{
		cin>>n>>r>>p>>s;
		n=r+p+s;
		cout<<"Case #"<<++no<<": ";
		solve(0,n-1,'R');
		if(check()) continue;
		solve(0,n-1,'P');
		if(check()) continue;
		solve(0,n-1,'S');
		if(check()) continue;
		cout<<"IMPOSSIBLE"<<'\n';
	}
}