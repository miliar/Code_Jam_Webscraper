#include<iostream>
using namespace std;
#include<stdio.h>

/*
int main()
{
    int t,testcases;
    float C,F,X,direct,indirect,temp,original,newone;
    cin>>testcases;
    for(t=1;t<=testcases;t++)
    {
        cin>>C>>F>>X;
        direct=X/2;
        indirect=(C/2)+(X/(2+F));
        original=direct;
        newone=indirect;
        int n=1;
        while(1)
        {
            if(original<newone)
            {
                break;
            }
            direct=X/(2+n*F);
            indirect=C/(2+n*F)+X/(2+(n+1)*F);
            n++;
            temp=newone;
            newone=original+indirect-direct;
            original=temp;
        }
        cout<<"Case #"<<t<<": "<<original<<endl;

    }



    return 0;
}
*/

#define LL long

/*
int main()
{
    int t,testcases;
    double ans,C,F,X,t0,t1;
    cin>>testcases;
    for(t=1;t<=testcases;t++)
    {
        cin>>C>>F>>X;
        t0=X/2;
        t1=(C/2)+(X/(2+F));
        if(t0<t1)
        {
            cout<<"Case #"<<t<<": "<<t0<<endl;
            continue;
        }
        int n=1;
        while(C*(2+n*F)<(X*F))
        {
            n++;
        }
        ans=0;
        for(int i=0;i<n;i++)
        {
            ans+=C/(2+i*F);

        }

        ans+=X/(2+n*F);
        //ans=X/2-X/(2+n*F);
        cout<<"Case #"<<t<<": "<<ans<<endl;

    }
    return 0;


}
*/


int main()
{

    int t,testcases;
    double ans,finalans,C,F,X,t0,t1;
    cin>>testcases;
    for(t=1;t<=testcases;t++)
    {
        cin>>C>>F>>X;
        t0=X/2;
        t1=(C/2)+(X/(2+F));
        finalans=X/2;
        ans=X/2;
        for(int n=1;n<=10000;n++)
        {
            ans+=C/(2+(n-1)*F)+X/(2+(n)*F)-X/(2+(n-1)*F);
            finalans=min(ans,finalans);
        }
        cout<<"Case #"<<t<<": ";
        printf("%lf",finalans);
        cout<<endl;

    }
    return 0;


}
