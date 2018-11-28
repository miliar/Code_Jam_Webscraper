#include <string>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <iomanip>
#include <limits.h>
using namespace std;

#define max(a,b) (a>=b?a:b)
#define min(a,b) (a<=b?a:b)
#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int N,i,j,T,cnt,t;
char a[4][4];
int won(char c);

int main()
{
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        for(i=0;i<4;i++) scanf(" %s",a[i]);
        cnt=0;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
          if(a[i][j]!='.') cnt++;
        if(won('X')) printf("Case #%d: X won\n",t);
        else if(won('O')) printf("Case #%d: O won\n",t);
        else if(cnt==16) printf("Case #%d: Draw\n",t);
        else printf("Case #%d: Game has not completed\n",t);
    }

    return 0;
}

int won(char c)
{
    int n3=0,n4=0;
    for(i=0;i<4;i++)
    {
        int num1=0,num2=0;
        for(j=0;j<4;j++)
        {
            if(a[i][j]==c || a[i][j]=='T') num1++;
            if(a[j][i]==c || a[i][j]=='T') num2++;
        }
        if(num1==4 || num2==4) return 1;
        if(a[i][i]==c || a[i][i]=='T') n3++;
        if(a[i][3-i]==c || a[i][3-i]=='T') n4++;
    }
    if(n3==4 || n4==4) return 1;
    return 0;
}
