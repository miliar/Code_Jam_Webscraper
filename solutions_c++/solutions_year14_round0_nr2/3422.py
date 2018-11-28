#include<iostream>
#include<stdio.h>

using namespace std;
int main()
{
    int t;
    float c,f,x,min,ctemp,temp,r;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>c>>f>>x;
        
        r=2;
        temp=0;
        min=float(x/r);
        ctemp=c/r;
        r=r+f;
        temp=ctemp+float(x/r);
        while(temp<min)
        {
           
            min=temp;
            ctemp=ctemp+float(c/r);
            r=r+f;
            temp=ctemp+float(x/r);
        }
        printf("Case #%d: %.7f",i,min);
        cout<<endl;
    }
    return 0;
}
