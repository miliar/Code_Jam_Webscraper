#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<stdlib.h>
using namespace std;
int main()
{
    int t,testcase,box,alag,complete,flag,temp;
    testcase=1;
    cin>>t;
    while(t--)
    {
        flag=1;
        cin>>box;
        cin>>alag;
        cin>>complete;
        temp=alag*complete;
        if((temp)%box==0)
        {
            if(box==4)
            {
                if(complete<3 || alag<3)
                flag=0;
            }
            else if(box==3)
            {
                if(complete<2 || alag<2)
                flag=0;
            }
            else
            flag=1;   
        }
        else
        flag=0;
        if(flag==1)
        cout<<"Case #"<<testcase<<": "<<"GABRIEL"<<endl;
        else
        cout<<"Case #"<<testcase<<": "<<"RICHARD"<<endl;
        testcase++;
    }
    return 0;
}

