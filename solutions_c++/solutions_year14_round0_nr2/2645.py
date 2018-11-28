#include<iostream>
#include<stdio.h>

using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        double C,F,X;
        cin>>C>>F>>X;
        double time=0.0,d=2.0,tmp1,tmp2;
        int ch=1;
        while(ch)
        {
            tmp1=time+X/d;
            tmp2=time+C/d+X/(d+F);
            if(tmp1<=tmp2)
            {
                time=tmp1;ch=0;
            }
            else
                {time=time+C/d;d+=F;}
        }
        printf("Case #%d: %.7lf",i+1,time);
        cout<<endl;
    }
    return 0;
}
