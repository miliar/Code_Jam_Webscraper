#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
string mat[101];
    int R,C;
bool ok(int i,int j)
{
    for(int k=i+1;k<R;k++)
        if(mat[k][j] != '.')
            return true;
    for(int k=i-1;k>=0;k--)
        if(mat[k][j] != '.')
            return true;
    for(int k=j+1;k<C;k++)
        if(mat[i][k] != '.')
            return true;
    for(int k=j-1;k>=0;k--)
        if(mat[i][k] != '.')
            return true;
    return false;
}


int main()
{
    freopen("c:\\codejam\\A-large.in", "r", stdin);
    freopen("c:\\codejam\\A-large.out", "w", stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        int ans = 0;
        bool suc = true;
        scanf("%d %d",&R,&C);
        for(int i=0;i<R;i++)
        //    scanf("%s",mat[i].c_str());
            cin>>mat[i];
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
            {
                if(mat[i][j] == '^')
                {
                    bool flag = false;
                    for(int k=i-1;k>=0;k--)
                    {
                        if(mat[k][j] != '.'){
                            flag = true;
                            break;
                        }
                    }
                    if(!flag)
                    {
                        if(ok(i,j))
                            ans++;
                        else
                            suc = false;
                    }
                }
                else if(mat[i][j] == '>')
                {
                    bool flag = false;
                    for(int k=j+1;k<C;k++)
                    {
                        if(mat[i][k] != '.'){
                            flag = true;
                            break;
                        }
                    }
                    if(!flag)
                    {
                        if(ok(i,j))
                            ans++;
                        else
                            suc = false;
                    }
                }
                else if(mat[i][j] == '<')
                {
                    bool flag = false;
                    for(int k=j-1;k>=0;k--)
                    {
                        if(mat[i][k] != '.'){
                            flag = true;
                            break;
                        }
                    }
                    if(!flag)
                    {
                        if(ok(i,j))
                            ans++;
                        else
                            suc = false;
                    }
                }
                else if(mat[i][j] == 'v')
                {
                    bool flag = false;
                    for(int k=i+1;k<R;k++)
                    {
                        if(mat[k][j] != '.'){
                            flag = true;
                            break;
                        }
                    }
                    if(!flag)
                    {
                        if(ok(i,j))
                            ans++;
                        else
                            suc = false;
                    }
                }
            }

        printf("Case #%d: ",cas++);
        if(suc)
        {
            printf("%d\n",ans);
        }
        else
        {
            puts("IMPOSSIBLE");
        }
    }
    return 0;
}
