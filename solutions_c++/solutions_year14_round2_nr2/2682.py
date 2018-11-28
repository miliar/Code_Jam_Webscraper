#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    FILE *f;
    long long int i,j,a,b,k,n,t,m,c,l;
    f=fopen("output","a");
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>a>>b>>n;
        c=0;
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                m=i&j;
                for(l=0;l<n;l++)
                    if(m==l)
                    { c++; break; }
            }
        }
        fprintf(f,"Case #%lld: %lld\n",k,c);
    }
    fclose(f);
    return 0;
}
