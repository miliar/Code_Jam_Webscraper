#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<bitset>
#include<time.h>
#define ll __int64
#define inf 0x7FFFFFFF
#pragma comment(linker, "/STACK:102400000,102400000")
using namespace std;
int main()
{
    int i,j,k;
    int n,m,t;
    //srand((unsigned)time(NULL));//int data=rand()%10000+1;
    freopen("A-large.in","r",stdin);freopen("A-output-large.txt","w",stdout);
    scanf("%d",&t);for(int tcase=1;tcase<=t;tcase++)
    //while(scanf("%d",&n)!=EOF)
    {
        scanf("%d",&n);
        char ch[10000];
        scanf("%s", ch);
        int nowNum = 0;
        int addNum = 0;
        for (i=0; i<=n; i++)
        {
            if (ch[i] == '0')
                continue;
            int now = ch[i]-'0';
            if (i<=nowNum)
            {
                nowNum+=now;
            }
            else
            {
                addNum+=i-nowNum;
                nowNum=i+now;
            }
        }
        printf("Case #%d: %d\n", tcase, addNum);
    }
}
