#include <iostream>
#include<string.h>
#include<map>
#include<queue>

using namespace std;


int main(int argc, const char * argv[])
{
   freopen("/Users/sangwoo/Desktop/cpp/cpp/input","r",stdin);
   freopen("/Users/sangwoo/Desktop/cpp/cpp/output","w",stdout);
    
    int tt;
    scanf("%d",&tt);
    
    for(int t=1;t<=tt;t++)
    {
        int N;
        int P[27];
        int sum=0;
        
        priority_queue< pair<int,char> > q;
        
        scanf("%d",&N);
        
        for(int i=0;i<N;i++)
        {
            scanf("%d",&P[i]);
            q.push(make_pair(P[i],'A'+i));
            sum+=P[i];
        }
        pair<int,char> p;
        printf("Case #%d: ",t);
 
        
        while(!q.empty())
        {

            p = q.top();
            q.pop();
            p.first--;
            if(p.first!=0)
            {
                q.push(p);
            }
            printf("%c",p.second);
            sum--;
            
            if(sum<q.top().first*2)
            {
                p = q.top();
                q.pop();
                p.first--;
                if(p.first!=0)
                {
                    q.push(p);
                }
                printf("%c",p.second);
                sum--;
            }
            printf(" ");
        }
        printf("\n");
        
    }
    return 0;
}