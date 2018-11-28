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
int main()
{
	#ifdef DEBUG
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	#else
	ios::sync_with_stdio(false);
	#endif
	int t,ti;
	cin>>t;
	for (ti=1;ti<=t;ti++)
	{
		const int N=11000;
		static int a[N];
		static bool u[N];
		int n,x;
		cin>>n>>x;
		int i;
		for (i=0;i<n;i++)
		{
			cin>>a[i];
			u[i]=false;
		}
		sort(a,a+n);
		int ans=0;
		for (i=n-1;i>=0;i--)
		{
			if (u[i])
			{
				continue;
			}
			u[i]=true;
			ans++;
			int c=x-a[i];
			int j;
			for (j=i-1;j>=0;j--)
			{
				if (!u[j]&&a[j]<=c)
				{
					u[j]=true;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",ti,ans);
	}
	return 0;
}

