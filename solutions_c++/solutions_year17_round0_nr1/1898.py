#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
#define maxn 1000100
#define maxm 10010
#define inf 0x3f3f3f3f

using namespace std;

string st;

int main()
{
    int m,T,len,len1,p,ans,top,cas = 1;
    bool flag;
    scanf("%d",&T);
    while(T--)
    {
        flag = true;
        ans = 0, top = 0;
        queue<int>que;
        cin>>st;
        scanf("%d",&m);
        len1= st.length();
        string str="";
        for(int j = 0;j < len1;++ j)
        {
            if(st[j]=='-')
                str+='1';
            else
                str+='0';
        }
        len=str.length();
        for(int i = 0; i < len;++ i)
        {
            if(!que.empty() && que.front() < i)
                que.pop();
            p = que.size() + str[i] - '0';
            if(p % 2)
            {
                ans++;
                if(i + m - 1 >= len)
                {
                    flag = false;
                    break;
                }
                que.push(i+m-1);
            }
        }
        if(flag)
            printf("Case #%d: %d\n",cas,ans);
        else
            printf("Case #%d: IMPOSSIBLE\n",cas);
        cas++;
    }
    return 0;
}
