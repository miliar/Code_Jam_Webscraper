

#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
using namespace std;



int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w",stdout);

    int t,T;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        int a;
        cin>>a;
        getchar();
        char b[a+1];
        gets(b);
        int x=atoi(b);
        int arr[a+1];
        for(int i=a;i>=0;i--)
        {
            arr[i]=x%10;
            x=x/10;
        }



        int count=0,flag=arr[0];
        for(int i=1;i<=a;i++)
        {
            if(flag>=i) flag=flag+arr[i];
            else
            {
                count=count+(i-flag);
                flag=flag+arr[i]+(i-flag);
            }


        }
        cout<<"Case #"<<t<<": "<<count<<endl;
    }
    return 0;
}


