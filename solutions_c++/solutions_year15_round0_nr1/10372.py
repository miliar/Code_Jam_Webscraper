#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
#include <ctype.h>

#define geti(a) scanf("%d",&a)
#define getli(a) scanf("%ld",&a)
#define getlli(a) scanf("%lld",&a)
#define getf(a) scanf("%f",&a)
#define getd(a) scanf("%lf",&a)
#define getst(a) scanf("%s",&a)

#define puti(a) printf("%d",a)
#define putli(a) printf("%ld",a)
#define putlli(a) printf("%lld",a)
#define putf(a) printf("%f",a)
#define putd(a) printf("%lf",a)
#define putst(a) printf("%s",a)
#define putn() printf("\n")
#define putt() printf("\t")

using namespace std;

int main()
{
    int t,input,n,length,ans,nstanding;
    int cas=1;
    char shyness[100001];
    geti(t);
    while(t--)
    {
        ans = 0;
        nstanding=0;
        geti(n);
        getst(shyness);
        length = n+1;
        for(int i=0 ; i<length ; ++i)
        {
            if(nstanding >= i && shyness[i]>'0')
                nstanding += shyness[i] - '0';
            else if(nstanding<i && shyness[i]>'0')
            {
                ans += i - nstanding;
                nstanding = i + shyness[i]-'0';
            }
        }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
        cas++;
    }
}
