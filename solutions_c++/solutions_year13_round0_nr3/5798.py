#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<map>
#include<queue>
#include<set>
using namespace std;
typedef long long LL;
#define For(i,a,n) for((i)=(a);(i)<=(n);(i)+=1)
#define refresh(a) memset((a),0,sizeof(a))
#define IN_S(x) scanf("%s",(x))
#define P_S(x) printf("%s\n",x)
#define IN_D(x) scanf("%d",&(x))
#define P_D(x) printf("%d\n",x)
#define IN_F(x) scanf("%lf",&(x))
#define P_F(x) printf("%lf\n",x)
#define IN_L(x) scanf("%lld",&(x))
#define P_L(x) printf("%lld\n",x)
#define P_NL printf("\n")
#define read() freopen("C-small-attempt0.in","r",stdin)
#define write() freopen("C-small.out","w",stdout)
#define INF 1000000
#define mod 1000000007
#define maxn 1000009
vector<LL> sq_palin;

bool is_palindrome(LL n)
{
    LL temp=n,dig=0,d,rev_num;
    char rev[30];
    while(temp>0)
    {
        d=temp%10;
        temp/=10;
        rev[dig]=(char)(d+48);
        dig++;
    }
    rev[dig]='\0';
    for(LL i=0;i<dig;i++)
        if(rev[i]!=rev[dig-i-1])
            return false;
    return true;
}

void compute_palins()
{
    int i;
    For(i,0,3)
        sq_palin.push_back(i*i);

    for(i=11;i<maxn;i++)
    {
        if(is_palindrome(i))
            if(is_palindrome((LL)(LL)i*(LL)i))
                sq_palin.push_back((LL)i*(LL)i);
    }
}

int main()
{
    read();write();
	LL cases,n,i,a,b,ans,j;
	compute_palins();
	IN_L(cases);
	For(j,1,cases)
	{
        ans=0;
	    IN_L(a),IN_L(b);
        for(i=1;i<sq_palin.size();i++)
            if(sq_palin[i]>=a && sq_palin[i]<=b)
                ans++;
        printf("Case #%lld: %lld\n",j,ans);
	}
	return 0;
}
