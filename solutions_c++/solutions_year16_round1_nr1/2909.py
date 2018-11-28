#include<bits/stdc++.h>
using namespace std;
char s[1135];
deque<char> q;
int main()
{
    int t,T,i,j,k,len,mc;
//    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%s",s);
        len=strlen(s);
        q.emplace_back(s[0]);
        mc=s[0];
        for(i=1;i<len;i++)
        {
            if(s[i]>=q.front())
            {
                q.emplace_front(s[i]);
            }
            else
            {
                q.emplace_back(s[i]);
            }
        }
        printf("Case #%d: ",t);
        while(!q.empty())
        {
            printf("%c",q.front());
            q.pop_front();
        }
        printf("\n");
    }
}

