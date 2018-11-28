#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int a[120][120];
bool mark[120][120];
string solve()
{
	int n,m,i,j,ma;
	cin>>n>>m;
	for(i=0;i<105;i++) for(j=0;j<105;j++) {a[i][j]=0;mark[i][j]=false;}
	for(i=0;i<n;i++) for(j=0;j<m;j++) cin>>a[i][j];
	for(i=0;i<n;i++)
	{
		ma=0;
		for(j=0;j<m;j++) if(a[i][j]>ma) ma=a[i][j];
		for(j=0;j<m;j++) if(a[i][j]==ma) mark[i][j]=true;
	}
	for(i=0;i<m;i++)
	{
		ma=0;
		for(j=0;j<n;j++) if(a[j][i]>ma) ma=a[j][i];
		for(j=0;j<n;j++) if(a[j][i]==ma) mark[j][i]=true;
	}
	for(i=0;i<n;i++) for(j=0;j<m;j++) if(!mark[i][j]) return "NO";
	return "YES";
}
int main()
{
	freopen("2.in","r",stdin);
	freopen("output.txt","w",stdout);
	int n,i;
	cin>>n;
	for(i=0;i<n;i++) {cout<<"Case #"<<i+1<<": "<<solve()<<endl;}
	return 0;
}