#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <string.h>
 
#include <utility>
#include <algorithm>
#include <cassert>
 
using namespace std;
 
//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
 
//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))
 
//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)
 
 
 
//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
 
// my own
#define sl(a) scanf("%lld",&a)
#define sll(a,b) scanf("%lld%lld",&a,&b)
#define slll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sllll(a,b,c,d) scanf("%lld%lld%lld%lld",&a,&b,&c,&d)
#define fastio std::ios_base::sync_with_stdio(false)


int main()
{
	set<pair<int,char> >S;
	set<pair<int,char> > :: iterator it;
	
	int i,val,T,N,ctr;
	pair<int,char> P;
	cin>>T;
	ctr=1;
	while(T--)
	{
		cin>>N;
		S.clear();
		repi(i,0,N)
		{
			cin>>val;
			P=make_pair(val,i+65);
			S.insert(P);
		}

		cout<<"Case #"<<ctr<<": ";
		while(S.size())
		{
			it=S.end();
			it--;
			P=*it;
			
			S.erase(it);
			cout<<P.second;
			P.first--;
			if(P.first)
				S.insert(P);
			if(S.size())
			{
				it=S.end();
				it--;
				P=*it;
				if(P.first==1 && S.size()==2)
				{
					cout<<" ";
					continue;
				}
				S.erase(it);
				cout<<P.second<<" ";
				P.first--;
				if(P.first)
					S.insert(P);
			}
		}
		ctr++;
		cout<<endl;

	}
}