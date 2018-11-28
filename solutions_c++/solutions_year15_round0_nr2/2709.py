#include<iostream>
#include<stdio.h>
#include<set>
using namespace std;
int a[10000];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,n;
    int sMax;
    cin>>t;
    for(i=0;i<t;++i)
    {
        cin>>n;
        for(j=0;j<n;++j)
            cin>>a[j];
        int mi = 1000000;
        for(j=1;j<2000;++j)
        {
            int count=j;
            for(int x=0;x<n;++x)
            {
                count += (a[x]-1)/j;
            }
            if(count<mi)
                mi=count;
        }
        cout<<"Case #"<<i+1<<": "<<mi<<endl;
    }
}

