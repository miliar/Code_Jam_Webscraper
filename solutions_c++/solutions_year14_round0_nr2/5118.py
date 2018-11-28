#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int T;
    float c,f,x,min,ctemp,temp,t;
    cin>>T;
    for(int m=1;m<=T;m++)
    {
        cin>>c>>f>>x;
        //printf("%.7f")
        t=2;
        temp=0;
        min=float(x/t);
        ctemp=c/t;
        t=t+f;
        temp=ctemp+float(x/t);
        while(temp<min)
        {
            //cout<<"Hello";
            min=temp;
            ctemp=ctemp+float(c/t);
            t=t+f;
            temp=ctemp+float(x/t);
        }
        printf("Case #%d: %.7f",m,min);
        cout<<endl;
    }
    return 0;
}
