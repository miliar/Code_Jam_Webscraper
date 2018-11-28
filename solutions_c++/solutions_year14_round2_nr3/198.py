#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include <climits>
#include<cmath>
#include<string>
#include <functional>
#include<sstream>
#include<map>
#include<set>


#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MAXM              1001
#define     MOD               1000000007
#define     Dbug             cout<<"";
#define     EPS              1e-15
typedef long long ll;
typedef pair<int,int> pii;
int n, m, mat[10][10], mat2[10][10];
string st, zip[10];

int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, t=1, u, v;
	cin>>tc;
	while (tc--)
	{
		Set(mat, 0);
		st="";
		cin>>n>>m;
		vector<int> vec;
		Rep(i, n) vec.push_back(i), cin>>zip[i];
		Rep(i, m)
		{
			cin>>u>>v;
			u--, v--;
			mat[u][v]=mat[v][u]=1;
		}
		do
		{
			string t=zip[vec[0]];
			stack<int> q;
			u=vec[0];
			bool can=1;
			For(i, 1, vec.size())
			{
				v=vec[i];
				while(!q.empty() && mat[u][v]==0)
				{
					u=q.top();
					q.pop();
				}
				if(mat[u][v]==0)
				{
					can=0;
					break;
				}
				t+=zip[v];
				q.push(u);
				u=v;
			}
			if(t.size()==5*n) 
			{
				if(st=="") st=t;
				else st=min(st, t);
			}
		} while (next_permutation(ALL(vec)));
		PF("Case #%d: ", t++);
		cout<<st<<endl;
	}
	return 0;
}