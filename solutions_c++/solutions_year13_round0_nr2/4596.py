#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <cassert>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define EACH(t,i,c) for(t::iterator i=(c).begin(); i!=(c).end(); ++i)
const double EPS = 1e-10;
const double PI  = acos(-1.0);

int dfs(int ii,int dir,vi &used1,vi &used2,vvi &g1,vvi &g2,int n,int m){
	if(dir==0){
		used1[ii]=1;
		for (int i = 0; i < m; i++)
		{
			if(g1[ii][i]){
				if(used2[i]){
					return true;
				}else if(dfs(i,(dir+1)%2,used1,used2,g1,g2,n,m)){
					return true;
				}
			}
		}
	}else{
		used2[ii]=1;
		for (int i = 0; i < n; i++)
		{
			if(g2[ii][i]){
				if(used1[i]){
					return true;
				}else if(dfs(i,(dir+1)%2,used1,used2,g1,g2,n,m)){
					return true;
				}
			}
		}
	}
	return false;
}

int main() {
	int t;
	cin>>t;
	for (int test = 1;test <= t;	test++)
	{
		int n,m;
		cin>>n>>m;
		vvi f(n,vi(m));
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				cin>>f[i][j];
			}
		}
		vvi g1(n,vi(m));
		for (int i = 0; i < n; i++)
		{
			int mx=0;
			for (int j = 0; j < m; j++)
			{
				mx=max(mx,f[i][j]);
			}
			for (int j = 0; j < m; j++)
			{
				if(f[i][j]<mx){
					g1[i][j]=1;
				}
			}
		}
		vvi g2(m,vi(n));
		for (int j = 0; j < m; j++)
		{
			int mx=0;
			for (int i = 0; i < n; i++)
			{
				mx=max(mx,f[i][j]);
			}
			for (int i = 0; i < n; i++)
			{
				if(f[i][j]<mx){
					g2[j][i]=1;
				}
			}
		}

		bool found=false;
		for (int i = 0; i < n; i++)
		{
			vi used1(n),used2(m);
			if(dfs(i,0,used1,used2,g1,g2,n,m)){
				found=true;
				goto end;
			}
		}
		for (int i = 0; i < m; i++)
		{
			vi used1(n),used2(m);
			if(dfs(i,1,used1,used2,g1,g2,n,m)){
				found=true;
				goto end;
			}
		}
end:

		cout<<"Case #"<<test<<": ";
		cout<<(found?"NO":"YES")<<endl;
	}
}