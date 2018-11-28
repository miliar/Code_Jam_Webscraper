#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int>vp;
bool comp(int x,int y)
{
	return x>y;
}
int mini,tmp;
void go(vector<int>v,int l)
{
	
	int i,m,j,s;
	m=v[0]/2;
	for(i=1;i<=m;i++)
	{
		vp.clear();
		for(j=1;j<v.size();j++)
		vp.push_back(v[j]);
		vp.push_back(i);
		vp.push_back(v[0]-i);
		
		sort(vp.begin(),vp.end(),comp);
		s=l+vp[0];
		if(s<mini)
		mini=s;
		if(vp[0]>3 && l+1<tmp)
		go(vp,l+1);
		
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
		vp.push_back(num);
		///cout<<num<<" ";
	}
//	cout<<endl;
	sort(vp.begin(),vp.end(),comp);

	mini=vp[0];
	tmp = mini;
	go(vp,1);
	printf("Case #%d: %d\n",t,mini);
	vp.clear();
   }
return 0;	
}
