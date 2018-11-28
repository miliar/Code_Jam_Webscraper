#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;
vector<char> chs[110];
vector<int> cnts[110];
char str[100][111];
int main()
{
    freopen("C:\\codejam\\A-small-attempt00.in","r",stdin);
    freopen("C:\\codejam\\a.in","w",stdout);
    int T,out=1;
    int n;
    scanf("%d",&T);

    while(T--){
        memset(str,0,sizeof(str));
        memset(chs,0,sizeof(chs));
        memset(cnts,0,sizeof(cnts));
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            int cnt = 0;
            str[i][0] = 'A';
            scanf("%s",str[i]+1);
            chs[i].push_back('A');
            for(int j=1;j<=strlen(str[i]);j++)
            {
                if(str[i][j] != str[i][j-1])
                    chs[i].push_back(str[i][j]),cnts[i].push_back(cnt),cnt = 1;
                else
                    cnt++;
            }
        }
        int flag = 1;
        int sz = chs[0].size();
        for(int i=0;i<n;i++)
        {
            if(chs[i].size() != sz) {flag = 0; break;}
        }
        for(int i=1;i<sz-1;i++)
        {
            for(int j=0;j<n-1;j++)
                if(chs[j][i] != chs[j+1][i])
                {
                    flag = 0;
                    break;
                }
        }
        if(!flag)
        {
            printf("Case #%d: ",out++);
            puts("Fegla Won");
        }
        else {
        int ans = 0;
        for(int i=1;i<sz-1;i++)
        {
            vector<int> temp;
            for(int j=0;j<n;j++)
                temp.push_back(cnts[j][i]);
            sort(temp.begin(),temp.end());
            for(int i=0;i<temp.size();i++)
                ans += abs(temp[i] - temp[temp.size()/2]);
        }
        printf("Case #%d: %d\n",out++,ans);


        }

    }
    return 0;
}
