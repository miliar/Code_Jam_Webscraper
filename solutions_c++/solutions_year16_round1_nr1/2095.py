#include <bits/stdc++.h>
#define MAXA 100005
#define MOD 1000000007
using namespace std;
char a[1005];
int main()
{
    freopen("A-large.in","r+",stdin);
    freopen("output1.txt","w+",stdout);
    int t,i,t1=1;
    cin>>t;
    while(t--)
    {
        scanf("%s",&a);
        int l=strlen(a);
        deque<char> q;
        q.push_back(a[0]);
        for(i=1;i<l;i++)
        {
            char temp=q.front();
            if(a[i]>=temp)
                q.push_front(a[i]);
            else
                q.push_back(a[i]);
        }
        printf("Case #%d: ",t1);
        while(!q.empty())
        {
            printf("%c",q.front());
            q.pop_front();
        }
        printf("\n");
        t1++;
    }
    return 0;
}
