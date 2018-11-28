#include<iostream>
#include<map>
#include<fstream>
#include<vector>
#include<cstdlib>
#include<list>
#include<cstdio>
#include<queue>
#define L long long int
#define LD long double

using namespace std;

L cal(L d, L n)
{
    L a=d*n;
    L b=(d*(d+1))/2;
    return a-b;
}

struct node
{
    int p;
    int n;
};

int main()
{
    ifstream cin("input");
    ofstream cout("output");
    
    int t,k;
    L mxa,ma,i,j,o,e,p,n,m;
    cin>>t;

    for(k=1;k<=t;k++)
    {
        cin>>n>>m;
        L c[n+1],u[n+1];
        for(i=0;i<=n;i++)
        {
            c[i]=u[i]=0;
        }
        mxa=0;
        for(i=0;i<m;i++)
        {
            cin>>o>>e>>p;
            c[o]+=p;
            u[e]+=p;
            mxa+=(cal(e-o,n)*p);
        }

        priority_queue<L> pq;
        ma=0;
        for(i=1;i<=n;i++)
        {
            for(j=0;j<c[i];j++)
            {
                pq.push(i); 
            }
            for(j=0;j<u[i];j++)
            {
                ma+=cal(i-pq.top(),n);
                pq.pop();
            }
        }
        //cout<<mxa<<" "<<ma<<" ";
        //cout<<mxa-ma<<"\n";
        cout<<"Case #"<<k<<": "<<mxa-ma<<"\n";
      }

      return 0;
}
