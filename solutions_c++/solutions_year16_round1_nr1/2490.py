#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
#define DEBUG

char str[1010];

void dfs(int len)
{
    if(len <= 0)return;
    char big = 0;
    int index = -1;
    for(int i=0;i<len;i++)
    {
        if(str[i]>=big)
        {
            big = str[i];
            index = i;
        }
    }
    putchar(big);
    dfs(index);

    for(int i=index+1;i<len;i++)
    {
        putchar(str[i]);
    }
}
int main()
{
    #ifdef DEBUG
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif //DEBUG

    int t;
    cin>>t;


    for(int ti=1;ti<=t;ti++)
    {
        cin>>str;
        printf("Case #%d: ",ti);
        dfs(strlen(str));
        putchar('\n');
    }
    return 0;
}
