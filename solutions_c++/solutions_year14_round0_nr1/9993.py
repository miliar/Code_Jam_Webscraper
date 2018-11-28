#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>

#define I (1<<31)-1
#define M 1000007
#define pi acos(-1)
#define max(a,b) (a>b)?a:b
#define min(a,b) (a<b)?a:b
#define mem(a) memset(a,0,sizeof(a))
#define pb push_back
#define mp make_pair
//typedef long long int ll;
typedef pair<long int, long int> ii;
typedef vector<long int> vi;
typedef vector<ii> vii;
struct edge
{
	long int x;
	long int y;
	long int w;
	bool operator < (const edge &b)
	{
		return w<b.w;
	}
};
long int gcd (long int a, long int b) {return (b==0?a:gcd(b,a%b));}
/*
bool cmp(pair < int , int > a, pair < int, int > b)
{
    return a.second < b.second;
}
*/


int main()
{
    //freopen("Problem A. Magic Trick.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	long int i,j,k,T,K,a[6][6],b[6][6],m,n,f,ans,p;
	cin>>T;
	for(K=1;K<=T;K++)
	{
	    mem(a); mem(b); f=0; ans=0;
	    scanf("%ld",&m);
	    for(i=0;i<4;i++)
	    {
	        for(j=0;j<4;j++)
	        {
	            scanf("%ld",&a[i][j]);
	        }
	    }
	    scanf("%ld",&n);
	    for(i=0;i<4;i++)
	    {
	        for(j=0;j<4;j++)
	        {
	            scanf("%ld",&b[i][j]);
	        }
	    }
	    for(i=0;i<4;i++)
	    {
	        k=a[m-1][i];
	        for(j=0;j<4;j++)
	        {
	            p=b[n-1][j];
	            if(k==p) { f++; ans=p;}
	        }
	    }
	    if(f==0) printf("Case #%ld: Volunteer cheated!\n",K);
	    else if(f==1) printf("Case #%ld: %ld\n",K,ans);
	    else if(f>1) printf("Case #%ld: Bad magician!\n",K);
	}
	return 0;
}
