#include<iostream>
#include<bits/stdc++.h>
#define whatis(x) cout << #x << " is " << x << endl;
#include<queue>

using namespace std;

int n;
int con[1000001][3];
int maxx=2000001;
int vis[1000001];
int mins[1000001];

int rev(int a)
{
	int b=0;
	while(a!=0)
	{
		b=b*10+a%10;
		a=a/10;
	}
	if(b>1000000 || b<0)
		b=0;
	return b;
}

void dfs(int a,int count)
{
	queue <int> myqueue;
	myqueue.push(a);
	vis[1]=1;
	while(!myqueue.empty())
	{
		a=myqueue.front();
		myqueue.pop();
		if(a<1000000)
		{
			vis[a]=1;
			if(vis[a+1]==0)
			{
				vis[a+1]=1;
				myqueue.push(a+1);
				mins[a+1]=mins[a]+1;
			}
			if(vis[rev(a)]==0)
			{
				vis[rev(a)]=1;
				myqueue.push(rev(a));
				mins[rev(a)]=mins[a]+1;
			}
		}
	}
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	int t,a,b,c,i,j,k;
	cin >> t;
	for(i=0;i<t;i++)
	{
		for(j=0;j<1000001;j++)
		{
			vis[j]=0;
			mins[j]=2000001;
		}
		mins[1]=1;
		cin >> n;
		vis[1]=1;
		dfs(1,1);
		cout << "Case #" << i+1 << ": " << mins[n] << endl;
	}
	return 0;
}
