#include<bits/stdc++.h>
using namespace std;

char ss[1050];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-solve.txt","w",stdout);
    int test,no=0;
    scanf("%d",&test);
    while(test--)
    {
        int n; scanf("%d",&n);
        scanf("%s",ss);
        int add = ss[0]-48;
        int ans = 0;
        int len = strlen(ss);
        //cout << len << endl;
        for(int i=1;i<len;i++)
        {
           // cout << add << endl;
            if(ss[i] == '0') continue;
            if(add < i) { ans += (i-add); add += (i-add); }
            add += (ss[i]-48);
        }
        printf("Case #%d: %d\n",++no,ans);
    }
    return 0;
}
