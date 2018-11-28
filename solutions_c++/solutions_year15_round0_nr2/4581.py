#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<iostream>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<cmath>
#include<queue>
#include<stack>
#include<deque>
#define INF 0x7fffffff


using namespace std;

typedef pair<int,int> ii;
typedef set<int> si;
typedef map<string, int> msi;
typedef priority_queue<int> pqi;


pqi rpq;
int result;

void solve(pqi pq, int q)
{
    int x = pq.top();
    //printf("%d\n",x);
    result = min(q+x,result);

        if(q==x || x <=3)
            return;
        pq.pop();
        for(int i=2; i<x/2+1; i++)
        {
            pqi auxpq(pq);
            auxpq.push(x-i);
            auxpq.push(i);
            solve(auxpq, q+1);
            //if(result>-1)return;
        }


}

int main()
{

    int cases =1;
    int t;
    while(cin >> t)
    {
        while(t--)
        {
            result = INF;
            int n;
            scanf("%d", &n);
            pqi pq;
            while(n--)
            {
                int a;
                scanf("%d",&a);


                pq.push(a);
            }

            solve(pq,0);
            printf("Case #%d: %d\n", cases++, result);

        }
    }

    return 0;
}
