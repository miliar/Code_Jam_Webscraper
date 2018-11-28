#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    int T,size,i=0;
    cin>>T;
    while(T--)
    {
        i++;
        char S[100];
        int count=0;
        cin>>S;
        size = strlen(S);
        for(int i=1;i<size;i++)
        {
           if(S[i-1]!=S[i])
                count++;
        }
        if(S[size-1]=='-')
            count++;
        cout<<"Case #"<<i<<": "<<count<<"\n";

    }
    return 0;
}
