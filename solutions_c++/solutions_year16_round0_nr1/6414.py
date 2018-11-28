#include<bits/stdc++.h>
using namespace std;
int t,n;
bool visited[10];
void add(long long no)
{
	while(no>0)
	{
		visited[no%10]=1;
		no/=10;
	}
}
bool check()
{
	int i;
	for(i=0;i<10;i++)if(!visited[i])return 0;
	return 1;
}
void ini()
{
	int i;
	for(i=0;i<10;i++)visited[i]=0;
}
void dojob(int caseno)
{
	cin>>n;
	cout<<"Case #"<<caseno<<": ";
	if(n==0){cout<<"INSOMNIA"<<endl;return;}
	ini();
	long long answer=0;
	while(!check())
	{
		add(answer+n);
		answer+=n;
	}
	cout<<answer<<endl;
}
int main()
{
	cin>>t;
	int i;
	for(i=1;i<=t;i++)dojob(i);
	return 0;
}
