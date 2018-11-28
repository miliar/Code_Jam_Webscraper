#include<iostream>
#include<stdio.h>
using namespace std;

int r,t;

int main()
{
    int tcc,tc;
    cin>>tc;
    for(tcc=1;tcc<=tc;tcc++)
    {
        cin>>r>>t;
        int x = t;
        int rings=0;
        while(1)
        {
            x = x-(2*r+1);
            if(x<0)
                break;
            r = r+2;
            rings++;
        }
        printf("Case #%d: %d\n",tcc,rings);
    }
    return 0;
}
