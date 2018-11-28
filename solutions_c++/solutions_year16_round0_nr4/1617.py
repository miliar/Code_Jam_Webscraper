#include<bits/stdc++.h>
using namespace std;

long long int val,val1;
int t,k,c,s,X;

int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        X++;
        printf("Case #%d: ",X);
        scanf("%d %d %d",&k,&c,&s);

        val1=1;
        for(int i=0;i<c-1;i++)
            val1=val1*k;
        //cout<<val1<<"\n";
        val=1;
        for(int i=0;i<s;i++)
            {
                printf("%lld ",val);
                val=val+ val1;
            }
            printf("\n");
    }
    return 0;
}
