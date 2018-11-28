#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
bool wayToSort(int i, int j) { return i > j; }
int main()
{
    long long t,n;
    cin>>t;
    for(long long x=1;x<=t;x++)
    {   long na=0,nd=0;
        cin>>n;
        double a[n],b[n],a1[n],b1[n];
        for(long long y=0;y<n;y++)
        {
            cin>>a[y];
            a1[y]=a[y];
        }
        for(long long y=0;y<n;y++)
        {
            cin>>b[y];
            b1[y]=b[y];
        }
        sort(a,a+n);
        sort(b,b+n);
        //WAR
        for(long long y=0;y<n;y++)
        {
            for(long long z=0;z<n;z++)
            {
                if(a[y]<b[z])
                {
                    a[y]=0;

                    b[z]=0;
                    na++;

                    break;
                }


            }
            if(a[y]!=0)
                {

                    break;
                }
        }
        //cout<<(n-na)<<endl;
        //DWAR

        sort(b1,b1+n,wayToSort);
        sort(a1,a1+n);
        for(long long y=0;y<n;y++)
        {
            for(long long z=0;z<n;z++)
            {
                if(a1[z]>b1[y])
                {   a1[z]=0;
                    b1[y]=0;
                    nd++;
                    break;
                }
            }

        }
        cout<<"Case #"<<x<<": "<<nd<<" "<<n-na<<endl;
    }
}
