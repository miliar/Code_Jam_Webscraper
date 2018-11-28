#include<bits/stdc++.h>
using namespace std;
int ar[11];

int main()
{

    int t,t1,i,j;
    cin>>t;


    for(t1=1;t1<=t;t1++)
    {

   cin>>i;

        for(j=0;j<10;j++)
        ar[j]=0;

        for(j=1;j<1000;j++)
        {

                int num=j*i;

        while(num>0)
        {
            int rem=num%10;
            ar[rem]=1;
            num/=10;

        }

        int j1;
        for(j1=0;j1<10;j1++)
        {
            if(ar[j1]==0)
            break;


        }

        if(j1==10)
        break;

        }
         cout<<"Case #"<<t1<<":  ";

        if(j==1000)
        cout<<"INSOMNIA"<<endl;
    else
       cout<<i*j<<endl;


    }

    return 0;
}
