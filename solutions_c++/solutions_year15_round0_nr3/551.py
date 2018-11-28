#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <algorithm>
#include <list>
#include <ctime>
#include <cstdio>
#include <stack>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <functional>
#include <sstream>
#include <map>
#include <set>

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
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-8
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
typedef long long ll;
typedef pair<int,int> pii;
int n;
string st, tmp;
pair<bool, char> chng(pair<bool, char> t, char x)
{
	if(x=='1') return t;
	if(t.second=='1') 
	{
		t.second=x;
		return t;
	}
	if(t.second==x)
	{
		t.second='1', t.first=1-t.first;
		return t;
	}
	if(x=='i') 
	{
		if(t.second=='k') t.second='j';
		else t.second='k', t.first=1-t.first;
		return t;
	}
	if(x=='j')
	{
		if(t.second=='i') t.second='k';
		else t.second='i', t.first=1-t.first;
		return t;
	}
	if(x=='k')
	{
		if(t.second=='j') t.second='i';
		else t.second='j', t.first=1-t.first;
		return t;
	}
}
bool solve()
{
	pair<bool, char> cur=MP(0, st[0]);
	int ind=-1;
	if(cur.second=='i') ind=1;
	else For(i, 1, tmp.size())
	{
		cur=chng(cur, tmp[i]);
		ind=i+1;
		if(cur.first==0 && cur.second=='i') break;
	}
	if(ind>=tmp.size() || !(cur.first==0 && cur.second=='i')) return 0;
	cur=MP(0, tmp[ind]);
	if(cur.second=='j') ind++;
	else For(i, ind+1, tmp.size())
	{
		cur=chng(cur, tmp[i]);
		ind=i+1;
		if(cur.first==0 && cur.second=='j') break;
	}
	if(ind>=tmp.size() || !(cur.first==0 && cur.second=='j')) return 0;
	cur=MP(0, tmp[ind]);
	For(i, ind+1, tmp.size()) cur=chng(cur, tmp[i]);
	if(cur.first==0 && cur.second=='k') return 1;
	return 0;
}
int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cas=1;
	ll x, l;
	cin>>tc;
	while(tc--)
	{
		cin>>l>>x;
		cin>>st;
		tmp="";
		pair<bool, char> cur=MP(0, st[0]);
		if(x<=12)
		{
			Rep(i, x) tmp+=st;
			if(solve()) PF("Case #%d: YES\n", cas++);
			else PF("Case #%d: NO\n", cas++);
			continue;
		}
		int ind=-1;
		Rep(j, 4)
		{
			if(cur.first==0 && cur.second=='i')
			{
				ind=0;
				break;
			}
			For(i, j==0, st.size())
			{
				cur=chng(cur, st[i]);
				if(cur.first==0 && cur.second=='i')
				{
					ind=i;
					break;
				}
			}
			if(ind!=-1) break;
			x--;
		}
		if(ind==-1)
		{
			PF("Case #%d: NO\n", cas++);
			continue;
		}
		///////// j
		ind++;
		if(ind==st.size()) x--, ind=0;
		cur=MP(0, st[ind]);
		int ind2=-1;
		Rep(j, 4)
		{
			if(cur.first==0 && cur.second=='j')
			{
				ind2=ind;
				break;
			}
			For(i, ind+(j==0), st.size())
			{
				cur=chng(cur, st[i]);
				if(cur.first==0 && cur.second=='j')
				{
					ind2=i;
					break;
				}
			}
			if(ind2!=-1) break;
			x--;
			Rep(i, ind)
			{
				cur=chng(cur, st[i]);
				if(cur.first==0 && cur.second=='j')
				{
					ind2=i;
					break;
				}
			}
			if(ind2!=-1) break;
		}
		if(ind2==-1)
		{
			PF("Case #%d: NO\n", cas++);
			continue;
		}

		///////// k

		ind=ind2+1;
		if(ind==st.size()) x--, ind=0;
		cur=MP(0, st[ind]);
		For(i, ind+1, st.size()) cur=chng(cur, st[i]);
		x--;
		x%=4;

		Rep(j, x) Rep(i, st.size())
			cur=chng(cur, st[i]);
		if(cur.first==0 && cur.second=='k') PF("Case #%d: YES\n", cas++);
		else PF("Case #%d: NO\n", cas++);
	}
	return 0;
}