//#include <bits/stdc++.h>
#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<iomanip>
#include<math.h>
#include<limits.h>
#include<string.h>
#include <ctime>
#include <deque>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<bitset>
#include<set>
#include <sstream>
#include <list>
#define mod 1000000007
#define MAX 100000000

using namespace std;
#define scan(a) scanf("%d",&a);
#define print(a) printf("%d\n",a);
#define mem(a,v) memset(a,v,sizeof(a))
#define clr(a) memset(a,0,sizeof(a))
#define pb(x) push_back(x)
#define sort(a) sort(a.begin(),a.end())
#define inf 1e9
#define mp(a,b) make_pair(a,b)
#define V vector
#define S string
#define Gu getchar_unlocked
#define Pu putchar_unlocked
#define Read(n) ch=Gu(); while (ch<'0') ch=Gu(); n=ch-'0'; ch=Gu(); while (!(ch<'0')) {n=10*n+ch-'0'; ch=Gu();}
#define Write(n) r=n; chptr=s; *chptr=r%10+'0'; r/=10; for (; r; r/=10) {++chptr; *chptr=r%10+'0'; } Pu(*chptr); for (; chptr!=s; ) Pu(*--chptr);
typedef long long LL;
typedef long double LD;
typedef long L;
typedef pair<int,int> pii;
const double pi=acos(-1.0);
int main()
{
   	/*int ch;
   	int r;
   	char s[12];
   	char *chptr;*/
   	//freopen("in.in","r",stdin);
   	//freopen("out.out","w",stdout);
	ios_base::sync_with_stdio(false);
	int t,cc=1;
	cin>>t;
	while(t--)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(x==1)
			cout<<"Case #"<<cc++<<": GABRIEL"<<endl;
		else if(x==2)
		{
			if((r==1 && c==1) || (r==1 && c==3) || (r==3 && c==3) || (r==3 && c==1))
				cout<<"Case #"<<cc++<<": RICHARD"<<endl;
			else
				cout<<"Case #"<<cc++<<": GABRIEL"<<endl;
		}
		else if(x==3)
		{
			if((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3))
				cout<<"Case #"<<cc++<<": GABRIEL"<<endl;
			else
				cout<<"Case #"<<cc++<<": RICHARD"<<endl;
		}
		else
		{
			if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4))
				cout<<"Case #"<<cc++<<": GABRIEL"<<endl;
			else
				cout<<"Case #"<<cc++<<": RICHARD"<<endl;
		}
	}
	return 0;
}




