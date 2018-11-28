                    /* Original Author: Akash Sinha(sinaka)
                       Language: C++ 4.3.2
                    */
using namespace std;
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <bitset>

//DEFINITIONS

#define LL  long long int
#define ULL  unsigned long long int
#define DB double
#define LDB long double
#define PB push_back
#define MP make_pair
#define SL(a) scanf("%lld",&a)
#define S(a) scanf("%d",&a)
#define SC(a) scanf("%c",&ch)
#define SD(a) scanf("%lf",&a)
#define PL(a) printf("%lld",a)
#define P(a) printf("%d",a)
#define PC(a) printf("%c",a)
#define PD(a) printf("%lf",a)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define NL printf("\n")
#define W(t) while(t--)
#define FOR(i,lo,hi) for(i=lo;i<hi;i++)
#define gc getchar_unlocked
#define MOD 1000000007

int n;
bool vowel(char ch)
{
     if((ch=='a')||(ch=='e')||(ch=='i')||(ch=='o')||(ch=='u'))
     return true;
     return false;
}

bool fun(vector<char> &v)
{
     int i,j,k,c=0;
     for(i=0;i<v.size();i++)
     {
        c=0;
        k=0;
        for(j=i;(j<v.size())&&(k<n);j++,k++)
        
           if(!vowel(v[j]))
           c++;
           
           
        
        if(c==n)
        return true;
     }
     return false;
}
     


int main()
{
   //freopen("C:\\Users\\Dell\\Desktop\\input.txt","r",stdin);
   //freopen("C:\\Users\\Dell\\Desktop\\output.txt","w",stdout);
   
   char arr[200];
   int t,i,j,k,len,c,tc,ans;
   scanf("%d",&t);
   for(tc=1;tc<=t;tc++)
   {
      scanf("%s",arr);
      scanf("%d",&n);
      len=strlen(arr);
      ans=0;
      for(i=0;i<len;i++)
      {
         vector<char> v;
         for(j=i;j<len;j++)
         {
            v.push_back(arr[j]);
            if(fun(v))
            ans++;
            
            
         }
      }
      printf("Case #%d: %d\n",tc,ans);
   }
   return 0;
}
