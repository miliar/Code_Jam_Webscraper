#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <string>
#include <cassert>

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define forup(i,a,b) for(int i=a; i<b; ++i)
#define fordn(i,a,b) for(int i=a; i>b; --i)
#define rep(i,a) for(int i=0; i<a; ++i)

#define dforup(i,a,b) for(i=a; i<b; ++i)
#define dfordn(i,a,b) for(i=a; i>b; --i)
#define drep(i,a) for(i=0; i<a; ++i)

#define slenn(s,n) for(n=0; s[n]!=13 and s[n]!=0; ++n);s[n]=0

#define gi(x) scanf("%d",&x)
#define gl(x) cin>>x
#define gd(x) scanf("%lf",&x)
#define gs(x) scanf("%s",x)

#define pis(x) printf("%d ",x)
#define pin(x) printf("%d\n",x)
#define pls(x) cout<<x<<" "
#define pln(x) cout<<x<<"\n"
#define pds(x) printf("%.12f ",x)
#define pdn(x) printf("%.12f\n",x)
#define pnl() printf("\n")

#define fs first
#define sc second

#define pb push_back

const int inv=1000000000;
const int minv=-inv;

const int max_m=8+5;
const int max_n=8+5;

struct node
{
	node* ch[26];
	node(){ rep(i,26) ch[i]=NULL; }
};
node* head;
int nodes;

void inserttrie(string s)
{
	node *curr=head;
	rep(i,(int)s.size())
	{
		if(curr->ch[(int(s[i]-'A'))]==NULL)
		{
			curr->ch[(int(s[i]-'A'))]=new node;
			++nodes;
		}
		curr=curr->ch[(int(s[i]-'A'))];
	}
}

void deletetrie(node* curr)
{
	rep(i,26)
		if(curr->ch[i]!=NULL)
			deletetrie(curr->ch[i]);
	delete curr;
}

int T;
int m,n;
string s[max_m];

int res,nres;
vector<string> V[max_n];
int a[max_m];
void backtrack(int x)
{
	if(x==m)
	{
		rep(i,n)
			if((int)V[i].size()==0)
				return;

		int cdt=0;
		rep(i,n)
		{
			head = new node; nodes=1;
			rep(j,(int)V[i].size())
				inserttrie(V[i][j]);
			cdt+=nodes;
			deletetrie(head);
		}

		if(cdt==res)
			++nres;
		else if(cdt>res)
		{
			res=cdt;
			nres=1;
		}
	}
	else
	{
		rep(i,n)
		{
			a[x]=i;
			V[i].pb(s[x]);
			backtrack(x+1);
			V[i].pop_back();
		}
	}
}

int main()
{
	gi(T);

	rep(z,T)
	{
		printf("Case #%d: ",z+1);

		gi(m); gi(n);
		rep(i,m)
			cin>>s[i];

		rep(i,n) V[i].resize(0);
		res=0; nres=0;
		backtrack(0);

		pis(res); pin(nres);
	}
	
	return 0;
}