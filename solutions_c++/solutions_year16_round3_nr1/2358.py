#include <fstream>
#include<iostream>
using namespace std;
#include<math.h>
#include<algorithm>
int main()
{
    int t,n,i,c,m=1;
    pair<int,int> a[100];
    ofstream outpu;
    outpu.open("output.in");
    ifstream inpu;
    inpu.open("A-large (3).in");
    inpu>>t;
    while(t--)
    {
        inpu>>n;
        for(i=0;i<n;i++)
        {
            inpu>>a[i].first;
            a[i].second=i;
        }
        sort(a,a+n);
        c=0;
        outpu<<"Case #"<<m<<": ";
        m++;
        while(c<n)
        {
            if(a[n-1].first==1&&a[n-2].first==1&&c<n-2)
            {
                outpu<<char(a[n-1].second+65)<<" ";
                a[n-1].first--;
                c++;
                sort(a,a+n);
            }
            else if(a[n-1].first!=0&&a[n-2].first!=0)
            {
                a[n-1].first--;
                a[n-2].first--;
                if(a[n-1].first==0)
                    c++;
                if(a[n-2].first==0)
                    c++;
                outpu<<char(a[n-1].second+65)<<char(a[n-2].second + 65)<<" ";
                sort(a,a+n);
            }
        }
        outpu<<"\n";
    }
    return 0;
}
