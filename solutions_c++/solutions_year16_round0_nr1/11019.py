#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int t;
    cin>>t;
    register int k=1;
    while(k<=t)
    {
        int n;
        cin>>n;
        int r=n;
        if(n==0)
        {cout<<"Case #"<<k<<":  "<<"INSOMNIA"<<endl;
        k++;
        continue;
        }
        int a[10];
        register int i,j,p=0;
        for(i=0;i<10;i++)
        {
            a[i]=0;
        }
        j=1;
        while(p!=10)
        {
            while(n>=1)
            {
                int s=n%10;
                if(a[s]==0)
                {
                    p++;
                    a[s]=1;
                }
                n/=10;
            }
            j++;
            n=r*j;
        }
        
      cout<<"Case #"<<k<<":  "<< n-r <<endl;
		k++;
    }
}