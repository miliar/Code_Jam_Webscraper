#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
int t,n;
string s;

int main()
{
       freopen("A-large.in", "r" , stdin);
   freopen("output.txt" , "w" , stdout);
    cin>>t;
    int case1=0;
    while(t--)
    {
        cin>>n>>s;
        int sum=0;
        int max1=0,k=0;
        for(int i=0; i<n+1; i++)
        {
           if(s[i]!=0)
           {
               sum=0;
              for(int j=0; j<i; j++)
              {
                  sum+=s[j]-'0';
              }
              if(sum<i)
              {
                  k=i-sum;
              }
              //cout<<sum<<" "<<i<<endl;

           }
           if(k>max1)
           {
               max1=k;
           }
        }
        printf("Case #%d: ",++case1);
        printf("%d\n",max1);
    }
    return 0;
}
