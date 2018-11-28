#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int check(int n)
{
    int rev=0,ori=n,r;
    while(n>0)
    {
        r=n%10;
        rev = (rev*10) + r;
        n= n/10;
    }

    if(ori==rev)
        return 1;

    else
        return 0;
}

int main()
{
    freopen("fair.txt","r",stdin);
    freopen("output1.txt","w+",stdout);

    int tc,cases,count,i,a,b,sq1,sq2,num;
    cin>>tc;

    for(cases=1; cases<=tc;cases++)
    {
        count=0;
        cin>>a>>b;
        sq1 = ceil(sqrt(a));
        sq2 = sqrt(b);

        for(i=sq1;i<=sq2;i++)
        {
            if(check(i))
            {
                num = i*i;
                if(check(num))
                    count++;
            }
        }

        cout<<"Case #"<<cases<<": "<<count<<"\n";
    }
    return 0;
}
