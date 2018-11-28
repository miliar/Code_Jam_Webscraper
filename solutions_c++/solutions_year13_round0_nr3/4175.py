
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int t,rec=0,ans;
long long da,db,data[1000]={
1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};

bool judge(long long a)
{
    long long xa,xb;
    xa=a; xb=0;
    while (a)
    {
        xb=xb*10+(a%10);
        a=a/10;
    }
    return xa==xb;
}

int main()
{
    int i;
    long long x;
    cin>>t;
    while (t--)
    {
        rec++;
        cin>>da>>db;
        ans=0; i=0;
        while (data[i])
        {
            x=data[i];
            if (x*x>=da && x*x<=db && judge(x) && judge(x*x)) ans++;
            i++;
        }
        printf("Case #%d: %d\n",rec,ans);
    }
    return 0;
}
