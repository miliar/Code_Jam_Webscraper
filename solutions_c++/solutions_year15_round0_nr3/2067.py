#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

struct Quaternion
{
	int adj[4][4];
	//a+b i + c j + d k
	Quaternion(int a=0, int b=0, int c=0, int d=0)
	{
		adj[0][0]=a; adj[0][1]=-b; adj[0][2]=-c; adj[0][3]=-d;
		adj[1][0]=b; adj[1][1]= a; adj[1][2]=-d; adj[1][3]= c;
		adj[2][0]=c; adj[2][1]= d; adj[2][2]= a; adj[2][3]=-b;
		adj[3][0]=d; adj[3][1]=-c; adj[3][2]= b; adj[3][3]= a;
	}
	int& operator()(int i, int j)
	{
		return adj[i][j];
	}
	int operator()(int i, int j) const
	{
		return adj[i][j];
	}
	Quaternion pow(int k);
};

Quaternion operator*(const Quaternion& a, const Quaternion& b)
{
	Quaternion res;
	REP(i,4) REP(j,4)
	{
		res(i,j)=0;
		REP(k,4)
			res(i,j)+=a(i,k)*b(k,j);
	}
	return res;
}

bool operator==(const Quaternion& a, const Quaternion& b)
{
	REP(i,4) REP(j,4)
		if(a(i,j)!=b(i,j))
			return false;
	return true;
}

bool operator!=(const Quaternion& a, const Quaternion& b)
{
	return !(a==b);
}

Quaternion Quaternion::pow(int k)
{
	Quaternion res(1,0,0,0);
	Quaternion a(*this);
	while(k)
	{
		if(k&1) res=res*a;
		a=a*a;
		k>>=1;
	}
	return res;
}

Quaternion I(0,1,0,0), J(0,0,1,0), K(0,0,0,1);
Quaternion q[3]={I,J,K};

char buf[10001];

bool solve()
{
	int l,x;
	scanf("%d%d",&l,&x);
	scanf("%s",buf);
	Quaternion cur(1,0,0,0);
	REP(i,l)
		cur=cur*q[buf[i]-'i'];
	cur=cur.pow(x);

	if(cur!=Quaternion(-1,0,0,0))
		return false;
	int top=0;
	cur=Quaternion(1,0,0,0);
	int cnt=0;
	int copyID=0;
	int posID=0;
	while(top<3 && copyID<x && cnt<=4*l)
	{
		if(posID==l)
		{
			copyID++;
			posID=0;
			continue;
		}
		cur=cur*q[(buf[posID++]-'i')];
		cnt++;
		if(cur==q[top])
		{
			top++;
			cnt=0;
			cur=Quaternion(1,0,0,0);
		}
	}
	return top==3;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: %s\n",test,solve()?"YES":"NO");
	}
	return 0;
}
