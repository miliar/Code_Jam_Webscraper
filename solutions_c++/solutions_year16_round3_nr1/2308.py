
#include <bits/stdc++.h>

#define mod 1000000007
#define inf 1000000000000
#define root2 1.41421
#define root3 1.73205
#define pi 3.14159
#define MAX 100001
#define ll long long int
#define PII pair<int, int>
#define f first
#define s second
#define mk make_pair

using namespace std;
priority_queue<PII> Q;
int main()
{
    ifstream in("A-large.in");
    ofstream out("output.txt");
    int i, t, j, k=1, n, sum;
    PII x, y, z;
    in>>t;
    while(k<=t)
    {
        out<<"Case #"<<k<<": ";
        //cout<<"Case #"<<k<<": ";
        in>>n;
        sum=0;

        while(!Q.empty())
            Q.pop();
        for(i=1;i<=n;i++)
        {
            in>>x.f;
            sum+=x.f;
            x.s=i;
            Q.push(x);
          //  cout<<x.f<<" "<<x.s<<"\n";
        }
        while(!Q.empty())
        {
            x=Q.top();
            Q.pop();
            y=Q.top();
            Q.pop();
            if(2*y.f>(sum-1))//remove x and y both
            {
                x.f-=1;
                y.f-=1;
                sum-=2;
                out<<(char)(x.s+64)<<(char)(y.s+64)<<" ";
            }
            else//remove x only
            {
                x.f-=1;
                sum-=1;
                out<<(char)(x.s+64)<<" ";
            }
            if(x.f!=0)
                Q.push(x);
            if(y.f!=0)
                Q.push(y);
        }
        out<<"\n";
        k++;
    }
}
