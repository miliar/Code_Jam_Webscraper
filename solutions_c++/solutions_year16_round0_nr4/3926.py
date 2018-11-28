#include<bits/stdc++.h>
using namespace std;
int t,k,c;
void dojob(int caseno)
{
	cin>>k>>c>>k;
	cout<<"Case #"<<caseno<<": ";
	long long jump=1,answer=1;
	int i,j,l;
	for(i=1;i<c;i++)jump*=k;
	for(i=1;i<=k;i++)
	{
		cout<<answer<<" ";
		answer+=jump;
	}
	cout<<endl;
}
int main()
{
	cin>>t;int i;
	for(i=1;i<=t;i++)dojob(i);
	return 0;
}
