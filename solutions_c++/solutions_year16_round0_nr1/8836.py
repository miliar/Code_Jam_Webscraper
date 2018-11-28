#include <iostream>
#include <stdio.h>

using namespace std;

bool check(bool arr[])
{
    for(int i=0; i<10; i++)
    {
        if(arr[i]==0)
            return 0;
    }
    return 1;
}

int MyNum(int n)
{
    bool tab[10] = {0}, flag=0;
    long long num, temp=0;
    while(!flag)
    {
        temp += n;
        num = temp;
        //cout<<"Testing for "<<num<<endl;
        while(num)
        {
            int dig = num%10;
            tab[dig] = 1;
            num /= 10;
        }
        flag = check(tab);
    }
    return temp;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, n;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        cin>>n;
        if(n==0)
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<MyNum(n)<<endl;
    }
    return 0;
}
