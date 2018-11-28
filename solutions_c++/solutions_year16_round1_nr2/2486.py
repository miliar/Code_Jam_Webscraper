#include<stdio.h>
#include<iostream>
#include<stdlib.h>

using namespace std;


int main()
{
    int T,n=0;
    cin>>T;
    while(T--)
    {
        n++;
        int Hash[2501] = {0};
        //int b[2501]={0};
        int N,i,temp,j,k;
        cin>>N;
        j = N;
        N = ((N*2) - 1);
        for(i=1;i<=N;i++)
        {
            for(k = 0;k<j;k++)
            {
                cin>>temp;
                Hash[temp]++;
            }

        }
        cout<<"Case #"<<n<<":";
        for(i=1;i<2501;i++)
        {
            if(Hash[i]%2!=0)
                cout<<" "<<i;
        }
        cout<<"\n";

    }
}
