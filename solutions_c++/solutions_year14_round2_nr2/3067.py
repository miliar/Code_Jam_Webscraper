#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
    long long int sl=1, i, j, t, a, b, k, ct=0;
    cin>>t;
    while (t--)
    {
        ct=0;
        cin>>a>>b>>k;
        for (i=0; i<a; i++)
        {
            for (j=0; j<b; j++)
            {
                if ((i&j)<k)
                {
                    ct++;
                }
            }
        }
        cout<<"Case #"<<sl++<<": "<<ct<<endl;
    }
    return 0;
}