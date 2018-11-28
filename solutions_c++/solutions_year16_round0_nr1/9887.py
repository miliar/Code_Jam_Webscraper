#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
int t,a[20];
cin>>t;

    for(int k=1;k<=t;k++)
    {
       int j;
        for(j=0;j<=9;j++) a[j]=0;

        long long int n,m,x,i=1;

        cin>>n;
        while(true)
        {
            m=i*n;
            if(m==0) break;
            while(m)
            {
                x=m%10;
                a[x]=1;
                m/=10;
            }
            j=0;
            while(j<=9)
            {
               if(a[j]==1) j++;
               else break;
            }


            if(j==10) break;
            else i++;

        }
         if(i*n==0) {cout<<"Case #"<<k<<": INSOMNIA"<<endl; continue;}
        cout<<"Case #"<<k<<": "<<i*n<<endl;
    }

return 0;
}
