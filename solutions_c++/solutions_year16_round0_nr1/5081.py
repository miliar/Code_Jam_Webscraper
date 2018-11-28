#include<bits/stdc++.h>
using namespace std;
long long visited[10];
int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(false);
    long long t;
    cin>>t;
    long long k=1;
    while(t--)
    {
        long long n;
        cin>>n;
        fill(visited,visited+10,0);
        if(n==0)
        {
           cout<<"Case #"<<k<<":"<<" "<<"INSOMNIA"<<"\n";
        }
        else
        {
            long long c=0;
            long long h=n;
            while(true)
            {
                long long orig=h;
                long long rem;
                while(orig>0)
                {
                    rem=orig%10;
                    if(visited[rem]==0)
                    {
                        visited[rem]=1;
                        c++;
                    }
                    orig=orig/10;
                }
                if(c==10)
                    break;
                h=h+n;
            }
            cout<<"Case #"<<k<<":"<<" "<<h<<"\n";
        }
        k++;
    }
}
