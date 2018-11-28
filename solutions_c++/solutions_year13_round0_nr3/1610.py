#include<vector>
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<assert.h>
#include<stdlib.h>
#include<sstream>
#define LIMIT 10000000
#define ull unsigned long long int
using namespace std;
/*
bool ispalin(ull num)
{
    string s;
    stringstream ss;
    ss<<num;
    s=ss.str();
    //cout<<s<<"\n";
    int l=s.length(),i;
    for(i=0;i<l;i++)
    {
        if(s[i]!=s[l-i-1])
        break;
    }
    if(i==l)
    return 1;
    return 0;
}
void preprocess()
{
    int cnt=0;
    for(ull i=1;i<=LIMIT;i++)
    {
        ull sq=i*i;
        if(ispalin(i)&&ispalin(sq))
        {
            cout<<sq<<",";
            cnt++;
        }

    }
    cout<<cnt<<"\n";
}*/
ull arr[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,
125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,
1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,
1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
int main()
{
    //preprocess();
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        ull a,b;
        scanf("%llu %llu",&a,&b);

        int cnt=0;
        for(int j=0;j<39;j++)
        {
            if(arr[j]>=a&&arr[j]<=b)
            cnt++;
        }

        printf("Case #%d: %d\n",i,cnt);
    }
    return 0;
}
