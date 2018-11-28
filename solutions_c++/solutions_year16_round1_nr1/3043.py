#include<bits/stdc++.h>


using namespace std;

deque <int> dq;
char s[1010];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t,ti,l,i,j,k;
    scanf("%d",&t);
    for(ti=1; ti<=t; ++ti)
    {
        while(!dq.empty())
            dq.pop_back();
        scanf("%s",s);
        l=strlen(s);
        for(i=0; i<l; ++i)
        {
            if(dq.empty())
                dq.push_back(s[i]);
            else
            {
                if(s[i]>=dq.front())
                    dq.push_front(s[i]);
                else
                    dq.push_back(s[i]);
            }
        }
        printf("Case #%d: ",ti);
        while(!dq.empty())
        {
            printf("%c",dq.front());
            dq.pop_front();
        }
        puts("");
    }
    return 0;
}
