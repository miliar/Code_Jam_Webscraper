#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int l,t,n,i,j,k;
	FILE *ptr,*ptr1;
	char s[1009];
	string ss;
	ptr=fopen("A1-large.in","r+");
	ptr1=fopen("A1-large2.in","w+");
	fscanf(ptr,"%lld",&t);
	map<int,int> mp;
	map<int,int> ::iterator it;
	for(k=1;k<=t;k++)
	{
		fscanf(ptr,"%lld",&n);
		for(i=0;i<2*n-1;i++)
		{
			for(j=0;j<n;j++)
			{
				fscanf(ptr,"%lld",&l);
				mp[l]+=1;
			}
		}
		fprintf(ptr1,"Case #%lld:",k);
	for(it=mp.begin();it!=mp.end();it++)
	{
		if(it->second&1)
		fprintf(ptr1," %d",it->first);
	}
		fprintf(ptr1,"\n");
		mp.clear();
	}
	return 0;
}

