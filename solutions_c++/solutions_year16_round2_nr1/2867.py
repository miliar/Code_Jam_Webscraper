
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>

#define ip freopen("in.txt","r",stdin)
#define op freopen("out.txt","w",stdout)
#define SET(a) memset(a,-1,sizeof a)
#define CLR(a) memset(a,0,sizeof a)
#define pb push_back
#define mp make_pair

#define max(a,b) ((a>b)?a:b)
#define min(a,b) ((a<b)?a:b)
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define MAX(a) (*max_element(all(a)))
#define MIN(a) (*min_element(all(a)))
#define LB(a,x) (lower_bound(all(a),x)-a.begin())
#define UB(a,x) (upper_bound(all(a),x)-a.begin())
#define countbit(x) __builtin_popcount(x)

#define pi acos(-1)
#define M 1000007
#define I (1<<30)
#define MD 100000007
#define eps 1e-7
typedef unsigned long long ull;
typedef long long ll;
typedef pair<int, int> ii;
ll GCD (ll a, ll b) {return (b==0?a:GCD(b,a%b));}
ll LCM (ll a, ll b) {return ((a*b)/GCD(a,b)); }
ll BMOD(ll a,ll b,ll m){if(b==0)return 1;ll x=BMOD(a,b/2,m);x=(x*x)%m;if(b%2==1)x=(x*a)%m;return x; }
ll POW(ll a,ll b){if(b==0)return 1;ll x=POW(a,b/2);x=(x*x);if(b%2==1)x=(x*a);return x; }
ll MINV(ll a) { return BMOD(a,MD-2,MD); }
ull next_popcount(ull a) { ull b=(a&-a); ull c=a+b; return ((((c^a)>>2)/b)|c); }

struct pt
{
	int x,y;
};
//bool cmp(pair < int , int > a, pair < int, int > b){ return a.second < b.second;}

int main()
{
    ip;
    op;
	int i,j,k,T,K,l;
	char str[2100];
	int cnt[30],digit[15];
	cin>>T;
	getchar();
	for(K=1;K<=T;K++)
	{
	    CLR(str); CLR(cnt); CLR(digit);
	    scanf("%s",&str);
	    l=strlen(str);
	    for(i=0;i<l;i++)
        {
            k=str[i]-64;
            cnt[k]++;
        }
	    k='Z'-64;
	    j=cnt[k];
        digit[0]=j;
        cnt[('Z'-64)]-=j; cnt[('E'-64)]-=j; cnt[('R'-64)]-=j; cnt[('O'-64)]-=j;

        k='W'-64;
	    j=cnt[k];
        digit[2]=j;
        cnt[('T'-64)]-=j; cnt[('W'-64)]-=j; cnt[('O'-64)]-=j;

        k='U'-64;
	    j=cnt[k];
        digit[4]=j;
        cnt[('F'-64)]-=j; cnt[('O'-64)]-=j; cnt[('U'-64)]-=j; cnt[('R'-64)]-=j;

        k='F'-64;
	    j=cnt[k];
        digit[5]=j;
        cnt[('F'-64)]-=j; cnt[('I'-64)]-=j; cnt[('V'-64)]-=j; cnt[('E'-64)]-=j;

        k='V'-64;
	    j=cnt[k];
        digit[7]=j;
        cnt[('S'-64)]-=j; cnt[('E'-64)]-=j; cnt[('V'-64)]-=j; cnt[('E'-64)]-=j; cnt[('N'-64)]-=j;

        k='X'-64;
	    j=cnt[k];
        digit[6]=j;
        cnt[('S'-64)]-=j; cnt[('I'-64)]-=j; cnt[('X'-64)]-=j;

        k='O'-64;
	    j=cnt[k];
        digit[1]=j;
        cnt[('O'-64)]-=j; cnt[('N'-64)]-=j; cnt[('E'-64)]-=j;

        k='R'-64;
	    j=cnt[k];
        digit[3]=j;
        cnt[('T'-64)]-=j; cnt[('H'-64)]-=j; cnt[('R'-64)]-=j; cnt[('E'-64)]-=j; cnt[('E'-64)]-=j;

        k='H'-64;
	    j=cnt[k];
        digit[8]=j;
        cnt[('E'-64)]-=j; cnt[('I'-64)]-=j; cnt[('G'-64)]-=j; cnt[('H'-64)]-=j; cnt[('T'-64)]-=j;

        k='E'-64;
	    j=cnt[k];
        digit[9]=j;
        cnt[('N'-64)]-=j; cnt[('I'-64)]-=j; cnt[('N'-64)]-=j; cnt[('E'-64)]-=j;

		printf("Case #%d: ",K);
		for(i=0;i<=9;i++)
        {
            if(digit[i]>0)
            {
                for(j=1;j<=digit[i];j++)
                {
                    printf("%d",i);
                }
            }
        }
        printf("\n");
	}
	return 0;
}
