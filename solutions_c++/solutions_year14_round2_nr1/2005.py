#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <memory.h>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#pragma comment(linker,"/STACK:16777216")
 
using namespace std;
 
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define MEM(a,b) memset((a),(b),sizeof(a))
#define N 100010
#define inf 1000000000
#define pi 2*acos(0.0)
#define eps 1e-9
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sz(x) int((x).size())
#define mp(a,b) make_pair((a), (b))
#define FREOPEN(a,b) freopen(a,"r",stdin); freopen(b,"w",stdout);
 
typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;


string s[222],p[222];
int Solve(string a,string b)
{
	int res=0,i=0,j=0;
	string c="";
	while(i < sz(a) || j < sz(b))
	{
		if(j == sz(b))i++,res++; else
		if(i == sz(a))j++,res++; else
		{
			if(a[i] == b[j])
			{
				i++;
				j++;
			} else
			{
				res++;
				if(a[i] == a[i-1])i++; else 
					              j++;
			}
		}
	}
	return res;
}
/*
aaabbb
ab
aabb
*/
int main()
{
    FREOPEN("input.txt","output.txt");
	int n,test,ans;
	set<string> st;
	scanf("%d",&test);
	rep(t,test)
	{
		ans=0;
		st.clear();
		scanf("%d",&n);
		rep(i,n)cin >> s[i];
	
		rep(i,n)
		{
			p[i]="";
			fe(j,s[i])
				if(!j)p[i]+=s[i][j]; else
				if(s[i][j] != s[i][j-1])p[i]+=s[i][j];
			st.insert(p[i]);
		}
		
		if(st.size() > 1)printf("Case #%d: Fegla Won\n",t+1,ans); else
		{
			ans=inf;
			int res=0;
			rep(j,n)res+=Solve(p[j],s[j]);
			ans=min(ans,res);
			rep(i,n)
			{
				int res=0;
				rep(j,n)res+=Solve(s[i],s[j]);
				ans=min(ans,res);
			}
			printf("Case #%d: %d\n",t+1,ans);
		}
			
	}
	return 0;   
}
/*
abcc
aabc
abbc
*/