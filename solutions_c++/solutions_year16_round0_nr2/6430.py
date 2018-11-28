#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
#define  ll long long
#define endl '\n'
char a[200];
int solve(int n)
{
   if(n==0) return 0;
   int ans=1;
   for(int i=1;i<n;i++)
   {
       if(a[i]!=a[i-1]) ans++;
   }
   return ans;
}
int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t,cas=1,n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",a);
        n=strlen(a);
        for(int i=n-1;i>=0;i--)
        {
            if(a[i]=='-') break;
            n--;
        }
        cout<<"Case #"<<cas++<<": ";
        cout<<solve(n)<<endl;
    }
    return 0;
}
