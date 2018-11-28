#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int cases=1;cases<=t;cases++)
    {
        int n,x,sum=0;
        priority_queue<pair<int,int> > pqp;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&x);
            sum+=x;
            pqp.push(make_pair(x,i));
        }

        printf("Case #%d:",cases);
        if(sum%2==1)
        {
           pair<int,int> tmp = pqp.top();
             pqp.pop();
             printf(" %c",tmp.second+'A');
             tmp.first--;
             if(tmp.first !=0 )
                pqp.push(tmp);
        }
        while(!pqp.empty())
        {
             pair<int,int> tmp = pqp.top();
             pqp.pop();
             printf(" %c",tmp.second+'A');
             tmp.first--;
             if(tmp.first !=0 )
                pqp.push(tmp);
            if(pqp.empty())
                break;
             tmp = pqp.top();
             pqp.pop();
             printf("%c",tmp.second+'A');
             tmp.first--;
             if(tmp.first !=0 )
                pqp.push(tmp);
        }
        printf("\n");

    }

    return 0;
}
