#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int i,t,num=0;
    double C,F,X,ans,r,prev,total,current,val;

    cin>>t;

    while(t--) {

        num++;
        cin>>C>>F>>X;

        prev = total = ans = X/2.0;
        total = val = 0.0;
        r = 2.0;

        while(true) {
            r = r+F;
            current = (C/(r-F)) + (X/r);
            if( current>prev ) {
                break;
            }
            total = current + val;
            val += (C/(r-F));
            prev = X/r;
        }

        if(total==0)
           printf("Case #%d: %0.7f\n",num,(X/2.0));
        else
            printf("Case #%d: %0.7f\n",num,total);

    }
    return 0;
}
