#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,x,c,r,n=1;
    cin>>t;
    while(t--)
    {
        cin>>x>>r>>c;
        if((r%x==0&&c>=x-1)||(c%x==0&&r>=x-1))
           printf("Case #%d: GABRIEL\n",n++);
        else
           printf("Case #%d: RICHARD\n",n++);

    }
    return 0;
}
