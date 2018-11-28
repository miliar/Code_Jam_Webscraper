
#include <cstdio>
#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <string.h>
#include <cstring>
#include <InfInt.h>

using namespace std;

int main()
{
    int t, u, i, d, no_of_digits, digits[10];
    long long num, n;
    freopen("AL.in", "rt", stdin);
    freopen("AL.out", "wt", stdout);
    cin>>t;
    u=1;
    while(u<=t)
    {
        cin>>n;
        cout<<"Case #"<<u<<": ";
        u++;
        if(n==0)
            goto insom;
        num=n;
        for(i=0;i<10;i++)
            digits[i]=0;
        no_of_digits=0;
        while(no_of_digits!=10)
        {
            long long temp=num;
            while(temp!=0)
            {
                
                d=temp%10;
                if(digits[d]==0)
                {
                    no_of_digits++;
                    digits[d]=1;
                }
                temp/=10;
                
            }
            num+=n;
        }
        num-=n;
        if(no_of_digits==10)
        {
            cout<<num<<endl;
            continue;
        }
        
        insom: cout<<"INSOMNIA\n";
            
    }
    return 0;
}

/**/

