#define _CRT_SECURE_NO_WARNINGS
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <list>
#include <cassert>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define pii pair <int ,char>
int p[1001];
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define EPS 1e-9
using namespace std;

int main()
{
	ios_base :: sync_with_stdio(false);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,p1=1; cin>>t;while(t--){
int n;priority_queue < pair <int ,char> > q;cin>>n;
char ch='A';for(int i=0;i<n;i++){
			cin>>p[i];
			char ch1=ch+i;
			q.push({p[i],ch1});
		}bool flag =false;
cout<<"Case #"<<p1<<": ";
while(!q.empty())
{ pii p1 =q.top();
if(p1.first==1&&q.size()==3)
{q.pop();cout<<p1.second<<" ";
continue;}q.pop();
pii p2;
 if(!q.empty()) {
p2 =q.top();  q.pop();
		    flag =true;
		   }cout<<p1.second<<p2.second<<" ";if(flag)
		   { p1.first-=1;
 p2.first-=1;
		         if(p1.first>0)
		        {
					q.push(p1); 
				}
		        if(p2.first>0)
		      {
				   q.push(p2);
				   } } else 
{	p1.first-=2;
		  	if(p1.first>0)
		          q.push(p1);
 }
}p1++;
cout<<"\n";
}
}

