//  Created by Chlerry in 2015.
//  Copyright (c) 2015 Chlerry. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define ll long long

int t,n,input;
vector<int> v;

void Output(vector<int> vt)
{
	for(int i=0;i<vt.size();i++)
		cout<<vt[i]<<' ';
	cout<<endl;
}
bool is(int share,int eat,vector<int> vt)
{
	vector<int> v1=vt,v2=vt;
	//cout<<"~~~"<<share<<','<<eat<<"  ";
	//Output(vt);
	if(!share)
		return (vt[0]<=eat);
	else if(!eat)
		return (vt[0]<=0);
	else
	{
		int temp=vt[0]-eat;

		v1[0]=INT_MIN;
		v1.push_back(temp);
		pop_heap(v1.begin(),v1.end());
		//v1.pop_back();
		//v1.push_back(temp);
		//make_heap(v1.begin(),v1.end());
		for(int i=0;i<v2.size();i++)
			v2[i]--;
		return is(share-1,eat,v1)||is(share,eat-1,v2);
	}
	return 0;
}
bool is_mid(int x)
{
	for(int i=0;i<=x;i++)
	{
		//cout<<"START "<<x<<':'<<i<<','<<x-i<<endl;
		if(is(i,x-i,v))
		{
			//cout<<"DONE!\n";
			return 1;
		}
	}
	return 0;
}
int Find(int l,int r)
{
	if(l==r)
		return l;
	int mid=(l+r)/2;
	if(is_mid(mid))
		return Find(l,mid);
	//else
		return Find(mid+1,r);
}
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("B-small-attempt1.in","r",stdin);
	//freopen("B-small-attempt0.out","w",stdout);
	cin>>t;
for(int ca=1;ca<=t;ca++)
{
	memset(&v,0,sizeof(v));
	//cout<<"---"<<v.size()<<"-----------\n";
	cin>>n;
	int maxn=0;
	for(int i=0;i<n;i++)
	{
		cin>>input;
		if(maxn<input)
			maxn=input;
		v.push_back(input);
	}
	make_heap(v.begin(),v.end());
	//cout<<Find(0,maxn)<<"<-ans"<<endl;
	//cout<<is_mid(2)<<endl;
	cout<<"Case #"<<ca<<": "<<Find(0,maxn)<<endl;
}
	return 0;
}


