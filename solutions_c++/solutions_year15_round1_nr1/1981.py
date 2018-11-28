#include <vector>
#include <climits>
#include <stack>
#include <map>
#include <algorithm>
#include <list>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <queue>
#define ll long long
#define s1(a) scanf("%d",&a)
#define sc(a) scanf("%c",&a)
#define s1ll(a) scanf("%lld",&a)
#define s2(a,b) scanf("%d %d",&a,&b)
#define s2ll(a,b) scanf("%lld %lld",&a,&b)
#define s1d(a) scanf("%lf",&a)
#define s2d(a,b) scanf("%lf %lf",&a,&b)
#define p1(a) printf("%d\n",a)
#define pc(a) printf("%c\n",a)
#define p1ll(a) printf("%lld\n",a)
#define p1d(a) printf("%lf\n",a)
#define MAX 1000000
using namespace std;
ll int comp1(int arr[],int n)
{
    ll int sum=0;
    for(int i=1;i<n;i++)
    {
        if(arr[i]<arr[i-1])
            sum+=arr[i-1]-arr[i];
    }
    return sum;
}
ll int comp2(int arr[],int n)
{
    int max=0;
    for(int i=1;i<n;i++)
    {
        if(max<arr[i-1]-arr[i])
            max=arr[i-1]-arr[i];
    }
   // cout<<max<<endl;
    ll int sum=0;
    for(int i=0;i<n-1;i++)
    {
        if(max>arr[i])
        {
            sum=sum+arr[i];
        }
        else
        {
            sum=sum+max;
        }
    }
    return sum;
}
int main()
{
    int t;
    s1(t);
    for(int ii=1;ii<=t;ii++)
    {
        int n;
        s1(n);
        int arr[n];
        for(int i=0;i<n;i++)
        {
            s1(arr[i]);
        }
        cout<<"Case #"<<ii<<": "<<comp1(arr,n)<<" "<<comp2(arr,n)<<endl;
    }
}