//Author: Tusshar Singh
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<deque>
#include<algorithm>

using namespace std;

#define mod 1000000007
#define inf 2147483647
#define ninf -2147483648
#define FOR(i,a,b) for(i=a;i<b;i++)
#define s(a) fscanf(fp,"%d",&a)
#define lls(a) fscanf("fp,%lld",&a)
#define ss(a) fscanf("fp,%s",a)
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define sp(a) printf("%s",a)
#define cp(a) printf("%c",a)
#define nline printf("\n")
#define space printf(" ")
#define ll long long

int main()
{
    int x,i,j,k,T;
    FILE *fp,*fw;
    fp=fopen("A-small-attempt.in","r");
    fw=fopen("output1.txt","w");
    s(T);
    FOR(x,1,T+1)
    {
        int t,r;
        s(r);
        s(t);
        int ans=0;
        while(1)
        {
            if(((r+1)*(r+1)-r*r)<=t)
            ans++;
            else
            break;
            t-=(r+1)*(r+1)-r*r;
            r+=2;
        }
        fprintf(fw,"Case #%d: %d\n",x,ans);
                printf("Case #%d: %d\n",x,ans);

    }
    return 0;
}
