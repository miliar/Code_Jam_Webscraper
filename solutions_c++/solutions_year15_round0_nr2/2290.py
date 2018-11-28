#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include<stdint.h>
#include<stdio.h>
using namespace std;
int main()
{
    int t,testcase;
    testcase=1;
    cin>>t;
    while(t--)
    {
        int d,i,flag,eatm,tsize=0;
        cin>>d;
        int a[1100],time[1100];
        for(i=0;i<d;i++)
        scanf("%d",&a[i]);
        sort(a,a+d);
        for(eatm=1;eatm<=a[d-1];eatm++)
        {   
    		flag=0;
            for(i=0;i<d;i++)
            {   
                if(a[i]>eatm)
                flag+=(a[i]-1)/eatm;
            }
            time[tsize++]=flag+eatm;
        }
        sort(time,time+tsize);
        cout<<"Case #"<<testcase<<": "<<time[0]<<endl;
        testcase++;
    }
    return 0;
}
