#include<iostream>
#include<cstdio>
#include<climits>
#include<vector>
#include<algorithm>
#include<utility>
#include<cmath>
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
typedef long long int ull;
using namespace std;

string s;

int main()
{
   int t,n,i,j,k;
   read(t);
   for(j=1;j<=t;j++)
   {
   	read(n);
    cin>>s;
    int stand=s[0]-48,req=0;
    for(i=1;i<=n;i++)
    {
         if(stand<i)
         	{
         		req+=i-stand;
         		stand+=i-stand;
         	}

         stand+=s[i]-48;
    }
    printf("Case #%d: %d\n",j,req);
   }

}