#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        long long n,m=1,k=0,temp,p,s=0;
        cin>>n;
        if(n==0)
            cout<<"Case #"<<j<<":"<<" INSOMNIA"<<endl;
        else
        {
        int a[10];
        for(int i=0;i<10;i++)
            a[i]=0;
        for(int i=1;;i++)
        {
                s=0;
                p=n*i;
                temp=p;
                while(temp)
                {
                    k=temp%10;
                    a[k]++;
                    temp=temp/10;
                }
            for(int q=0;q<10;q++)
            {
                if(a[q]>=1)
                    s++;
            }
            if(s>=10)
                break;
        }
        cout<<"Case #"<<j<<":"<<" "<<p<<endl;
        }
    }
	return 0;
}
