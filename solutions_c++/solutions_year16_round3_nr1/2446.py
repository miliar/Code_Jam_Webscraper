#include<iostream>
#include<vector>
#include<string.h>
#include<math.h>
#include<fstream>
using namespace std;
int main()
{
   //ofstream cout("out1_1.in");
    ofstream cout("out2.in");
    ifstream cin("A-large.in");
    long long int t,i,j,k,sum,mini,n;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        int a[n];
        long int count=0;
        for(j=0;j<n;j++)
        {
            cin>>a[j];
            count+=a[j];
        }
        cout<<"Case #"<<i<<": ";
        while(count)
        {
        long int max1=0,max2=0;
        long int mxi,mxj;
        int f1=0,f2=0;
        for(j=0;j<n;j++)
        {
            if(a[j]>max1 && a[j]!=0)
                {
                    max1=a[j];
                    mxi=j;
                    f1=1;
                }
        }
        if(f1==1)
        {
         //   cout<<max1<<" ";
            a[mxi]-=1;
            count--;
         char c1=char(65+mxi);
            cout<<c1;
        }
        long int max=0,tell=0;
        for(j=0;j<n;j++)
        {
            if(a[j]>=max)
                max=a[j];
        }
           for(j=0;j<n;j++)
        {
            if(a[j]==max)
                tell++;
        }
        int f3=0;
        if(tell%2==0)
            f3=1;
         for(j=0;j<n;j++)
        {
            if(a[j]>=max2 && a[j]!=0)
                {
                    if(f3==1)
                    {
                      if(a[j]==max2 && mxi!=j )
                    {
                        max2=a[j];
                        mxj=j;
                        f2=1;
                    }
                    }
                    else
                    {
                        max2=a[j];
                        mxj=j;
                        f2=1;
                    }
                }
        }
        if(f2==1)
        {
            a[mxj]-=1;
          //  cout<<max2<<endl;
            count--;
            char c2=char(mxj+65);
            cout<<c2;
        }
         cout<<" ";
        }
    cout<<endl;
    }
    return 0;
}
