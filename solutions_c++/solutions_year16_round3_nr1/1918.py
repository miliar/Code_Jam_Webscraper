#include<iostream>
#include<stdio.h>
#include<math.h>
#include<fstream>
#include<utility>
#include<queue>
#include<vector>
#define pp pair<int,int>
#define ll long long int
#define si(t) scanf("%d",&t)
#define sii(t,t2) scanf("%d %d",&t,&t2)

using namespace std;

int c=1;

class Prioritize
{
public:
    int operator()(const pair<int,int>& p1,const pair<int,int>& p2)
    {
        return p1.second<p2.second;
    }
};

int main()
{
    int t;
    si(t);
    while(t--)
    {
        priority_queue<pp,vector<pp>,Prioritize> q;
        int n,p,s=0;
        si(n);
        int i=0;
        while(i<n)
        {
            int k;
            si(k);
            s+=k;
            q.push(pp(i,k));
            i++;
        }
        cout<<"Case #"<<c++<<": ";
        while(!q.empty())
        {
            int a,b;
            a=q.top().first;
            b=q.top().second;
            q.pop();
            char cc;
            cc=a+'A';
            s--;
            cout<<cc;
            if(b>1)
                q.push(pp(a,b-1));
            if(!q.empty() && q.top().second>=(s/2))
            {
                a=q.top().first;
                b=q.top().second;
                q.pop();
                cc=a+'A';
                s--;
                cout<<cc;
                if(b>1)
                    q.push(pp(a,b-1));
            }
            cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}
