#include<bits/stdc++.h>
#define mp make_pair
#define f first
#define s second
using namespace std;
int x[30];
int max_p,P;
main()
{
    freopen("A.txt","w",stdout);
    int T,t,N,i,countt,c;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        printf("Case #%d:",t);
        scanf("%d",&N);
        priority_queue<pair<int,int> > Q;
        max_p=-1;
        countt=0;
        for(i=0;i<N;i++)
        {
            scanf("%d",&x[i]);
            countt+=x[i];
            Q.push(mp(x[i],-i));
//            if(max_p<x[i])
//            {
//                max_p=x[i];
//                P=i;
//            }
        }
        c=0;
        if(countt%2)
        {
            P=-Q.top().s;
            printf(" %c",P+'A');
            Q.pop();
            x[P]--;
            if(x[P]>0)
                Q.push(mp(x[P],-P));
        }
        while(!Q.empty())
        {
            P=-Q.top().s;
            Q.pop();
            x[P]--;
                if(c==0)
                {
                    printf(" %c",P+'A');
                    c=1;
                }
                else
                {
                    printf("%c",P+'A');
                    c=0;
                }
            if(x[P]>0)
                Q.push(mp(x[P],-P));
        }
        printf("\n");
    }
}
