#include<iostream>
#include<stdio.h>
#include<math.h>
#define Max 1001
using namespace std;
typedef long long int llint;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outfile.txt","w",stdout);
    llint ans1, ans2, ar[Max], grtfall, eat;
    long double rate, auxeat;
    int t, N, i;
    scanf("%d", &t);
    for(int tcase=1;tcase<=t;tcase++)
    {
        ans1=ans2=grtfall=rate=0;
        scanf("%d", &N);
        for(i=0;i<N;i++)
            scanf("%lld", &ar[i]);
        for(i=0;i<N-1;i++)
        {
            if(ar[i]>ar[i+1])
            {
                ans1+=ar[i]-ar[i+1];
                if(grtfall<ar[i]-ar[i+1])
                    grtfall=ar[i]-ar[i+1];
            }
        }
        //rate = 1 + ((grtfall - 1) / 10);
        rate=grtfall/10.0;
        /*cout<<"Array is "<<endl;
        for(i=0;i<N;i++)
            cout<<ar[i]<<" ";
        cout<<endl;*/
        auxeat=rate*10;
        eat=auxeat;
        //cout<<"eat = "<<rate<<" * "<<10<<" = "<<eat<<endl;
        for(i=0;i<N-1;i++)
            if(ar[i]<=eat)
                {
                    //cout<<ar[i]<<" <= "<<eat<<endl;
                    //cout<<"adding "<<ar[i]<<endl;
                    ans2+=ar[i];
                    //cout<<"ans2= "<<ans2<<endl;
                }
            else
                {
                    //cout<<ar[i]<<" > "<<eat<<endl;
                    //cout<<"adding "<<eat<<endl;
                    ans2+=eat;
                    //cout<<"ans2= "<<ans2<<endl;
                }
        //ans2+=ar[N-2]-ar[N-1];
        printf("Case #%d: %lld %lld", tcase, ans1, ans2);
        printf("\n");
    }
}

//freopen("C-small-attempt9.in","r",stdin);
//freopen("dijioutfile.txt","w",stdout);
