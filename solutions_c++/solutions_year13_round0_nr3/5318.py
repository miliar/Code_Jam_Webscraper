#include<cstdio>
#include<vector>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
char str[20];
bool ispalin(long long x)
{
	sprintf(str,"%d",x);
	int len=strlen(str),i;
	for(i=0;i<len/2;i++)
	{
		if(str[i]!=str[len-1-i]) return false;
	}
	return true;
}

int issqf(long x)
{
	long f=sqrt(x);
	if(f*f!=x) return false;
	if(ispalin(x) && ispalin(f)) return true;
	return false;
}

int main()
{
	int N;
	N=10000001;
	int cnt=0,i;
	vector<long long> v;
	for(i=1;i<=N;i++)
		if(ispalin(i) && ispalin(i*i)) { cnt++; v.push_back(i*i);}
	int tc,T;
	scanf(" %d",&T);
	for(tc=1;tc<=T;tc++){
		long long A,B;
		scanf(" %lld %lld",&A,&B);
		int start,end;
		start=distance(v.begin(),lower_bound(v.begin(),v.end(),A));
		end=distance(v.begin(),lower_bound(v.begin(),v.end(),B));
		if(end==v.size()) end--;
		if(start==v.size()) start--;
		if(v[end]>B) end--;
		int dist;
		printf("Case #%d: %d\n",tc,end-start+1);
	}
	
	
	return 0;
}

