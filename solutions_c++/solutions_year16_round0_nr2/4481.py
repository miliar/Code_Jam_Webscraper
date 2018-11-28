#include<iostream>
#include<stdio.h>
#include<stdlib.h>

#include <fstream>
#include <string.h>
using namespace std;
int main()
{
    int t,x=0;
    cin>>t;

    while(t--)
    {
        x++;
        char a[101];
        cin>>a;
        int i,size,count = 0;
        size = strlen(a);
        for(i=0;i<size-1;i++)
        {
            if(a[i]!=a[i+1])
                count++;

        }
        if(a[size-1]=='-')
            count++;
        cout<<"Case #"<<x<<": "<<count<<"\n";


    }
}
