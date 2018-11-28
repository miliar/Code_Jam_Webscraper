#include <iostream>
#include<stdint.h>
#include<stdio.h>
using namespace std;

int main() {
    long int t,te=0;
    cin>>t;
    do
    {
        uint64_t n,nact;
        cin>>n;
        nact=n;
        cout<<"Case #"<<te+1<<": ";
        int A[10],i,flag=0;
        for (i=0;i<10;i++)
        A[i]=0;
        if (n==0) cout<<"INSOMNIA"<<endl;
        else
        {
        while(flag==0)
        {
            uint64_t n1=n;
            while(n1>0)
            {
                int r=n1%10;
                n1/=10;
                A[r]++;
            }
            int count=0;
            i=0;
            for (i=0;i<10 && count==i;i++)
            {
                if (A[i]!=0) count++;
            }
            if (count==10) {flag=1;cout<<n<<endl;}
             n+=nact;
        }
        }
        te++;
    }
    while(te<t);
	return 0;
}
