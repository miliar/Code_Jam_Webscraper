#include<bits/stdc++.h>

using namespace std;
long long a[11],h;
long long hashfor(long long n)
{
    int h, i;
    while(n>0)
    {
        h = n%10;
        a[h] = 1;
        n/=10;
    }
    for(i=0;i<10;i++)
        if(a[i]==0)
        return 0;

    return 1;
}

int main()
{
    FILE *fin = freopen("input.txt","r",stdin);
    FILE *fout = freopen("output.txt","w",stdout);
    long long n,ty,temp,temp1,j=1,t,k;
    long long flag = 0, i=2;
    cin>>t;

    while(j<=t)
    {
        i=2;
        flag=0;

        for(k=0;k<11;k++)
            a[k]=0;

    cin>>n;
    if(n==0)
    {
        cout<<"Case #"<<j<<": INSOMNIA\n";
        j++;
        continue;
    }

    temp1 = hashfor(n);

    while(flag!=1)
    {
        temp=n*i;
        i++;
        ty = hashfor(temp);
        if(ty == 1)
        {
            flag=1;
        }
    }
    cout<<"Case #"<<j<<": "<<temp<<endl;
    j++;
    }
    return 0;
}
