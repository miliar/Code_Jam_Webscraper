#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int arr[1010]={0};

void pre_fun()
{
    arr[1]=1;
    arr[4]=1;
    arr[9]=1;
    arr[121]=1;
    arr[484]=1;
}

int main()
{
    pre_fun();
    int test,a,b;
    cin>>test;

    for(int cr=0;cr<test;cr++)
    {
        cin>>a>>b;
        int ans=0;
        for(int i=a;i<=b;i++)
        {
            if(arr[i]==1)
            {
                ans++;
            }
           // cout<<ans;
                //ans++;
        }
        cout<<"Case #"<<(cr+1)<<": "<<ans<<endl;
    }
    return 0;
}
