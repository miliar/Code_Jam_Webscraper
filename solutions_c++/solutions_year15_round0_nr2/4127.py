#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,d,p,m,k=0,mn,it,tp;
    scanf("%d",&t);
    while(t--)
    {
        m=0;it=1;mn=0;
        priority_queue<int> pq,pr;
        scanf("%d",&d);
        for(int i=0;i<d;i++)
        {
            scanf("%d",&p);
            pq.push(p);
            pr.push(p);
        }
        m=pq.top();
        mn=m;
        while(pq.top()!=1)
        {
            tp=pq.top();
            //cout<<tp<<" ";
            pq.pop();

            {pq.push(tp/2);
            pq.push(tp-tp/2);
            }
            //if(m>=pq.top()+it)
            {
                m=pq.top()+it;
                it++;
            }
            //cout<<m<<" ";
            if(mn>m)
                mn=m;
        }
        it=1;
        m=pr.top();
        while(pr.top()!=1)
        {
            tp=pr.top();
            //cout<<tp<<" ";
            pr.pop();
            if(tp==9)
            {
                pr.push(tp/3);
            pr.push(tp-tp/3);
            }
            else
            {pr.push(tp/2);
            pr.push(tp-tp/2);
            }
            //if(m>=pr.top()+it)
            {
                m=pr.top()+it;
                it++;
            }
            //cout<<m<<" ";
            if(mn>m)
                mn=m;
        }
        printf("Case #%d: %d\n",k+1,mn);
        k++;
    }
}
