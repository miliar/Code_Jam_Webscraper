/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
typedef unsigned int uint;
#define pb push_back
#define fi first
#define se second
#define mp make_pair

const int MOD=1000000007,dx[]={0,1,0,-1},dy[]={1,0,-1,0};
const double eps=1e-8;

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

int lis[1000000],len,l;
char s[100];

bool rev(llint x)
{
	sprintf(s,"%I64d",x);
	l=strlen(s);
	for(int i=0;i*2<l;i++) if (s[i]!=s[l-i-1]) return 0;
	return 1;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int T,tt,ans;
	llint L,R;
	for(int i=1;i<=10000000;i++)
		if (rev(i)&&rev(1ll*i*i))
		{
			//cout<<i<<' '<<len<<endl;
			lis[++len]=i;
		}
	for(cin>>T,tt=1;tt<=T;tt++)
	{
		cin>>L>>R;
		ans=0;
		for(int i=1;i<=len;i++)
			if (1ll*lis[i]*lis[i]>=L&&1ll*lis[i]*lis[i]<=R) ans++;
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
	
	return 0;
}
