#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<map>

using namespace std;
map<int, bool> mp;



bool Check()
{
    for(int i=0;i<=9;i++)
    {
        if(mp[i] == false) return false;
    }

    return true;
}

void UpdateMap(int value)
{
    while(value)
    {
        mp[value%10] = true;
        value/=10;
    }
}
int main()
{
    freopen("1.txt", "r+", stdin);
    freopen("outputA.txt", "w+", stdout);
    //freopen("test.txt", "w+", stdout);

    long long n, prevValue;
    long long startMultiplyer;
    int kount = 0;
    long long TestCase;
    cin>>TestCase;
    while(TestCase--)
    {
        cin>>n;
        mp.clear();

        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", ++kount);
            continue;
        }

        startMultiplyer = 1;
        prevValue = n;
        while(true)
        {
            UpdateMap(prevValue);
            if(Check())
            {
                printf("Case #%d: %lld\n",++kount, prevValue);
                break;
            }
            prevValue = n*startMultiplyer;
            startMultiplyer++;
        }
    }
    return 0;
}
