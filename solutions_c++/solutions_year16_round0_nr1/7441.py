#include<bits/stdc++.h>

using namespace std;
int main()
{
    long long i,j,k,n,count,q,cas,t,m;
    freopen("A-large.txt","r",stdin);
    freopen("Counting Sheep output2.txt","w",stdout);
    cin>>t;
    for(cas=1;cas<=t;cas++){
    cin>>n;
    int a[10] = {0,0,0,0,0,0,0,0,0,0};
    q=1;
    k=0;
    while(k!=1){
            if(n==0){
            k=1;
            }
    m=n*q;
    j=m;
    while(j>0)
    {
        a[j%10]=1;
        j/=10;
    }
    count=0;
    for(i=0;i<10;i++)
    {
        if(a[i]==1)
        count++;
       // cout<<count<<endl;
    }
    if(count==10)
        k=1;

        q++;
    }
    if(m==0)
    printf("Case #%lld: INSOMNIA\n",cas,m);
    else
    printf("Case #%lld: %lld\n",cas,m);
    }
    return 0;

}
