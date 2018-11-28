#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n,i;
    int t;
     ofstream out("output.txt");
    ifstream in("input.txt");
    in>>t;
    int T=1;

    while(t--)
    {
            in>>n;
    pair<int,int>a[n];
    int sum=0;
    for(i=0;i<n;i++)
    {
        in>>a[i].first;
        a[i].second=i;
        sum+=a[i].first;
    }
    sort(a,a+n);
    out<<"Case #"<<T++<<": ";
     if(sum%2==1)
    {
        out<<char(a[n-1].second+65)<<" ";
        sum--;
        a[n-1].first--;
    }
    for(i=n-1;i>0 && sum>0;)
    {
        if(a[i].first!=0 && a[i-1].first!=0 )
        {
            out<<char(a[i].second+65)<<char(a[i-1].second+65)<<" ";
            a[i].first--;
            a[i-1].first--;
            sum=sum-2;
             sort(a,a+n);
        }
        else
        {
            i--;
        }

    }
    out<<"\n";

    }
}
