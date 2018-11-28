/*

*/
 
//#pragma comment(linker, "/STACK:16777216")
#include <fstream>
#include <iostream>
#include <string>
#include <complex>
#include <math.h>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stdio.h>
#include <stack>
#include <algorithm>
#include <list>
#include <ctime>
#include <memory.h>
#include <ctime> 
 
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
 
#define eps 1e-9
//#define M_PI 3.141592653589793
#define bs 1000000007
#define bsize 256

using namespace std;

int tests;
int n,m;
char board[500][500];
string st;
int d[500][500],u[500][500],l[500][500],r[500][500];
int ans;
int ts;

int main(){
//freopen("newlines.in","r",stdin);
//freopen("newlines.out","w",stdout);
freopen("F:/in.txt","r",stdin);
freopen("F:/output.txt","w",stdout);
ios_base::sync_with_stdio(0);
//cin.tie(0);

cin>>tests;
for (;tests;--tests)
{
	cin>>n>>m;
	for (int i=1;i<=n;i++)
	{
		cin>>st;
		for (int j=1;j<=m;j++)
		 board[i][j]=st[j-1];
	}
	ans=0;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
		{
			if (board[i][j]=='.')continue;
			l[i][j]=r[i][j]=u[i][j]=d[i][j]=0;
			for (int q=i-1;q>=1;--q)
			 if (board[q][j]!='.')
			  	u[i][j]=1;
			for (int q=i+1;q<=n;q++)
			 if (board[q][j]!='.')
			    d[i][j]=1;
			for (int q=1;q<j;q++)
			 if (board[i][q]!='.')
			  l[i][j]=1;
			 for (int q=j+1;q<=m;q++)
			  if (board[i][q]!='.')
			   r[i][j]=1; 
			if (l[i][j]+r[i][j]+u[i][j]+d[i][j]==0)
			 ans=1e6;
			if (board[i][j]=='^'&&u[i][j]==0)++ans;
			if (board[i][j]=='>'&&r[i][j]==0)++ans;
			if (board[i][j]=='<'&&l[i][j]==0)++ans;
			if (board[i][j]=='v'&&d[i][j]==0)++ans;
		}
		++ts;
		cout<<"Case #"<<ts<<": ";
		if (ans>1e5)cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
}

//cin.get();cin.get();
return 0;}
