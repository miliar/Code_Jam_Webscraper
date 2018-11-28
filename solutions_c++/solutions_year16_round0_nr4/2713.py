#include<bits/stdc++.h>
using namespace std;
int main()
{
    int num1,testCases,num2,num3,i,ress1,temp1;
    cin>>testCases;
    for(i=1;i<=testCases;++i)
    {
    cin>>num1>>num2>>num3;
            if(num1<=num3)
            {
            cout<<"Case #"<<i<<":";
            for(temp1=1;temp1<=num3;++temp1)
            cout<<" "<<temp1;
            cout<<endl;
            }
            else
            {
                 ress1=0;
                cout<<"Case #"<<i<<":";
                    if(num2==1)
                    cout<<" IMPOSSIBLE";
                    else
                    {
                        for(temp1=2;temp1<=num1*num1;temp1=temp1+num1+1)
                        ++ress1;
                        if(num1==2)
                        ress1=2;
                        if(ress1>num3)
                        cout<<" IMPOSSIBLE";
                        else
                        for(temp1=2;temp1<=num1*num1;temp1=temp1+num1+1)
                        cout<<" "<<temp1;
                    }
                cout<<endl;
            }
     }
     //cin>>temp1;
    return 0;
}
