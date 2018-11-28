#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t,ca=1;
    cin>>t;

    while(t--)
    {
        long long n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<ca<<": INSOMNIA"<<endl;
            ca++;
            continue;
        }
        vector<int> num(10);
        int mul=1;
          long long b;
        while(1){
           long long a= mul*n;
           b=a;
             int dig;
        while(a)
        {
            dig=a%10;
            num[dig]=1;
            a=a/10;
        }
        int flag=1;
        for(int i=0;i<10;i++)
        if(!num[i])
        {
            flag=0;
            break;
        }
        if(flag)
        break;
        mul++;

        }

        cout<<"Case #"<<ca++<<": "<<b<<endl;

    }


    return 0;
}
