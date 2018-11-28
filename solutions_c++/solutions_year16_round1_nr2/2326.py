#include<stdio.h>
#include<iostream>
#include<stdlib.h>

using namespace std;


int main()
{
    int t,z=0;
    cin>>t;
    while(t--)
    {
        z++;
        int a[2501] = {0};
        //int b[2501]={0};
        int n,i,temp,j,k;
        cin>>n;
        j = n;
        n = ((n*2) - 1);
        for(i=1;i<=n;i++)
        {
            for(k = 0;k<j;k++)
            {
                cin>>temp;
                a[temp]++;
            }

        }
        cout<<"Case #"<<z<<":";
        for(i=1;i<2501;i++)
        {
            if(a[i]%2!=0)
                cout<<" "<<i;
        }
        cout<<"\n";

    }
}
