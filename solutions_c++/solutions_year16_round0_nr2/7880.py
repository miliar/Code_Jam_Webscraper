#include <bits/stdc++.h>

using namespace std;

int t;
string line;

int main()
{
    freopen("B-large.out", "w", stdout);
    scanf("%d", &t);
    getchar();
    for(int i=1; i<=t; i++)
    {
        getline(cin, line);
        string tmp = "";
        for(int j=line.length()-1; j>=0; j--)
        {
            if(line[j]=='-')
            {
                tmp = line.substr(0, j+1);
                break;
            }
        }
        if(tmp.length()==0)
        {
            printf("Case #%d: 0\n", i);
            continue;
        }
        bool flag;
        if(tmp[tmp.length()-1]=='+') flag = true;
        else flag = false;
        int ans = 1;
        for(int j=tmp.length()-2; j>=0; j--)
        {
            if(tmp[j]=='+' && flag) continue;
            else if(tmp[j]=='-' && !flag) continue;
            else
            {
                ans++;
                flag = tmp[j]=='+';
            }
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
