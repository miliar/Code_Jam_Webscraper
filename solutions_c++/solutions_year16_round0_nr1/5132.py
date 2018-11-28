#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("large.in","r",stdin);
    freopen("output.in","w",stdout);
    long long int N,t,temp,l,rem,ctr=0,no=0; cin >> t;
    int a[10]={};
    while(t--)
    {   no++;
        cin>>N; l=N;
    if(N==0) {cout<<"Case #"<<no<<": INSOMNIA\n"; continue;}
    for(int i=1;;i++)
    {   N=l;
        N=N*i;
        temp=N;
        while(temp!=0)
        {
            rem=temp%10; temp=temp/10;
            a[rem]=1;
        }
        for(int j=0;j<10;j++)
        {
            if(a[j]==1) ctr++;
        }
        if(ctr==10) break;
    ctr=0;
    }
    if(ctr==10) cout<<"Case #"<<no<<": "<<N<<"\n";
    for(int i=0;i<10;i++) a[i]=0;
    }
    return 0;
}
