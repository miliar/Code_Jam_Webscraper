#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string>
#include<string.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    long long t;
    cin>>t;
    for (int i=1; i<=t; i++)
    {
        string a;
        long long count = 0;
        cin>>a;
        if (a[0] == '-')
        {
            count ++;
        }
        for (int i1=0; i1<a.size(); i1++)
        {

            if (a[i1] == '+')
            {
                if (a[i1+1] == '-')
                {
                    count = count+2;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<count<<endl;

    }
}

