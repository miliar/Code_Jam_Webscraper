#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define lli long long int
#define gc getchar//_unlocked
#define mod 1000000007
#define pii pair<int,int>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,n,l,r=0;
    char arr[1009];
    cin>>t;
    while(t-->0)
    {
        cin>>l;
        cin>>arr;
        int curr=0,ans=0;
        for(i=0;i<=l;i++)
        {
            j=int(arr[i]-'0');
            if(curr>=i)curr+=j;
            else if(j!=0){
                ans+=(i-curr);
                curr=i+j;
            }
        }
        printf("Case #%d: %d\n",++r,ans);
    }
    return 0;
}
