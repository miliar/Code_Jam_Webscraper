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

char str[1111];

int main()
{
    freopen("input.txt","r",stdin);//redirects standard input
    freopen("output.txt","w",stdout);//redirects standard output
    int T;
    scanf("%d",&T);
    for(int test=1;test<=T;test++)
    {
        int N;

        scanf("%d",&N);
        memset(str,'\0',sizeof(str));
        scanf("%s",str);

        vector<LL> V(N+1,0LL);

        for(int i=0;i<=N;i++)
        {
            V[i]=str[i]-'0';
        }

        LL reqd=0LL,curr=V[0];

        for(int i=1;i<=N;i++)
        {
        	if(V[i]==0)
        	{

        	}
            else if(V[i]>0)
            {
                if(i<=curr)
                {
                     curr+=V[i];
                }
                else
                {
                    //V[i-1]+=1;
                    reqd+=i-curr;
                    curr+=V[i]+reqd;
                }
            }
        }

        printf("Case #%d: %d\n",test,reqd);
    }
    return 0;
}
