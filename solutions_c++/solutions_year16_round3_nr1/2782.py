#include<stdio.h>
#include<iostream>
#include<vector>
#include<stack>
#include<utility>//pair
#include<functional>//greater
#include<queue>
#include<string.h>
#include<algorithm>
#include<math.h>
#define mod 1000000007//10^9+7
#define pp(a,b) make_pair(a,b)
/*#include<fstream>
ifstream fin("in.txt");
ofstream fout("out.txt");*/
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<long long,long long> pll;
priority_queue< pii, vector<pii> > pq;
int main()
{
    int t,n,tc=1;
    int p[27],s;
    scanf("%d",&t);
    pii x,y;
    char c1,c2;
    while(t--)
    {
        scanf("%d",&n);
        s=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&p[i]);
            pq.push(pp(p[i],i));
            s+=p[i];
        }
        printf("Case #%d: ",tc);tc++;
        while(s&&!(pq.empty()))
        {
            x=pq.top();
            pq.pop();
            y=pq.top();
            if(x.first-y.first>=2)
            {
                if(x.first>=2)
                {printf("%c%c ",x.second+65,x.second+65);
                x.first-=2;
                if(x.first>=1)
                pq.push(x);s-=2;}
                else if(x.first==1)
                {
                    printf("%c ",x.second+65);
                    x.first-=1;
                    s-=1;
                }
            }
            else
            {
                if(y.first>1&&!pq.empty())
                {pq.pop();
                printf("%c%c ",x.second+65,y.second+65);
                x.first-=1;
                y.first-=1;
                if(x.first>=1)
                pq.push(x);
                if(y.first>=1)
                pq.push(y);
                s-=2;}
                else
                {
                    if(x.first>1)
                        {
                            pq.pop();printf("%c%c ",x.second+65,y.second+65);;x.first-=1;pq.push(x);s-=2;}
                    else
                    {
                        if(s==2)
                            {printf("%c%c ",x.second+65,y.second+65);s-=2;pq.pop();}
                        else
                        {printf("%c ",x.second+65);s-=1;}
                    }
                }

            }

        }
        printf("\n");
        while(!pq.empty())
            pq.pop();
    }
    return 0;
}


