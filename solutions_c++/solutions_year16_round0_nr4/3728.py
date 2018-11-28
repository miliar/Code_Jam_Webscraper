#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,k,c,s;
    long long int ans,anss;
    int TT=0;
    cin>>T;
    while(T--)
    {TT++;
        scanf("%d%d%d",&k,&c,&s);
        if(s==k)
        {
            printf("Case #%d: ",TT);
            /*if(c==1)
            {FOR(i,1,k)
                cout<<i<<" ";cout<<endl;}
                else*/
                    anss=pow(k,c-1);
            FOR(i,0,k-1)
            {
                ans=i*anss+1;
                cout<<ans<<" ";
            }
            //if(c!=1)
            cout<<endl;
        }
    }
    return 0;
}
