#include <bits/stdc++.h>
using namespace std;

int check(int *arr)
{
    for(int i=0;i<10;i++)
    if(!arr[i])
    return 0;

    return 1;
}

int main()
{
    //freopen("cj1.in","r",stdin);
    //freopen("out.txt","w",stdout);
    long long n,num,t,curr,copy;
    cin>>t;
    for(int co=1;co<=t;co++)
    {
    int arr[10]={0};
        cin>>n;
        curr=copy=n;
        if(!n)
        cout<<"Case #"<<co<<": "<<"INSOMNIA"<<endl;
        else
        {
            while(1)
            {
            copy=curr;

                while(copy)
                {
                arr[copy%10]++;
                copy/=10;
                }
            if(check(arr))
            {cout<<"Case #"<<co<<": "<<curr<<endl;
            break;}
            curr+=n;
            }
        }
    }
    return 0;
}


