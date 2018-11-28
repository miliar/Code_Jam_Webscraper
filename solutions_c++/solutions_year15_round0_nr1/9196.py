#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <complex>
#include <climits>
#define MAX 1005
#define ll long long
using namespace std;

int main()
{ freopen("input.txt", "r", stdin);

    int t,n,i,j,total,len,ans;
    char s[MAX];


    //scanf("%d",&t);
    cin>>t;
  freopen("out.txt", "w", stdout);
    for(j=0;j<t;j++)
    {
        //scanf("%d %s",&n,s);
         cin>>n;
         cin>>s;
        total=ans=0;

        len=strlen(s);
        //printf("%d\n",len);
        for(i=0;i<len;i++)
        {
            total+=s[i]-'0';
          if(total<i+1)
            {ans+=i+1-total;
              total+=i+1-total;
            }
           // printf("%d ",ans);
        }
    //     printf("\n");


        printf("Case #%d: %d\n",j+1,ans);

    }



    return 0;
}
