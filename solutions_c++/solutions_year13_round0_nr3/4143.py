#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);



long long AR[100],pi=0;
int get(long long n)
{
    int i,ret=0;
    for(i=0;i<pi;i++)
    {
        if(AR[i]<=n) ret++;
    }
    return ret;
}




int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);




    int T,cs;
    char in[100];
    int ans=0,i,n,j;



    for(j=1;j<=10000000;j++)
    {
        long long J=j;

        sprintf(in,"%lld",J*J);

        n=strlen(in);


        int ok1=1,ok2=1;
        for(i=0;i<n;i++)
        {
            if(in[i]!=in[n-i-1]) ok1=0;
        }


        if(ok1)
        {
            sprintf(in,"%lld",J);

            n=strlen(in);
            for(i=0;i<n;i++)
            {
                if(in[i]!=in[n-i-1]) ok2=0;
            }


            if(ok2)
            {
           //     cout<<J<<endl;
                AR[pi++]=J*J;
            }
        }




    }




    scanf("%d",&T);




    for(cs=1;cs<=T;cs++)
    {
        printf("Case #%d: ",cs);
        long long A,B;


        scanf("%lld %lld",&A,&B);


        printf("%d\n",get(B)-get(A-1));

    }

    return 0;
}
