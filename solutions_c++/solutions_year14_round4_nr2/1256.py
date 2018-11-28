#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
using namespace std;
#ifndef for
	#define for if (0) ; else for
#endif
#ifndef DEBUIG
	#define DEBUG
#endif
//This file only works in GNU C++
#ifdef DEBUG
	int _CALL_DEPTH=0;
	struct _CALL_STACK
	{
		_CALL_STACK();
		~_CALL_STACK();
	};
	#define _PRINT_STACK_TAB(number) if (number) printf("%5d:\t",__LINE__); else printf("\t"); for (int i=0;i<_CALL_DEPTH;i++) printf("\t");
	#define VAR(f,x) _PRINT_STACK_TAB(true); printf("%s=\t" f "\n",#x,x);
	#define MSG(format,...) _PRINT_STACK_TAB(true); printf(format "\n",##__VA_ARGS__);
	#define FUNC _PRINT_STACK_TAB(true); printf("%s\n",__PRETTY_FUNCTION__); _CALL_STACK _call_stack; 
	_CALL_STACK::_CALL_STACK()
	{
		_PRINT_STACK_TAB(false);
		printf("{\n");
		_CALL_DEPTH++;
	}
	_CALL_STACK::~_CALL_STACK()
	{
		_CALL_DEPTH--;
		_PRINT_STACK_TAB(false);
		printf("}\n");
	}
#else
	//display a single variable, like
	//	VAR("%d",x);
	#define VAR
	//display a message, like
	//	MSG("a[%d]=%d",i,a[i]);
	#define MSG
	//put this line at the beginning of a function in order to update the indent of call stack
	#define FUNC
#endif
const int N=1100;
int merge(int *a,int l,int r)
{
	if (l+1>=r)
	{
		return 0;
	}
	int m=(l+r)/2;
	int ret=0;
	ret+=merge(a,l,m);
	ret+=merge(a,m,r);
	static int b[N];
	int i=l,j=m,k=0;
	while (i<m||j<r)
	{
		if ((j==r)||(i<m&&a[i]<a[j]))
		{
			b[k]=a[i];
			i++;
			k++;
		}
		else
		{
			b[k]=a[j];
			j++;
			k++;
			ret+=m-i;
		}
	}
	for (i=l;i<r;i++)
	{
		a[i]=b[i-l];
	}
	return ret;
}
bool check(int *a,int *s,int n)
{
	bool up=true;
	int i;
	for (i=0;i+1<n;i++)
	{
		if (up)
		{
			if (a[s[i]]>a[s[i+1]])
			{
				up=false;
			}
		}
		else
		{
			if (a[s[i]]<a[s[i+1]])
			{
				return false;
			}
		}
	}
	return true;
}
int find(int* a,int *s,bool *u,int x,int n)
{
	if (x==n)
	{
		if (!check(a,s,n))
		{
			return 2147483647;
		}
		else
		{
			static int b[N];
			int i;
			for (i=0;i<n;i++)
			{
				b[i]=s[i];
			}
			int ret=merge(b,0,n);
			if (0&&ret==9)
			{
				for (i=0;i<n;i++)
				{
					printf("%d ",a[s[i]]);
				}
				printf("\n");
			}
			return ret;
		}
	}
	int ret=2147483647;
	int i;
	for (i=0;i<n;i++)
	{
		if (u[i])
		{
			continue;
		}
		u[i]=true;
		s[x]=i;
		int current=find(a,s,u,x+1,n);
		if (current<ret)
		{
			ret=current;
		}
		u[i]=false;
	}
	return ret;
}
int main()
{
	#ifdef DEBUG
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1_by-small.out","w",stdout);
	#else
	ios::sync_with_stdio(false);
	#endif
	int t,ti;
	cin>>t;
	for (ti=1;ti<=t;ti++)
	{
		int n;
		cin>>n;
		static int a[N];
		int i,j;
		for (i=0;i<n;i++)
		{
			cin>>a[i];
		}
		static int s[N];
		static bool u[N];
		int ans=find(a,s,u,0,n);
		printf("Case #%d: %d\n",ti,ans);
	}
	return 0;
}

