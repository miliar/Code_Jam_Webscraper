#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
using namespace std;
#ifndef for
	#define for if (0) ; else for
#endif
#ifndef ONLINE_JUDGE
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
	void _REDIRECT(bool in,bool out)
	{
		const char * f=__FILE__;
		int i;
		for (i=strlen(f)-1;i>=0;i--)
		{
			if (f[i]=='.')
			{
				break;
			}
		}
		char *p=new char[strlen(f)+10];
		strncpy(p,f,i);
		if (in)
		{
			strcpy(p+i,".in");
			freopen(p,"r",stdin);
		}
		if (out)
		{
			strcpy(p+i,".out");
			freopen(p,"w",stdout);
		}
		delete[] p;
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
const int W=110;
int w,h;
inline bool inMap(int y,int x) {
	return 0<=y&&y<h&&0<=x&&x<w;
}
char map[W][W];
bool danger[W][W][4];
const int dx[4]={1,0,-1,0},dy[4]={0,-1,0,1};
const char arrow[]=">^<v";

int main()
{
	#ifdef DEBUG
	_REDIRECT(0,0);
	#else
	ios::sync_with_stdio(false);
	#endif
	int t,ti;
	cin>>t;
	for (ti=1;ti<=t;ti++) {
		cin>>h>>w;
		int y,x;
		for (y=0;y<h;y++) {
			cin>>map[y];
		}
		bool safe=true;
		int ans=0;
		for (y=0;y<h;y++) {
			for (x=0;x<w;x++) {
				if (map[y][x]=='.') {
					continue;
				}
				int totalDanger=0;
				int d;
				for (d=0;d<4;d++) {
					danger[y][x][d]=true;
					int y2=y,x2=x;
					int i;
					for (i=0;i<W;i++) {
						y2+=dy[d];
						x2+=dx[d];
						if (!inMap(y2,x2)) {
							break;
						}
						if (map[y2][x2]!='.') {
							danger[y][x][d]=false;
							break;
						}
					}
					if (danger[y][x][d]) {
						totalDanger++;
					}
				}
				if (totalDanger==4) {
					safe=false;
					break;
				}
				for (d=0;d<4;d++) {
					if (map[y][x]==arrow[d]) {
						if (danger[y][x][d]) {
							ans++;
						}
					}
				}
			}
		}
		printf("Case #%d: ",ti);
		if (safe) {
			printf("%d\n",ans);
		}
		else { 
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}

