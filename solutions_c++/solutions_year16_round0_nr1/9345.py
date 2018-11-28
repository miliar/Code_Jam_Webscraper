#include <bits/stdc++.h>
using namespace std;
int main()
{     freopen("A-large.in", "r", stdin);
     freopen("A-large.txt", "w", stdout);
    long long t,n,a,b,counter=0;
    bool test=true;
    cin>>t;
    for (int i=1; i<=t; i++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        counter=0;
        a=0;
        int arr[50] {};
        test=true;
        while (test)
        {
            counter++;
            a=n*counter;
            while (a>0)
            {
                b=a%10;
                arr[b]+=1;
                a=a/10;
            }

            for (int j=0; j<=9; j++)
            {
                test=false;
                if (arr[j]<1)
                {
                    test=true;
                    break;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<n*counter<<endl;
    }
}
