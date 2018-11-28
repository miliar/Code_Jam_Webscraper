#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long i,j,k,n,t,m,count,d;
    string a;
    freopen("B-large.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>a;
        k=a.size();
        //cout<<k<<endl;
        n=0;
        count=0;
        while(count!=k){

        count=0;
        string b;
        j=0;
        d=0;
            if(a[0]=='+'){
                while(a[j]=='+')
            {
                b+='-';
                j++;
                d++;
            }
            if(d==k){
                count=d;
                n--;
            }
            }
            else
            {

            while(a[j]=='-')
            {
                b+='+';
                j++;
            }
            }
         for(;j<k;j++)
            b+=a[j];
        a=b;
        for(m=0;m<k;m++)
        {
            if(a[m]=='+')
                count++;
        }
        n++;

    }
    printf("Case #%lld: %lld\n",i,n);
    }



}
