#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <memory.h>
#include <bitset>
#include <time.h>
#define sf(x) scanf("%d", &x)
#define sff(x) scanf("%lf", &x)
#define sfc(x) scanf(" %c", &x)
#define pf(x) printf("%d ", x)
#define pff(x) printf("%lf", x)
#define pfc(x) printf("%c", x)
#define pfs(x) printf("%s", x)
#define sfl(x) scanf("%I64d", &x)
#define sfl2(x,y) scanf("%I64d %I64d", &x,&y)
#define ENDL printf("\n")
#define INF 2147483647
#define pf2(x,y) printf("%d %d ", x,y)
#define sf2(x,y) scanf("%d %d", &x,&y)
#define pb(x) push_back(x)
#define ppb() pop_back()
#define mp(x,y) make_pair(x,y)
#define sf3(x,y,z) scanf("%d %d %d", &x,&y,&z)
#define print(x) puts(#x)
#define error(x) cerr<<#x<<' '<<x<<'\n'


using namespace std;

typedef long long ll; 
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef vector<int> vec;


string s1,s2;
int nn;
int k,l,s;
int res;
int mx;

void foo(string S)
{
	if(S.size()==s)
	{
		int tmp=0;
		for(int i=0; i<=s-l; i++)
		{
			bool f=0;
			for(int j=0; j<l; j++)
			{
				if(S[i+j]!=s2[j])
				{
					f=1;
					break;
				}
			}
			if(!f) tmp++;
		}
//		cout<<S<<' '<<tmp<<endl;
		mx=max(mx,tmp);
		res+=tmp;
		return;
	}
	for(int i=0; i<k; i++)
	{
		foo(S+s1[i]);
	}
}

int main()
{
    
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    /**/
    
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	sf3(k,l,s);
    	cin>>s1>>s2;
    	nn=1;
    	for(int i=0; i<s; i++)
    	{
    		nn*=k;
    	}
    	res=0;
    	string S;
    	mx=0;
    	foo(S);
    	double qwe=res*1.0/nn;
    	printf("Case #%d: %.10lf\n",t,mx-qwe);
    	
    	
    }
    return 0;
}








