#include<iostream>
#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    freopen("in1.txt","r",stdin);
    freopen("out1.txt","w",stdout);

    long long t, sMax, mCount, fCount, p;
    string sMaxString;

    cin>>t;

    for(int i=1;i<=t;i++)
    {
        cin>>sMax;

        cin>>sMaxString;

        mCount = 0;
        fCount = 0;
        p = 0;

        for(int j=0;j<=sMax;j++)
        {
            if(j == 0) mCount += sMaxString[j]-48;
            else{
                int y = sMaxString[j]-48;

                if(mCount < j && y > 0)
                {
                    fCount += abs(j - mCount);
                    p = abs(j - mCount);
                }

                if(y > 0)
                {
                    mCount += sMaxString[j]-48;
                    mCount += p;
                    p = 0;
                }
            }
        }

        cout<<"Case #"<<i<<": "<<fCount<<endl;
    }

    return 0;
}
