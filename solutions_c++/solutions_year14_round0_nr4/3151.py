#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int AwB(int len,vector<int > A,vector<int > B)
{
	sort(A.begin(),A.end());
	sort(B.begin(),B.end());
	bool v[len];
	memset(v,false,sizeof(v));
	int ans=0;
	for(int i=len-1;i>=0;i--)
		for(int j=len-1;j>=0;j--)
			if(A[i]>B[j]&&!v[j])
			{
				v[j]=true;
				ans++;
				break;
			}
	return ans;
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("DoutL.txt","w",stdout);
	int T,sz;
	cin>>T;
	vector<int > K,N;
	double tmp;
	for(int i=1;i<=T;i++)
	{
		K.clear();
		N.clear();
		cin>>sz;
		for(int k=0;k<sz;k++)
			cin>>tmp,tmp*=1000000,tmp+=0.5,N.push_back((int)(tmp));
		for(int k=0;k<sz;k++)
			cin>>tmp,tmp*=1000000,tmp+=0.5,K.push_back((int)(tmp));
		printf("Case #%d: %d %d\n",i,AwB(sz,N,K),sz-AwB(sz,K,N));
	}
	return 0;
}
