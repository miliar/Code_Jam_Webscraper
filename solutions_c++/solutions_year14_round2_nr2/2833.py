

#include<iostream>
#include<cstdio>
#include <iomanip>
#include<algorithm>
#include<string>
using namespace std;


int main()
{
    int t,l,n,m,i,j,case_c=0,a,b,k;
    int *p,*q,*r;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        case_c++;
        cin>>a>>b>>k;
        p= new int[a+2];
        q= new int[b+2];
        r= new int[(a*b)+2];
        for(i=0;i<a;i++)
            p[i]=i;
        for(j=0;j<b;j++)
            q[j]=j;
        l=0;
        for(i=0;i<a;i++)
            for(j=0;j<b;j++)
            r[l++]=p[i]&q[j];
        int countt=0;

        for(i=0;i<l;i++)
            for(j=0;j<k;j++)
                if(r[i]==j)
                    countt++;

        cout<<"Case #"<<case_c<<": "<<countt<<endl;
    }
    return 0;
}

