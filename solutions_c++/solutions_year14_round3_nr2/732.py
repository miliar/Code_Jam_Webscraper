/*
*
* solved by Ahmed Kamal
*/
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<cstring>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<bitset>
#include<queue>
#include<utility>
#include<algorithm>
#include<functional>

using namespace std;

typedef long long int LL ;
#define vi vector<int>
#define ii pair<int,int>
#define vii vector< pair<int,int> >
#define sc(x) scanf("%d",&x)
double const EPS = 2.22045e-016;
#define INF (1<<29)

#define ALL(v)				((v).begin()), ((v).end())
#define SZ(v)				((int)((v).size()))
#define CLR(v, d)			memset(v, d, sizeof(v))
#define LOOP(i, n)		for(int i=0;i<(int)(n);++i)
#define LOOPP(i,b, n)		for(int i=(b);i<(int)(n);++i)

#define PB	push_back
typedef vector<double>    VD;
typedef vector<string>    VS;
LL gcd(LL a, LL b) { return (b == 0 ? a : gcd(b, a % b)); }

int n;
VS arr;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

int ts;sc(ts);
LOOP(t,ts){
	 sc(n);
	 arr.assign(n,"");
	 LOOP(i,n)
	  cin>>arr[i];
	vi per(n,0);
	LOOP(i,n)
    	per[i] = i;
int hash[300];
LL ans =0;
LL mod = 1000000007;
	do {
	string s="";
    LOOP(i,n)
	 s+= arr[per[i]];
    CLR(hash,0);
    bool g =true;
    hash[(int)s[0]]++;
    LOOPP(i,1,SZ(s)){
      if(!(hash[(int)s[i]] == 0 || s[i]==s[i-1])){
         g =false;
         break;
      }
     hash[(int)s[i]]++;
    }
    if(g)
    	ans++;
    if(ans > mod)
    ans %=mod ;

} while (next_permutation(ALL(per)));
	printf("Case #%d: %lld\n",t+1,ans);
}
return 0;
}
