#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<queue>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
const int N = 1005;
string got(int R,int P,int S)
{
	if(R+P+S==1)
	{
		if(R==1)
		{
			return "R";
		}
		if(P==1)return "P";
		return "S";
	}
	int x=R+P-S;
	if(x%2||x<0)return "IMPOSSIBLE";
	x/=2;
	int y=R-x;
	if(y<0)return "IMPOSSIBLE";
	int z=P-x;
	if(z<0)return "IMPOSSIBLE";
	//cout << "x: " << x << "y: " << y << "z: " << z << endl;
	string ret=got(y,x,z);
	return ret;
}
string dfs(char c,int dep)
{
	string ret;
	if(dep==0){ret+=c;return ret;}
	string a,b;
	if(c=='R')
	{
		a=dfs('R',dep-1);
		b=dfs('S',dep-1);
	}
	if(c=='P')
	{
		a=dfs('P',dep-1);
		b=dfs('R',dep-1);
	}
	if(c=='S')
	{
		a=dfs('P',dep-1);
		b=dfs('S',dep-1);
	}
	if(a+b<b+a)return a+b;
	return b+a;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	//scanf("%d",&T);
	cin >> T;
	while(T--)
	{
		cout << "Case #" << ca++ << ": "; 
		//printf("Case #%d: ",ca++);
		int n,P,R,S;
		scanf("%d%d%d%d",&n,&R,&P,&S);
		string ret=got(R,P,S);
		if(ret!="IMPOSSIBLE")
		{
			ret=dfs(ret[0],n);
		}
		cout << ret << endl;
	}
	return 0;
}

