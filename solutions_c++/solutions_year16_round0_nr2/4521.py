#include<iostream>
#include<stdio.h>
#include<cmath>
#include<string>
using namespace std ;


main()
{
    int T,l,cnt=0;
    string S;
    freopen("B-large.in","r",stdin) ;
    freopen("bout.txt","w",stdout) ;
    cin>>T;
    for (int i=0;i<T;i++)
    {
        cnt=0;
        cin>>S;
        l = S.length();
        if(l==1)
        {
            if (S[0]=='-')
                cnt=1;
        }
        else
        {
            for (int j=0;j<(l-1);j++)
            {
                if (S[j]!=S[j+1])
                    cnt++;

            }
            if(S[l-1]=='-')
                cnt++;
        }

        cout<<"Case #"<<(i+1)<<": "<<cnt<<endl;

    }
}
