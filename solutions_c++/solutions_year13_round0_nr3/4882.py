#include<stdio.h>
#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
#define mod 1000000009
#define ll long long

using namespace std;

int main()
{
    int t,n,i,j,count,a,b;
    ll arr[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    for(i=0;i<t;i++)
    {
        scanf("%d%d", &a, &b);
        n=sizeof(arr)/sizeof(arr[0]);
        count=0;
        for(j=0;j<=n;j++)
        {
            if(arr[j]<=b&&arr[j]>=a)
                count++;
        }
        printf("Case #%d: %d\n", i+1,count);
    }
	return 0;
}
