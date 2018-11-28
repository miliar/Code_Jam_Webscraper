/*
Shamim Ehsan
SUST CSE 12
*/
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>
#include<limits.h>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<deque>
#include<algorithm>
#include<sstream>
#define PI (2* acos(0))
#define pb push_back
#define ll long long
using namespace std;
//int X[]= {0,0,1,-1};
//int Y[]= {-1,1,0,0};
//int X[]= {0,0,1,1,1,-1,-1,-1};
//int Y[]= {-1,1,0,1,-1,0,1,-1};
char cake[1500];
int len;
bool check()
{
    for(int i=0; i<len; i++)
        if(cake[i]=='-')
            return true;
    return false;
}
void change(int n)
{
//    cout<<n<<endl;
    for(int i=0; i<=n/2; i++)
        swap(cake[i],cake[n-i]);
    for(int i=0; i<=n; i++)
        {
//            printf("bal %c \n",cake[i]);
            if(cake[i]=='-')
            cake[i]= '+';
        else
            cake[i]= '-';

        }


}
#include<conio.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("newoutput.txt","w",stdout);

    int t,n,temp;
    scanf("%d",&t);
//    getchar();
   // printf("%d\n",t);
    int ans=0;

    for(int cs=1; cs<=t; cs++)
    {
        ans=0;
        scanf("%s",cake);
     //       printf("%s\n",cake);
   // continue;
        len = strlen(cake);
        while(check())
        {
            char pos = cake[0];
            int in=1;
            while(cake[in]==pos)
                in++;
                change(in-1);
                ans++;

//            char pos2 = cake[in];
//            while(cake[in]==pos2)
//                in++;
//

//           puts(cake);
//            getche();
        }

        printf("Case #%d: %d\n",cs,ans);

    }

    return 0;
}


