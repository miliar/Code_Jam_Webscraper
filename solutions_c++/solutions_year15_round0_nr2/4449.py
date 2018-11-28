#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int>v2;
bool comp(int x,int y)
{
	return x>y;
}
int mi,tmp;
void go(vector<int>v1,int l)
{
	
	int i,m,j,s;
	m=v1[0]/2;
	for(i=1;i<=m;i++)
	{
		v2.clear();
		for(j=1;j<v1.size();j++)
		v2.push_back(v1[j]);
		v2.push_back(i);
		v2.push_back(v1[0]-i);
		
		sort(v2.begin(),v2.end(),comp);
		s=l+v2[0];
		if(s<mi)
		mi=s;
		if(v2[0]>3 && l+1<tmp)
		go(v2,l+1);
		
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
		v2.push_back(num);
	
	}

	sort(v2.begin(),v2.end(),comp);

	mi=v2[0];
	tmp = mi;
	go(v2,1);
	printf("Case #%d: %d\n",t,mi);
	v2.clear();
   }
return 0;	
}
