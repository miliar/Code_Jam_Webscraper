#include<iostream>
#include<stdio.h>
using namespace std;
main()
{

    double c,f,x,var,cf,f1,cf1,i,var1,var2,t;int y=0;
    cin>>t;
    while(t--)
    {
i=0;
f1=2;
var1=0;
    cin>>c>>f>>x;
    while(1)
    {

    if(i==0)
    {
        i++;
    var=c/2;
    var1+=var;
    var2=x/2;
    cf=var2;
    cf1=cf;
    if(c>x){cf1=x/2;break;}
//cout<<cf<<"a ";
    }
    else{
            f1+=f;

        var=c/f1;
    var1+=var;
    var2=x/f1;

    cf=var1-var+var2;
//cout<<cf<<"b ";
    if(cf>cf1)break;
cf1=cf;

    }
}
printf("Case #%d: %.7lf\n",++y,cf1);    }
    return 0;
}
