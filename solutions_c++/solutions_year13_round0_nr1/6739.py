#include <sstream>
#include <iostream>
#include <iomanip>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <vector>
// #include "incl.h"
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))

int run()
{
	int res=0;
	int n,m,X=0,O=0,T=0,noopt=0; char arr[4][4];
	char temp;

//	cin>>n>>m;
	
	for(int i=0;i<4;i++)
	{
	for(int j=0;j<4;j++)
	{
		cin>>arr[i][j];if(arr[i][j]=='.') noopt=1;
	}
	}

	//row
	for(int i=0;i<4;i++)
	{
	for(int j=0;j<4;j++)
	{
		if(arr[i][j]=='X') X++;	
		if(arr[i][j]=='O') O++;	
		if(arr[i][j]=='T') { T++;}
	}
	//cout<<X<<O<<T<<endl;
	if(X==4 || (X==3 && T==1) ) {res=1; goto res;}
	if(O==4 || (O==3 && T==1) ) {res=2; goto res;}
	X=0;O=0;T=0;
	}
	
	//COL
	for(int i=0;i<4;i++)
	{
	for(int j=0;j<4;j++)
	{
		if(arr[j][i]=='X') X++;	
		if(arr[j][i]=='O') O++;	
		if(arr[j][i]=='T') { T++;}
	}
	if(X==4 || (X==3 && T==1) ) {res=1; goto res;}
	if(O==4 || (O==3 && T==1) ) {res=2; goto res;}
	X=0;O=0;T=0;
	}
	
	// diagonal
	{
	for(int i=0;i<4;i++)
	{
		if(arr[i][i]=='X') X++;	
		if(arr[i][i]=='O') O++;	
		if(arr[i][i]=='T') { T++;}
	}
	if(X==4 || (X==3 && T==1) ) {res=1; goto res;}
	if(O==4 || (O==3 && T==1) ) {res=2; goto res;}
	X=0;O=0;T=0;
	}
	
	{
	for(int i=0;i<4;i++)
	{
		if(arr[3-i][i]=='X') X++;	
		if(arr[3-i][i]=='O') O++;	
		if(arr[3-i][i]=='T') { T++;}
	}
	if(X==4 || (X==3 && T==1) ) {res=1; goto res;}
	if(O==4 || (O==3 && T==1) ) {res=2; goto res;}
	X=0;O=0;T=0;
	}
	
	// draw
	if(res==0)
	if(noopt==0) res=3;
	
	res:
	//print result
	switch(res)
	{
		case 0: cout<<"Game has not completed";break;
		case 1: cout<<"X won";break;
		case 2: cout<<"O won";break;
		case 3: cout<<"Draw";
	}
//	cin>>temp;
	return 0;
}

int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	cin>>testcase;
	REP(case_id,testcase)
	{
		cout<<"Case #"<<case_id+1<<": ";
		run();
		cout<<endl;
		fflush(stdout);
	}
	return 0;
}

