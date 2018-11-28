#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#define maxn 105
#define maxl 105
#define M 1000000007
using namespace std;

    char ch[maxn][maxl];
    long long jie[105];
    vector<int> ch[300];
    long long vis[300];
    int num[300];//buhelifu
    int in[300];
    int f[300];
    int flag=0;
    int ru[300];
    int ch[300];
    vector<int> dui[30];
    long long ans[30];
    int sum=0;

    void f(int x)
    {
        int l=strlen(ch[x]);
        int n=1;
        int a[300]={0};//chuxian

        a[ch[x][0]]=1;

        for (i=0;i<l;i++)
        if (num[ch[x][i]]==-1)
            {
                    flag=1;return;
            }



        for (i=1;i<l;i++)
            if (ch[x][i]!=ch[x][i-1])
            {
                n++;
                if ( a[ch[x][i]]==0 ) a[ch[x][i]]=1;
                else
                {
                    flag=1;return;
                }
            }

        if (n>2)
        {
            for (i=0;i<l;i++)
                if ( ch[x][i]!=ch[x][0] && ch[x][i]!=ch[x][l-1] )
                  num[ch[x][i]]=-1;
        }

        num[ch[x][l-1]]=num[ch[x][0]]=1;

        if ( n==1 ) vis[ch[x][0]]++;
        else if (n==2)
        {
            g[ch[x][0]].push_back(ch[x][l-1]);
            ru[ch[x][l-1]]++;
            chu[ch[x][0]]++;
        }

    }

    void dfs(int x)
    {
        if (in[x]==1)
            {
                    flag=1;return;
            }

        in[x]=1;
        dui[sum].push_back(x);
        if (g[x].size()>1)
            {
                    flag=1;return;
            }

        if (g[x].size()==0) return;

        dfs(g[x][0]);

    }


    void pan(int x)
    {
         if (chu[x]>1||ru[x]>1)
            {
                flag=1;return;
            }

         if (ru[x]==0&&num[x]==1)
         {
             sum++;
             dfs(x);
         }
    }


   int main()
   {
       int T,tt=0;
       int n,i;

       cin>>T;
       jie[1]=1;

       for (i=2;i<=100;i++)
        jie[i]=jie[i-1]*i%M;

       while (T--)
       {
           printf("Case #%d: ",++tt);
           memset(vis,0,sizeof(vis));
           memset(num,0,sizeof(num));
           sum=0;

           for (i='a';i<='z';i++) g[i].clear();

           flag=0;
             cin>>n;
             for (i=1;i<=n;i++)
                cin>>ch[i];

             for (i=1;i<=n&&flag==0;i++)
                f(i);//heli

             for (i='a';i<='z'&&flag==0;i++)
             pan(i);//huilu

             if (flag) {printf("0\n");continue;}

             for (i='a';i<='z';i++)
                if (vis[i]>0) vis[i]=jie[vis[i]];





       }





       return 0;
   }



