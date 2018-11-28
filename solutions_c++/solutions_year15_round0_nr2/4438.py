#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int>v1;
bool comp(int x,int y)
{
	return x>y;
}
int minim,tmp;
void go(vector<int>v0,int l)
{
	
	int i,m,j,s;
	m=v0[0]/2;
	for(i=1;i<=m;i++)
	{
		v1.clear();
		for(j=1;j<v0.size();j++)
		v1.push_back(v0[j]);
		v1.push_back(i);
		v1.push_back(v0[0]-i);
		
		sort(v1.begin(),v1.end(),comp);
		s=l+v1[0];
		if(s<minim)
		minim=s;
		if(v1[0]>3 && l<tmp)
		go(v1,l+1);
		
	}
	
	
	
}
int main()
{
freopen("0in.txt", "r", stdin);
   freopen("0out.txt", "w", stdout);
	int t,tcase;
	scanf("%d",&tcase);
	for(t=1;t<=tcase;t++)
	{
	int n,i,num;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>num;
		v1.push_back(num);
	
	}

	sort(v1.begin(),v1.end(),comp);

	minim=v1[0];
	tmp = minim;
	go(v1,1);
	printf("Case #%d: %d\n",t,minim);
	v1.clear();
   }
return 0;	
}
