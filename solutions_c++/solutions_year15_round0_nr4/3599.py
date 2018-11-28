#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define LD long double
#define gc getchar_unlocked
#define pc putchar_unlocked
#define MOD 1000000007
#define MAXN 2*100005
#define bitcount __builtin_popcount
#define INF 2000000000
#define EPS 1e-9

template<typename T>T absll(T X)
{
    if(X<0)
        return -1*X;
    else
        return X;
}

bool solve(int X,int R,int C)
{
    if(X==1)
	{
		return false;
	}
	else if(((R*C)%2==0)&&X==2&&(R>=2 || C>=2))
	{
		return false;
	}
	else if((X==3)&&((R*C)%3==0)&(R>=3||C>=3)&&(R>1&&C>1))
	{
		return false;
	}
	else if((X==4)&&((R*C)%4==0)&&(R>=4||C>=4)&&(R>2&&C>2))
	{
		return false;
	}
	else
	{
		return true;
	}
}
int main()
{
    freopen("input.txt","r",stdin);//redirects standard input
    freopen("output.txt","w",stdout);//redirects standard output
    int T;
    scanf("%d",&T);
    for(int test=1;test<=T;test++)
    {
        int R,X,C;
        scanf("%d %d %d",&X,&R,&C);
        printf("Case #%d: %s\n",test,solve(X,R,C)?"RICHARD":"GABRIEL");
    }
    return 0;
}
