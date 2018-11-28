#include<bits/stdc++.h>
using namespace std;
#define LL long long int

LL solve(LL n)
{
    int arr[10];
    LL val = 1;
    memset(arr,0,sizeof(arr));

    while(true)
    {
        LL num = n*val;

        while(num>0)
        {
            arr[num%10] = 1;
            num/=10;
        }

        bool flag = true;
        for(int i = 0; i<10;i++)
        {
            if(arr[i]==0)
            {
                flag = false;
                break;
            }
        }

        if(flag)
            break;

        val++;
    }

    return (n*val);
}

int main()
{
    int t,test;
    LL n;

    freopen("a-large.in","r",stdin);
    freopen("a-large.out","w",stdout);

    cin>>test;

    for(t=1;t<=test;t++)
    {
        cin>>n;

        cout<<"Case #"<<t<<": ";
        if(n==0)
            cout<<"INSOMNIA"<<endl;
        else
            cout<<solve(n)<<endl;
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
