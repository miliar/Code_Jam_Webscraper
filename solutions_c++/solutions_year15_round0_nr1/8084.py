#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define F(i,a,b) for(int i = (int)(a); i <= (int)(b); i++)
#define RF(i,a,b) for(int i = (int)(a); i >= (int)(b); i--)
#define MOD 1000000007
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-output.txt","w",stdout);
    int T,Smax,reqF,sF;
    char S[1005];
    scanf("%d",&T);
    F(t,1,T)
    {
        scanf("%d%s",&Smax,S);
        reqF = 0;
        sF = S[0] - '0';
        F(i,1,Smax)
        {
            if(sF >= i)
            {
                sF += (S[i] - '0');
            }
            else
            {
                reqF += (i-sF);
                sF = i + (S[i]-'0');
            }
        }
        printf("Case #%d: %d\n",t,reqF);
    }
    return 0;
}

