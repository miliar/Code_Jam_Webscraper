#include<bits/stdc++.h>
using namespace std;
int n;
int odata[1010];
int data[1010];
int cald[1010];
void input()
{
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>data[i];
		odata[i]=data[i];
	}
}
bool check()
{
	bool ic=true;
	for(int i=1;i<n;i++)
		if(data[i]>data[i-1] && ic==false)
			return false;
		else if(data[i]<data[i-1] && ic==true)
			ic=false;
	return true;
}
int cal()
{
	map<int,int> mm;
	for(int i=0;i<n;i++)
		mm[data[i]]=i;
	for(int i=0;i<n;i++)
		cald[i]=mm[odata[i]];
	int ans=0;
	for(int i=0;i<n;i++)
		for(int j=n-1;j>i;j--)
		{
			if(cald[j]<cald[j-1])
			{
				swap(cald[j],cald[j-1]);
				ans++;
			}
		}
	return ans;
}
int solve()
{
	sort(data,data+n);
	int ans=INT_MAX;
	do
	{
		if(check())
		{
			ans=min(ans,cal());
		}
	}
	while(next_permutation(data,data+n));
	return ans;
}
int main(int argc, char *argv[])
{
	int T;
	cin>>T;
	int TestDataFrom=1,TestDataTo=T;
	if(argc>=3)
		TestDataFrom=atoi(argv[1]),TestDataTo=atoi(argv[2]);
	for(int no=1;no<=TestDataTo;no++)
	{
		input();
		if(no<TestDataFrom) continue;
		clog<<no<<endl;
		int ans=solve();
		printf("Case #%d: %d\n",no,ans);
	}
}

