#include <bits/stdc++.h>

using namespace std;

void solve(int smax,char help[])
{
    int ans=0;
    int len=smax+1;
    int curr=0;
    for(int i=0;i<len;i++)
    {
        if(curr<i && help[i]!='0')
        {
            ans=ans+(i-curr);
            curr=curr+(i-curr);
        }
        curr=curr+(help[i]-'0');

    }
    cout << ans << "\n";
    return ;
}

int main()
{
    freopen("al.in", "r", stdin);
  freopen ("myfile22.txt","w",stdout);
int t,smax;
cin >> t;
char help[1007];
for(int i=0;i<t;i++)
{
    scanf("%d%s",&smax,help);
    printf("Case #%d: ", i+1);
    solve(smax,help);
}
return 0;
}
