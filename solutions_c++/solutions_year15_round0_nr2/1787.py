#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<fstream>
using namespace std;
struct P{
	int x,y;
	P(){}
	P(int a,int b):x(a),y(b){}
};
P p;
double t;
int a,n,num[1010],d[1010][31],ans,maxnum,res,k=0;
P binary(int limit,int now)
{
	int l=1,r=30,mid;
	while(l<r)
	{
		mid=(l+r)/2;
		if(d[now][mid]>limit)
			l=mid+1;
		else 
			r=mid;
	}
	return P(d[now][l],l-1);
}
int main()
{
	fstream file1,file2;
	file1.open("a.in",ios::in);
	file2.open("b.txt",ios::out);
	file1>>a; //scanf("%d",&a);
	while(a--)
	{
		k++;
		res=1e9;
		file1>>n; //scanf("%d",&n);
		for(int q=0;q<n;++q)
			file1>>num[q]; //scanf("%d",&num[q]);
		for(int q=0;q<n;++q)
		{
			for(int w=1;w<=30;++w)
			{
				t=(double)num[q]/w;
				d[q][w]=num[q]/w;
				if(t>d[q][w])
					d[q][w]=t+1;
			}
		}
		for(int q=1;q<=1000;++q)
		{
			maxnum=ans=0;
			for(int w=0;w<n;++w)
			{
				p=binary(q,w);
				ans+=p.y;
				maxnum=max(maxnum,p.x);
			}
			ans+=maxnum;
			res=min(res,ans);
		}
		file2<<"Case #"<<k<<": "<<res<<"\n"; //printf("Case #%d: %d\n",k,res);
	}
 	return 0;
}

