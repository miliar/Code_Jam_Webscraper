#define LL long long
#include <bits/stdc++.h>
using namespace std;

int a[1<<5];
vector<int> res;

LL judge(LL k)
{
	for(int i=2;(LL)i*i<=k;i++)
		if(k%i==0) return i;
	return 0;
}

void Trans(int k,int* a)
{
	for(int i=0;i<32;i++)
		a[i]=0;
	for(int i=31;k;k>>=1)
		a[i--]=k&1;
}

LL Trans2(int* a,int b)
{
	LL res=0;
	for(int i=0;i<32;i++)
		res=res*b+a[i];
	return res;
}

int main()
{
	freopen("out","w",stdout);
	puts("Case #1:");
	for(int i=(1<<15)+1;i<(1<<16);i+=2)
	{
		Trans(i,a);

		bool f=1;
		for(int j=2;j<=10;j++)
			if(!judge(Trans2(a,j)))
			{
				f=0;
				break;
			}
		if(f)
		{
			res.push_back(i);
			if(res.size()==50) break;
		}
	}
	for(int i=0;i<res.size();i++)
	{
		Trans(res[i],a);

		int st=0;
		for(int j=0;j<32;j++)
		{
			if(a[j] && !st) st=j;
			if(st) putchar(a[j]+48);
		}

        for(int j=2;j<=10;j++)
        	cout<<" "<<judge(Trans2(a,j));
		cout<<endl;
	}
	return 0;
}
