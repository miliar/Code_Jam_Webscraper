#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long int t,n,ans,index,temp,temp1;
    bool a[10],check;
    cin>>t;
    for (long long int x=0;x<t;x++)
    {
        cin>>n;
        if (n==0)
        {
            cout<<"Case #"<<x+1<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        for (int i=0;i<10;i++)
            a[i]=false;
        ans = 0;
        index = 1;
        temp = n;
        temp1 = temp;
        check;
        while (1)
        {
            temp = index*n;
            temp1 = temp;
            index++;
            while (temp)
            {
                a[temp%10] = true;
                temp/=10;
            }
            check = a[0];
            for (int i=1;i<10;i++)
                check = check & a[i];

            if (check)
            {
                cout<<"Case #"<<x+1<<": "<<temp1<<endl;
                break;
            }
        }
    }
}
